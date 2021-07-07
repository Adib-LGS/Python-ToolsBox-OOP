import threading
import time

from process import MyProcess

th1 = MyProcess()
th1.run()

th1.start()
th1.join()

print('End of thread')