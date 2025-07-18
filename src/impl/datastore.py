from typing import List
from interface.base_datastore import BaseDatastore, DataItem
import lancedb
from lancedb.table import Table
import pyarrow as pa
from concurrent.futures import ThreadPoolExecutor
from src.util.embedding import embed_text  # ← new

class Datastore(BaseDatastore):
    DB_PATH = "data/sample-lancedb"
    DB_TABLE_NAME = "rag-table"

    def __init__(self):
        self.vector_dimensions = 768  # ← nomic-embed-text returns 768-dim
        self.vector_db = lancedb.connect(self.DB_PATH)
        self.table: Table = self._get_table()

    def reset(self) -> Table:
        try:
            self.vector_db.drop_table(self.DB_TABLE_NAME)
        except Exception:
            print("Table did not exist. Creating fresh one.")

        schema = pa.schema(
            [
                pa.field("vector", pa.list_(pa.float32(), self.vector_dimensions)),
                pa.field("content", pa.utf8()),
                pa.field("source", pa.utf8()),
            ]
        )
        self.vector_db.create_table(self.DB_TABLE_NAME, schema=schema)
        self.table = self.vector_db.open_table(self.DB_TABLE_NAME)
        print(f"✅ Table created: {self.DB_TABLE_NAME}")
        return self.table

    def get_vector(self, content: str) -> List[float]:
        return embed_text(content)

    def add_items(self, items: List[DataItem]) -> None:
        with ThreadPoolExecutor(max_workers=8) as executor:
            entries = list(executor.map(self._convert_item_to_entry, items))

        self.table.merge_insert("source").when_matched_update_all().when_not_matched_insert_all().execute(entries)

    def search(self, query: str, top_k: int = 5) -> List[str]:
        vector = self.get_vector(query)
        results = (
            self.table.search(vector)
            .select(["content", "source"])
            .limit(top_k)
            .to_list()
        )
        return [r["content"] for r in results]

    def _get_table(self) -> Table:
        try:
            return self.vector_db.open_table(self.DB_TABLE_NAME)
        except Exception:
            return self.reset()

    def _convert_item_to_entry(self, item: DataItem) -> dict:
        return {
            "vector": self.get_vector(item.content),
            "content": item.content,
            "source": item.source,
        }