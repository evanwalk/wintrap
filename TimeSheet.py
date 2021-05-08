from Entry import Entry
from datetime import timedelta

class TimeSheet():
    def __init__(self, name:str):
        self.name:str = name
        self.entries:list[Entry] = []

    def __eq__(self, other):
        if isinstance(other, TimeSheet):
            if other.name == self.name:
                return True
        return False
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        ret = "Timesheet: " + self.name + "\n"
        last = None
        ret += "   {0:17}  {1:10}{2:10}{3:10}   {4}\n".format("Day", 
                                                            "Start", 
                                                            "End",
                                                            "Duration",
                                                            "Message")
        for entry in self.entries: 
            line = "   {0:17}  {1:10}{2:10}{3:10}   {4}"
            if last is None or last.start.day != entry.start.day:
                line = line.format(entry.start.strftime("%a %b %m, %Y"),
                                    entry.start.strftime("%H:%M:%S"),
                                    entry.end.strftime("%H:%M:%S"),
                                    self.delta_format(entry.delta),
                                    entry.message)
            else:
                line = line.format("",
                                    entry.start.strftime("%H:%M:%S"),
                                    entry.end.strftime("%H:%M:%S"),
                                    self.delta_format(entry.delta),
                                    entry.message)
            ret += line + "\n"
        return ret

    def checkin(self, message):
        if len(self.entries) > 0:
            if self.entries[-1].open():
                self.entries[-1].close()

        self.entries.append(Entry(message))
    
    def checkout(self):
        if len(self.entries) > 0:
            self.entries[-1].close()
    
    def delta_format(self, delta):
        if isinstance(delta, timedelta):
            seconds = delta.total_seconds()
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            val = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
            if val == "00:00:00":
                return "--:--:--"
            else:
                return val

    

