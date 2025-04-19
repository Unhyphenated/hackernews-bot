"""
Article summarization using LangChain and GPT-3.5-turbo.
"""
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
import requests
from typing import Optional

class ArticleSummarizer:
    def __init__(self, openai_api_key: str):
        """Initialize the summarizer with OpenAI API key."""
        self.llm = OpenAI(
            temperature=0.5,
            model_name="gpt-3.5-turbo",
            openai_api_key=openai_api_key
        )
        self.chain = load_summarize_chain(self.llm, chain_type="stuff")
    
    def fetch_article_content(self, url: str) -> Optional[str]:
        """Fetch article content from URL."""
        try:
            response = requests.get(url)
            return response.text
        except Exception as e:
            print(f"Error fetching article: {e}")
            return None
    
    def summarize_article(self, content: str) -> str:
        """Generate a summary of the article content."""
        try:
            doc = Document(page_content=content)
            summary = self.chain.run([doc])
            return summary
        except Exception as e:
            print(f"Error generating summary: {e}")
            return ""

if __name__ == "__main__":
    # Test summarization
    import os
    summarizer = ArticleSummarizer(os.getenv("OPENAI_API_KEY"))
    test_content = """
    This is a test article content.
    It contains multiple paragraphs of information.
    The summarizer should create a concise summary.
    """
    summary = summarizer.summarize_article(test_content)
    print(f"Summary: {summary}")
