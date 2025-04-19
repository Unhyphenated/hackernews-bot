"""
HackerNews API client for fetching top stories.
"""
import requests
from typing import List, Dict

class HackerNewsAPI:
    BASE_URL = "https://hacker-news.firebaseio.com/v0"
    
    @staticmethod
    def get_top_stories(limit: int = 3) -> List[Dict]:
        """Fetch top stories from HackerNews."""
        # Get top story IDs
        response = requests.get(f"{HackerNewsAPI.BASE_URL}/topstories.json")
        story_ids = response.json()[:limit]
        
        # Fetch each story's details
        stories = []
        for story_id in story_ids:
            story = requests.get(f"{HackerNewsAPI.BASE_URL}/item/{story_id}.json").json()
            stories.append(story)
            
        return stories

if __name__ == "__main__":
    # Test the API
    hn_api = HackerNewsAPI()
    top_stories = hn_api.get_top_stories()
    for story in top_stories:
        print(f"Title: {story.get('title')}")
        print(f"URL: {story.get('url')}")
        print("---")
