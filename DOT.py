'''
DOT API Library
'''
import requests
class DOT:
    def __init__(self,ID,Key):
        '''
        (Creating Object)

        obj = DOT.DOT('API ID ','API Key')

        obj = DOT.DOT('12345','987654')
        '''
        self.id = ID
        self.key = Key

        self.getID()
        self.getKey()
        #Constants

        #Content Type
        self.kml = 'kml'
        self.zip = 'zip'
        #Traffic
        self.t_WeeklyTraf = 'WeeklyTraf'
        self.t_WeekendTraf = 'WeekendTraff'
        self.t_SpecialAlerts = 'SpecialAlerts'

        #Traffic Advisory
        self.t_TrafficSpeed = 'TrafficSpeed'

        #Construction / Schedules
        self.c_CWAMPS = 'Citywide Arterials Milling Paving Schedule'
        self.c_BMPS = 'Bronx Milling Paving Schedule'
        self.c_BKMPS = 'Brooklyn Milling Paving Schedule'
        self.c_MMPS = 'Manhattan milling & Paving Schedule'
        self.c_SIMPS = 'Staten Island Milling Paving Schedule'
        self.c_CS = 'Concrete Schedule'
        self.c_SWMUCIS = 'Sidewalk Management Unit Construction & Inspection Schedule'

        #Parking Info
        self.p_ParkReminder = 'ParkingRegReminder'
        self.p_Locations = 'locations'
        self.p_Signs = 'signs'

        #Truck Info
        self.r_LowBridges = 'lowbridges_citywide_data_71309'
        self.r_AllRoutes = 'all_truck_routes_nyc'
        self.r_ThroughRoutes = 'through_truck_routes_nyc'
        self.r_LocalRoutes = 'local_truck_routes_nyc'

        #Bike Info
        self.b_BikeRacks = 'dot_cityracks_2012'
        self.b_BikeRoutes = 'nyc_bike_routes'
        self.b_BikeShelters = 'bike_shelters'

        
    def validation(self,statusCode, category):
        '''
        Validates whether the search was successful or not.

        '''
        if statusCode == 403:
            print 'Error Code:403 \n Make sure your APP ID/APP Key are correct'
            print 'APP ID: ', self.id,'  APP Key: ',self.key
    
        elif statusCode == 0:
            print 'Error Code:0 \n Make sure your firewall isn\'t blocking any connections'

        elif statusCode == 403:
            print 'APP Key/ID are correct. The way we are calling the information isn\'t'
            print 'Please report this API to us so we can fix it!'
        elif statusCode == 200:
            return True
        
    def setID(self, newID):
        '''
        (Set a new ID for an object)

        (Example)

        object.setID(12345)
            ==> Assigns a new ID number(12345) to the object
        '''
        self.id = newID
        print self.id

    def setKey(self,newKey):
        '''
        (Set a new key for an object)

        (Example)

        object.setKey(56789)
            ==> Assigns a new key number(56789) to the object
        '''
        self.key = newKey
        print self.key

    def getID(self):
        '''
        (Check to make sure the ID entered for an object was correct)

        (Example)

        object.getID()
            ==> Returns the ID number for object
        '''
        print self.id
        return self.id
    def getKey(self):
        '''
        (Check to make sure the Key entered for an object was correct)

        (Example)

        object.getKey()
            ==> Returns the key for object
        '''
        print self.key
        return self.key

    def getTrafficInfo(self,information):
        '''
        (Search for Specific Traffic Information)

        (Example)
        
        Object.getTrafficInfo(Object.t_WeeklyTraf)
                ==> Searches for "Weekly Traffic" Information


        (Traffic Filters)
        
        self.t_WeeklyTraf
                ==> Search Weekly Traffic
                
        self.t_WeekendTraff
                ==> Search Weekend Traffic
                
        self.t_SpecialAlerts
                ==> Search Special Alerts

        self.t_TrafficSpeed
                ===> Search Traffic Speeds
                
         '''

        print information
        if information == self.t_TrafficSpeed:
            ta = 'traffic-advisory/'
            self.r = requests.get("https://api.cityofnewyork.us/dot/v1/" + ta +
                                  information + '.php' +
                                  "?app_id=" + self.id +
                                  "&app_key=" + self.key)
        else:
            self.r = requests.get("https://api.cityofnewyork.us/dot/v1/"+
                                   information+".xml"+
                                   "?app_id="+self.id+
                                   "&app_key=" +self.key)
        self.sCode = self.r.status_code
        print self.sCode
        self.validator = self.validation(self.sCode , information)
        if  self.validator == True:
            return self.r

    def getConstructionInfo(self,information):
        '''
        (Search for Specific Construction Schedule Information)

        (Example)
        
        Object.getConstructionInfo(Object.c_MMPS)
                ==> Searches for "Manhattan Milling & Paving Schedule"


        (Construction Schedule Filters)
        
        self.c_CWAMPS
                ==> Search 'Citywide Arterials Milling Paving Schedule'
        self.c_BMPS
                ==> Search 'Bronx Milling Paving Schedule'
        self.c_BKMPS
                ==> Search 'Brooklyn Milling Paving Schedule'
        self.c_MMPS
                ==> Search 'Manhattan milling & Paving Schedule'
        self.c_SIMPS
                ==> Search 'Staten Island Milling Paving Schedule'
        self.c_CS
                ==> Search 'Concrete Schedule'
        self.c_SWMUCIS
                ==> Search 'Sidewalk Management Unit Construction &'+
                                'Inspection Schedule'  
                
         '''

        print information
        self.r = requests.get("https://api.cityofnewyork.us/dot/v1/"+
                               information+".xml"+
                               "?app_id="+self.id+
                               "&app_key=" +self.key)
        self.sCode = self.r.status_code
        print self.sCode
        self.validator = self.validation(self.sCode , information)
        if  self.validator == True:
            return self.r

    def getParkingInfo(self,information):
        '''
        (Search for Specific Parking Information)

        (Example)
        Object.getParkingInfo(Object.p_Locations)
                ==> Searches for parking Locations


        (Parking Filters)
        self.p_ParkReminder
                    ==> 'ParkingRegReminder'
        self.p_Locations
                    ==> 'locations'
        self.p_Signs
                    ==> 'signs'
        
         '''
        p = 'parking-reg/'
        
        print information
        if information == self.p_ParkReminder:
            self.r = requests.get("https://api.cityofnewyork.us/dot/v1/"+ p +
                                   information + ".xml" +
                                   "?app_id=" + self.id +
                                   "&app_key=" + self.key)
            
        
        else:
            self.r = requests.get("https://api.cityofnewyork.us/dot/v1/"+ p +
                                   information+ ".csv" +
                                   "?app_id=" + self.id +
                                   "&app_key=" + self.key)
        self.sCode = self.r.status_code
        print self.sCode
        self.validator = self.validation(self.sCode , information)
        if  self.validator == True:
            return self.r


    def getTruckInfo(self,information, contentType):
        '''
        (Search for Truck Information)

        (Example)
        Object.getTruckInfo(Object.r_AllRoutes , Object.kml)
                ==> Searches for all truck routes in NYC

        Content Type choices:
            Object.kml or Object.zip
                                ==> Low Bridge Data only comes in KML format

        (Truck Filters)
        self.r_LowBridges
                ==> Search for low bridges
        self.r_AllRoutes
                ==> Search for all truck routes in NYC
        self.r_ThroughRoutes
                ==> Search for thru truck routes in NYC
        self.r_LocalRoutes
                ==> Search for local truck routes in NYC
        
         '''

        
        ti = 'truck-info/'
        
        print information
        if contentType == self.zip and information != self.r_LowBridges:
            self.r = requests.get("https://api.cityofnewyork.us/dot/v1/"+ ti +
                                   information + ".zip" +
                                   "?app_id=" + self.id +
                                   "&app_key=" + self.key)
        elif contentType == self.zip and information == self.r_LowBridges:
            print 'Low bridge data only comes in KML format'
            self.r = requests.get("https://api.cityofnewyork.us/dot/v1/"+ ti +
                                   information+ ".kml" +
                                   "?app_id=" + self.id +
                                   "&app_key=" + self.key)
            
        
        elif contentType == self.kml:
            self.r = requests.get("https://api.cityofnewyork.us/dot/v1/"+ ti +
                                   information+ ".kml" +
                                   "?app_id=" + self.id +
                                   "&app_key=" + self.key)
        self.sCode = self.r.status_code
        print self.sCode
        self.validator = self.validation(self.sCode , information)
        if  self.validator == True:
            return self.r

    def getBikeInfo(self,information, contentType):
        '''
        (Search for Bike Information)

        (Example)
        Object.getBikeInfo(Object.b_BikeRacks , Object.kml)
                ==> Searches for bike racks in NYC

        Content Type choices:
            Object.kml or Object.zip
                ==> Bicyle Shelters data only comes in KML format!

        (Bike Filters)
        self.b_BikeRacks
                ==> Search for Bike Racks
        self.b_BikeRoutes
                ==> Search for Bike Routes
        self.b_BikeShelters
                ==> Search for Bike Shelters
        
         '''

        
        bi = 'bike-info/'
        
        print information
        if contentType == self.zip and information != self.b_BikeShelters:
            print 'zip'
            self.r = requests.get("https://api.cityofnewyork.us/dot/v1/"+ bi +
                                   information + ".zip" +
                                   "?app_id=" + self.id +
                                   "&app_key=" + self.key)
            
        elif contentType == self.zip and information == self.r_LowBridges:
            print 'Low bridge data only comes in KML format'
            self.r = requests.get("https://api.cityofnewyork.us/dot/v1/"+ bi +
                                   information+ ".kml" +
                                   "?app_id=" + self.id +
                                   "&app_key=" + self.key)
            
        
        elif contentType == self.kml:
            print 'kml'
            self.r = requests.get("https://api.cityofnewyork.us/dot/v1/"+ bi +
                                   information + ".kml" +
                                   "?app_id=" + self.id +
                                   "&app_key=" + self.key)
        self.sCode = self.r.status_code
        print self.sCode
        self.validator = self.validation(self.sCode , information)
        if  self.validator == True:
            return self.r
