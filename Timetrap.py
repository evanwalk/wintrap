import pickle
from sys import argv
from sys import exit as BOOM
from os import listdir
from Timesheet import Timesheet

SHEETS:list[Timesheet] = []

CURRENT_SHEET:Timesheet = None

def loadSheets():
    for file in listdir("store"):
        if file.endswith(".TIMESHEET"):
            try:
                timesheet = pickle.load(open(file, "rb"))
                timesheet.entries
            except:
                #file format error
                pass
            else:
                SHEETS.append(timesheet)

def switch(timesheet_name):
    name = " ".join(timesheet_name)
    if CURRENT_SHEET is not None:
        CURRENT_SHEET.checkout()
        sheet = Timesheet(name)
        for cached in SHEETS:
            if cached.name == name:
                sheet = cached
                break
        CURRENT_SHEET = sheet
    else:
        sheet = Timesheet(name)
        CURRENT_SHEET = sheet
    
    CURRENT_SHEET.switchto()
    print("Switched to", name)

def checkin(message):
    message = " ".join(message)


COMMANDS = {"switch":switch}

def parse_arg(arg, *args):
    count = 0
    v = None
    matches = []
    for key, val in COMMANDS.items():
        if key.lower().startswith(arg.lower()):
            count += 1
            v = val
            matches.append(key)
    if count == 1:
        #command found
        v(args)
    else:
        #no command found
        if count != 0:
            print(f"Unknown command {arg.lower()}")
            print()
            print(f"\tDid you mean one of these?")
            for m in matches:
                print(f"\t\t{m}")
            print()
        else:
            print('No command matches arguments given')
        BOOM()


if __name__ == '__main__':
    loadSheets()
    args = [x.strip() for x in argv[1:]]
    
    try:
        parse_arg(args[0], args[1:])
    except IndexError:
        print("Missing argument")













