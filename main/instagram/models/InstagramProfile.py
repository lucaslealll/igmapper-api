class InstagramProfile:
    def __init__(self, id: str, username: str, media_count: int, media: dict):
        self.id = id
        self.username = username
        self.media_count = media_count
        self.media = media

    def __str__(self):
        return f"Instagram Profile of {self.username} (ID: {self.id}) with {self.media_count} posts"
