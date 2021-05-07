from Timesheet import Timesheet
from os import listdir, remove


class Commands():

    def __init__(self):
        self.SHEETS:list[Timesheet] = []

        self.command_map = {"switch":   self.switch,
                            "in":       self.checkin,
                            "clear":    self.clear_all,
                            "out":      self.checkout}

    def get_current_sheet(self):
        current_sheet = None
        for sheet in self.SHEETS:
            print(sheet.name)
            if sheet.current and current_sheet is None:
                current_sheet = sheet
            elif sheet.current:
                print("Current sheet sync error, not handeled yet")
        
        return current_sheet
        

    def switch(self, timesheet_name):
        name = " ".join(timesheet_name)
        for sheet in self.SHEETS:
            sheet.checkout()
            sheet.current = False
            sheet.cache()
        
        sheet = Timesheet(name)
        flag = False
        for cached in self.SHEETS:
            if cached.name == name:
                sheet = cached
                flag = True
        
        if not flag:
            self.SHEETS.append(sheet)

        sheet.switchto()
        print("Switched to", sheet.name)


    def checkin(self, message):
        message = " ".join(message)
        current_sheet = self.get_current_sheet()

        if current_sheet is None:
            print("No sheet selected, switch to a sheet")
        else:
            current_sheet.checkin(message)
            print(f"Checked into \"{current_sheet.name}\", updated with \"{message}\"")

    def checkout(self, args):
        current_sheet = self.get_current_sheet()

        if current_sheet is None:
            print("No sheet selected, switch to a sheet")
        else:
            current_sheet.checkout()


    def clear_all(self, x):
        resp = input("Are you sure you want to clear all sheets? (y/n)")
        if resp.strip().lower() == "y":
            for file in listdir("store"):
                remove(f"store/{file}")