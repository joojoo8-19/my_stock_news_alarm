import requests
import os
from dotenv import load_dotenv
from data.article_model import ArticleModel

END_POINT = "https://newsapi.org/v2/everything"

class NewsManager:
    def __init__(self):
        load_dotenv()
        self.end_point = END_POINT
        self.default_queries = {
            "apiKey": os.environ.get("NEWS_API"),
            "page":1,
            "pageSize": 5,
        }

    def fetch_news(self, q) -> list[ArticleModel]:
        self.default_queries["q"] = q
        response = requests.get(url=self.end_point, params=self.default_queries)
        response.raise_for_status()
        data = response.json()["articles"]
        articles = []

        for article in data:
            articles.append(ArticleModel(
                author=article["author"],
                title=article["title"],
                description=article["description"],
                url=article["url"],
                published_at=article["publishedAt"]
            ))

        return articles