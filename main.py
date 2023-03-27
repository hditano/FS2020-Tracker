from simfs2020 import *
import maprender as map
import time
import traceback

oPlane = SimFs2020()

def every(delay, task):
    next_time = time.time() + delay
    while True:
        time.sleep(max(0, next_time - time.time()))
        try:
            oPlane.SimRender()
            map.Marker(oPlane.SimLatLon())
        except Exception:
            traceback.print_exc()
        next_time += (time.time() - next_time) // delay * delay + delay


if __name__ == '__main__':
    print('Starting Data...')
    every(5, oPlane.SimRender())
