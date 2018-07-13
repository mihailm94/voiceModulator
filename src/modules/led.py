import sys
sys.path.append('/home/pi/project_nrsss0555407/src/LEDdriver')

import apa102
import time
import threading

try:
    import queue as Queue
except ImportError:
    import Queue as Queue

class Lights:
    PIXELS_N = 3
    
    def __init__(self):
        self.basis = [0] * 3 * self.PIXELS_N
        self.basis[0] = 2
        self.basis[3] = 1
        self.basis[4] = 1
        self.basis[7] = 2

        self.colors = [0] * 3 * self.PIXELS_N
        self.dev = apa102.APA102(num_led=self.PIXELS_N)
        
        self.next = threading.Event()
        self.queue = Queue.Queue()
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()
    
    def wakeup(self, direction=0):
        def f():
                self._wakeup(direction)

        self.next.set()
        self.queue.put(f)

    def _wakeup(self, direction=0):

        for i in range(1, 25):
            colors = [i * v for v in self.basis]

            self.write(colors)
            time.sleep(0.01)

        self.colors = colors

    def _run(self):
        while True:
            func = self.queue.get()
            func()

    def think(self):
        self.next.set()
        self.queue.put(self._think)
    

    def write(self, colors):
        for i in range(self.PIXELS_N):
            self.dev.set_pixel(i, int(colors[3*i]), int(colors[3*i + 1]), int(colors[3*i + 2]))

        self.dev.show()


    def _think(self):
        colors = self.colors

        self.next.clear()
        while not self.next.is_set():
            colors = colors[3:] + colors[:3]
            self.write(colors)
            time.sleep(0.2)

        t = 0.1
        for i in range(0, 5):
            colors = colors[3:] + colors[:3]
            self.write([(v * (4 - i) / 4) for v in colors])
            time.sleep(t)
            t /= 2

        self.colors = colors
   
    def _off(self):
        self.write([0] * 3 * self.PIXELS_N)


    def off(self):
        self.next.set()
        self.queue.put(self._off)

#pixels.wakeup()
#time.sleep(3)
#pixels.off()

'''
if __name__ == '__main__':
    while True:
        try:
            pixels.wakeup()
            time.sleep(3)
            #pixels.think()
            #time.sleep(3)
            pixels.off()
            #time.sleep(3)
        except KeyboardInterrupt:
            break

    #pixels.off()
    #time.sleep(1)
'''    
