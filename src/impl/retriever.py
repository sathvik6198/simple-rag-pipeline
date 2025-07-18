# src/impl/retriever.py

from typing import List
from interface.base_retriever import BaseRetriever
from interface.base_datastore import BaseDatastore


class Retriever(BaseRetriever):
    def __init__(self, datastore: BaseDatastore):
        self.datastore = datastore

    def search(self, query: str, top_k: int = 5) -> List[str]:
        return self.datastore.search(query, top_k=top_k)