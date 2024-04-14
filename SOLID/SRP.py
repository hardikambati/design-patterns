"""
    Single Responsibility Principle [SRP]
    -> Every class should only have 1 single responsibility, if a method does not belong to a class, create a new class
"""

class FileManager:

    def __init__(self, name: str):
        self.name = name

    def read(self):
        print('reading file...')

    def write(self):
        print('writing to file...')

    def compress(self):
        print('compressing file...')

    def extract(self):
        print('extracting file data...')


# TO
        

class FileManager:

    def __init__(self, name: str):
        self.name = name

    def read(self):
        print('reading file...')

    def write(self):
        print('writing to file...')


class ZipFileManager:

    def __init__(self, name: str):
        self.name = name

    def compress(self):
        print('compressing file...')

    def extract(self):
        print('extracting file data...')

