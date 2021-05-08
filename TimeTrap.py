from TimeSheet import TimeSheet
from hashlib import sha1
from os import listdir
import pickle


class TimeTrap():
    __STORE_PATH__  = "chache"
    __FILE_EXT__    = ".timetrap"

    def __init__(self):
        self.all_sheets: list[TimeSheet] = []
        self.open_sheet: TimeSheet = None

    def __str__(self):
        ret = ""
        for sheet in self.all_sheets:
            ret += str(sheet)
            ret += "\n\n"

        return ret

    @classmethod
    def loadCache(cls):
        try:
            timetrap = pickle.load(open(f"{cls.__STORE_PATH__}{cls.__FILE_EXT__}", "rb"))
            if isinstance(timetrap,TimeTrap):
                return timetrap
            else:
                return cls()
            
        except FileNotFoundError:
            return cls()
    
    def __del__(self):
        pickle.dump(self, open(f"{self.__STORE_PATH__}{self.__FILE_EXT__}","wb"))
    
    def switchto(self, sheet_name):
        found_flag = False
        for sheet in self.all_sheets:
            if sheet.name.lower().strip() == sheet_name.lower().strip():
                self.open_sheet.checkout()
                self.open_sheet = sheet
                found_flag = True
        
        if not found_flag:
            self.all_sheets.append(TimeSheet(sheet_name.lower().strip()))
            self.open_sheet = self.all_sheets[-1]
        

    def checkin(self, message):
        if self.open_sheet is None:
            print("No sheet current selected")
            return
        else:
            self.open_sheet.checkin(message)
    
    def checkout(self):
        if self.open_sheet is None:
            print("No sheet current selected")
            return
        else:
            self.open_sheet.checkout()
        
    








