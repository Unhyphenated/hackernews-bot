"""
ChromaDB integration for storing article embeddings and summaries.
"""
import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional

class ChromaDBClient:
    def __init__(self, persist_directory: str = "./chroma_db"):
        """Initialize ChromaDB client with persistence."""
        self.client = chromadb.Client(Settings(
            persist_directory=persist_directory,
            chroma_db_impl="duckdb+parquet"
        ))
        self.collection = self.client.get_or_create_collection("articles")
    
    def store_article(
        self,
        article_id: str,
        title: str,
        url: str,
        summary: str,
        metadata: Optional[Dict] = None
    ) -> None:
        """Store article information and summary in ChromaDB."""
        if metadata is None:
            metadata = {}
        
        # Combine article info with provided metadata
        full_metadata = {
            "title": title,
            "url": url,
            **metadata
        }
        
        # Store in ChromaDB
        self.collection.add(
            documents=[summary],
            metadatas=[full_metadata],
            ids=[article_id]
        )
    
    def get_recent_articles(self, limit: int = 3) -> List[Dict]:
        """Retrieve most recent articles."""
        results = self.collection.get(
            limit=limit,
            where={},  # No filtering
        )
        
        articles = []
        for i in range(len(results['ids'])):
            articles.append({
                "id": results['ids'][i],
                "summary": results['documents'][i],
                **results['metadatas'][i]
            })
        
        return articles

if __name__ == "__main__":
    # Test ChromaDB integration
    db = ChromaDBClient()
    db.store_article(
        "test1",
        "Test Article",
        "https://example.com",
        "This is a test summary.",
        {"timestamp": "2023-01-01"}
    )
    recent = db.get_recent_articles()
    print("Recent articles:", recent)
