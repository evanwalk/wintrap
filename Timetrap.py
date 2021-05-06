import pickle
from sys import argv
from sys import exit as BOOM
from os import listdir
from Timesheet import Timesheet

SHEETS:list[Timesheet] = []

def loadSheets():
    for file in listdir("store"):
        if file.endswith(".timesheet"):
            try:
                timesheet = pickle.load(open(f"store/{file}", "rb"))
                timesheet.entries
            except:
                #file format error
                pass
            else:
                SHEETS.append(timesheet)

def switch(timesheet_name):
    name = " ".join(timesheet_name)
    for sheet in SHEETS:
        sheet.checkout()
    
    sheet = Timesheet(name)
    for cached in SHEETS:
        if cached.name == name:
            sheet = cached
    
    sheet.switchto()
    print("Switched to", name)


def checkin(message):
    message = " ".join(message)
    current_sheet = None
    for sheet in SHEETS:
        if sheet.current and current_sheet is None:
            current_sheet = sheet
        elif sheet.current:
            print("Current sheet sync error, not handeled yet")

    if current_sheet is None:
        print("No sheet selected, switch to a sheet")
        BOOM()
    else:
        current_sheet.checkin(message)
        print(f"Checked into \"{current_sheet.name}\", updated with \"{message}\"")


    message = " ".join(message)


COMMANDS = {"switch":   switch,
            "in":       checkin}

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
        v(args[0])
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
        import traceback
        print(traceback.format_exc())
        print("Missing argument")













