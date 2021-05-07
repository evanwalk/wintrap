from Timesheet import Timesheet
from os import listdir, remove
from Timesheet import Timesheet


SHEETS:list[Timesheet] = []

def get_current_sheet():
    current_sheet = None
    for sheet in SHEETS:
        if sheet.current and current_sheet is None:
            current_sheet = sheet
        elif sheet.current:
            print("Current sheet sync error, not handeled yet")
    
    return current_sheet
    



def switch(timesheet_name):
    name = " ".join(timesheet_name)
    for sheet in SHEETS:
        sheet.checkout()
        sheet.current = False
        sheet.cache()
    
    sheet = Timesheet(name)
    for cached in SHEETS:
        if cached.name == name:
            sheet = cached
    
    sheet.switchto()
    print("Switched to", sheet.name)


def checkin(message):
    message = " ".join(message)
    current_sheet = get_current_sheet()

    if current_sheet is None:
        print("No sheet selected, switch to a sheet")
    else:
        current_sheet.checkin(message)
        print(f"Checked into \"{current_sheet.name}\", updated with \"{message}\"")

def checkout(args):
    current_sheet = get_current_sheet()

    if current_sheet is None:
        print("No sheet selected, switch to a sheet")
    else:
        current_sheet.checkout()


def clear_all(x):
    resp = input("Are you sure you want to clear all sheets? (y/n)")
    if resp.strip().lower() == "y":
        for file in listdir("store"):
            remove(f"store/{file}")