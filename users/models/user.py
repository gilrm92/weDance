import uuid
from pydantic import Field


class User:
    def __init__(self, name, login, password):
        self._id = str(uuid.uuid4())
        self.name = name
        self.login = login
        self.password = password