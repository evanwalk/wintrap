import pickle
from sys import argv
from os import listdir
from Commands import switch, checkout, checkin, clear_all, SHEETS


def loadSheets():
    global SHEETS
    SHEETS = []
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


COMMANDS = {"switch":   switch,
            "in":       checkin,
            "clear":    clear_all,
            "out":      checkout}

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



if __name__ == '__main__':
    loadSheets()
    args = [x.strip() for x in argv[1:]]
    
    try:
        parse_arg(args[0], args[1:])
    except IndexError:
        import traceback
        print(traceback.format_exc())
        print("Missing argument")
    

    #DEBUG
    loadSheets()
    print("{0:15}| {1:15}| {2:15}| {3}".format("Sheet Name", "Current", "Num Entries", "Last Message"))
    for e in SHEETS:
        print(f"{e.name:15}| {'True' if e.current else 'False':15}| {len(e.entries):15}| {e.entries[-1].message if e.entries else 0}")
    print(e)












