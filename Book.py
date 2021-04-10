class Book:
    def __init__(self, title, author, length, status):
        self.title = title
        self.author = author
        self.length = length
        self.status = status

    def to_string(self):
        return str(self.title + self.author + self.length + self.status)

    def check_title(self):
        return str(self.title)

    def check_author(self):
        return str(self.author)

    def check_length(self):
        return str(self.length)

    def check_status(self):
        if self.status == "True":
            return True
        else:
            return False


