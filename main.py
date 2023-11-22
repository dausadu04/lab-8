import requests


class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed
        self.url = "https://jsonplaceholder.typicode.com/todos/"

    def response(self):
        response = requests.get(self.url)
        data = [self.url, paramt]
    def __str__(self):
        return print(self.userId)