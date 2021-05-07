from datetime import datetime
from os import listdir
import pickle
from hashlib import sha1

class Timeframe():
    def __init__(self, start):
        self.start = start
        self.end = None
    
    @property
    def duration(self):
        if self.end is None:
            return datetime.now()-self.start
        else:
            return self.end-self.start
        
class Entry():
    def __init__(self, message):
        self.message = message
        self.timeframe = Timeframe(start=datetime.now())
        self.open = True
        self.delta = self.timeframe.duration
    
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
        ret = f"Timesheet: {self.name}\n"
        last = None
        for entry in self.entries:
            #       day     start   end     duration    notes
            line = "\t{0:15} {1:15}-{2:15} {3:15} {4:15}\n"
            if last is None or entry.timeframe.start.day != last.timeframe.start.day:
                line.format(entry.timeframe.start.strftime("%a %b %m, %Y"), entry.timeframe.start.strftime("%H:%M:%S"),
                            entry.end.strftime("%H:%M:%S"), (entry.duration.strftime("%H:%M:%S")),
                            entry.message)
            else:
                line.format("", entry.timeframe.start.strftime("%H:%M:%S"),
                            entry.end.strftime("%H:%M:%S"), (entry.duration.strftime("%H:%M:%S")),
                            entry.message)
            last = entry
            ret += line
        return ret
            


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
    













