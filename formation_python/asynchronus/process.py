import time
import threading

class MyProcess(threading.Thread):

    def __init__(tibidabo):
        threading.Thread.__init__(tibidabo)
    
    # To lock and control specific process during a Thread
    control_thread = threading.RLock()
    
    def run(tibidabo):
        i = 0
        while i < 2:
            with tibidabo.control_thread:
                message = 'I control the order of my thread'
                for i in message:
                    print(i)
                    time.sleep(.5)
            i += 1


    