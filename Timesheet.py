from datetime import datetime
from os import listdir
import pickle
from hashlib import sha1

class Timeframe():
    def __init__(self, start):
        self.start = start
        self.__end = None
    
    @property
    def duration(self):
        if self.__end is None:
            return datetime.now()-self.start
        else:
            return self.__end-self.start
        
    @property
    def end(self):
        if self.__end is None:
            return datetime.now()
        else:
            return self.__end
    
    @end.setter
    def end(self, value):
        self.__end = value
        
class Entry():
    def __init__(self, message):
        self.message = message
        self.timeframe = Timeframe(start=datetime.now())
        self.open = True
        self.duration = self.timeframe.duration
    
    def end(self):
        self.timeframe.end = datetime.now()
        self.open = False
        self.duration = self.timeframe.end - self.timeframe.start
    

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
            line = "\t{0: <20} {1: <10} {2: <10} {3: <15} {4: <15}\n"
            if last is None or entry.timeframe.start.day != last.timeframe.start.day:
                line = line.format(entry.timeframe.start.strftime("%a %b %m, %Y"), entry.timeframe.start.strftime("%H:%M:%S"),
                            entry.timeframe.end.strftime("%H:%M:%S"), str(entry.duration),
                            entry.message)
            else:
                line = line.format("", entry.timeframe.start.strftime("%H:%M:%S"),
                            entry.timeframe.end.strftime("%H:%M:%S"), str(entry.duration),
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
    













