class Post:
    def __init__(self, post_id, title, subtitle, body):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
