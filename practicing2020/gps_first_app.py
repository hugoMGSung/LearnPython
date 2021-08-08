from gps import *
import time

running = True

def getPositionData(gps):
    nx = gpsd.next()

    if nx['class'] == 'TPV':
        latitude = getattr(nx, 'lat', 'Unknown')
        longitude = getattr(nx, 'lon', 'Unknown')
        print('Your position: lon={}, lat={}'.format(str(longitude), str(latitude)))

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

if __name__ == '__main__':
    try:
        print('Application started!')
        while running:
            getPositionData(gpsd)
            time.sleep(1.0)
    except KeyboardInterrupt:
        running = False
        print('Application closed!')