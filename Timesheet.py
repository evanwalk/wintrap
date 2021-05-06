from datetime import datetime
from os import listdir
import pickle
from hashlib import sha1

class Timeframe():
    def __init__(self, start):
        self.start = start
        self.end = None
        
class Entry():
    def __init__(self, message):
        self.message = message
        self.timeframe = Timeframe(start=datetime.now())
        self.open = True
        self.delta = None
    
    def end(self):
        self.timeframe.end = datetime.now()
        self.open = False
        self.delta = self.timeframe.end - self.timeframe.start

class Timesheet():
    def __init__(self, name):
        self.entries = []
        self.name = name
        self.checked_in = False
        self.current = False
        self.cache()
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<{self.name}>"

    def cache(self):
        value = sha1(self.name.encode()).hexdigest()
        pickle.dump(self, open(f"store/{value}.timesheet", "wb"))

    def checkin(self, message):
        self.entries.append(Entry(message))
        self.checked_in = True
        self.cache()
        
    def checkout(self):
        if self.entries:
            self.entries[-1].end()
        self.checked_in = False
        self.cache()
    
    def switchto(self):
        self.current = True
        self.cache()
    
    def switchaway(self):
        if self.entries[-1].open:
            self.entries[-1].end()
        self.current = False
        self.cache()
    













