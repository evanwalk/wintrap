from datetime import datetime
from os import listdir
import pickle

class Timeframe():
    def __init__(self, start):
        self.start = start
        self.end = None
        
class Entry():
    def __init__(self, message):
        self.message = message
        self.timeframe = Timeframe(start=datetime.Now())
        self.open = True
        self.delta = None
    
    def end(self):
        self.timeframe.end = datetime.Now()
        self.open = False
        self.delta = self.timeframe.end - self.timeframe.start

class Timesheet():
    def __init__(self, name):
        self.entries = []
        self.name = name
        self.checked_in = False
        self.current = False
        self.cache_self()
    
    def cache_self(self):
        pickle.dump(self, open(f"store/{str(hash(self.name))}"))

    def checkin(self, message):
        self.entries.append(Entry(message))
        self.checked_in = True
        self.cache_self()
        
    def checkout(self):
        self.entries[-1].end()
        self.checked_in = False
        self.cache_self()
    
    def switchto(self):
        self.current = True
    
    def switchaway(self):
        self.current = False












