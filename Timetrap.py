import pickle
from sys import argv
from os import listdir
from Commands import Commands


def loadSheets():
    sheets = []
    for file in listdir("store"):
        if file.endswith(".timesheet"):
            try:
                timesheet = pickle.load(open(f"store/{file}", "rb"))
                timesheet.entries
            except:
                #file format error
                pass
            else:
                sheets.append(timesheet)
    return sheets

cmd = Commands()

COMMANDS = {"switch":   cmd.switch,
            "in":       cmd.checkin,
            "clear":    cmd.clear_all,
            "out":      cmd.checkout}

def parse_arg(arg, *args):
    count = 0
    v = None
    matches = []
    for key, val in cmd.command_map.items():
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
    
    cmd.SHEETS = loadSheets()
    args = [x.strip() for x in argv[1:]]
    
    try:
        parse_arg(args[0], args[1:])
    except IndexError:
        import traceback
        print(traceback.format_exc())
        print("Missing argument")
    

    #DEBUG
    print("{0:15}| {1:15}| {2:15}| {3}".format("Sheet Name", "Current", "Num Entries", "Last Message"))
    for e in cmd.SHEETS:
        print(e)
        print("\n")












