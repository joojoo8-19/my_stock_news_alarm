class ArticleModel:
    def __init__(self, author:str, title:str, description:str, url:str, published_at: str):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.published_at = published_at

    def to_dict(self):
        return {
            "author":self.author,
            "title":self.title,
            "description":self.description,
            "url":self.url,
            "published_at": self.published_at
        }

