from Entry import Entry

class TimeSheet():
    def __init__(self, name:str):
        self.name:str = name
        self.entries:list[Entry] = []

