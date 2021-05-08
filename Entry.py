from datetime import datetime 


class Entry():
    def __init__(self, message:str):
        self.message:str = message
        self.start = datetime.now()
        self.__end = None

    def open(self):
        return True if self.__end is None else False

    @property
    def end(self):
        if self.__end is None:
            return datetime.now()
        else:
            return self.__end
    
    @property
    def delta(self):
        return self.end - self.start

    def close(self):
        self.__end = datetime.now()
