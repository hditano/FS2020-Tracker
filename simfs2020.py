from SimConnect import *
from datetime import datetime
import math

class SimFs2020():
    def __init__(self) -> None:
        self.sm = SimConnect()
        self.aq = AircraftRequests(self.sm, _time=2000)
        self.altitude = 0 
        self.speed = 0
        self.title = ''
        self.latlon = []
        self.lat = ''
        self.lon = ''
        self.date = ''
        
    def updateData(self):
        self.altitude = self.SimAltitude()
        self.speed = self.SimSpeed()
        self.title = self.SimTitle()
        self.latlon = self.SimLatLon()
        self.date = self.SimTimestamp()
        print('Data Updated')
        
    def SimTimestamp(self):
       now = datetime.now()
       time = now.strftime("%H:%M:%S")
       return time
   
    def SimAltitude(self):
        altitude = self.aq.get("PLANE_ALTITUDE")
        return round(altitude, 2)
    
    def SimSpeed(self):
        speed = self.aq.get("AIRSPEED_INDICATED")
        return math.trunc(speed)
    
    def SimTitle(self):
        title = self.aq.get("TITLE")
        return title
    
    def SimLatLon(self):
        lat = self.aq.get("PLANE_LATITUDE")
        lon = self.aq.get("PLANE_LONGITUDE")
        latlon = [lat, lon]
        self.lat, self.lon = latlon
        return latlon

    def SimRender(self):
        self.updateData()
        print(self.altitude)
        print(self.title)
        print(self.speed)
        print(self.latlon)
        print(self.date)
        