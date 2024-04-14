"""
    5. Dependency Inversion Principle [DIP]
    -> High level modules(derieved class) should not be dependent on low level modules(base class), they both should be dependent on ABSTRACTIONS
    -> Abstraction should not depend on details, details should depend on abstractions

    (classes should not be tightly coupled)
"""


class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.fetch_from_database()
        return data
    

class BackEnd:
    def fetch_from_database(self):
        return '[database] data'
    

# TO
    
from abc import ABC, abstractmethod


class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        return data
    

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return '[database] data'
    

class API(DataSource):
    def get_data(self):
        return '[api] data'


api = API()
db = Database()

fe = FrontEnd(data_source=db).display_data()
print(fe)
