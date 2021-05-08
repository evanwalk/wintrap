from TimeTrap import TimeTrap
from sys import argv
import pickle


if __name__ == '__main__':
    trap = TimeTrap.loadCache()
    args = argv[1:]
    
    if "switch".startswith(args[0]):
        trap.switchto(" ".join(args[1:]))
    elif "in".startswith(args[0]):
        trap.checkin(" ".join(args[1:]))
    elif "out".startswith(args[0]):
        trap.checkout()
    
    print(trap)


