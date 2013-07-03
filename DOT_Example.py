import DOT
import time


x = DOT.DOT('a98c12a', '58f4671dc98af44434a6f41c4d14a1f')

    #Set / Get Keys
x.setID('a98c12a8')
x.setKey('58f4671dc98af44434a6f41c4d14a1fc')

x.getID()
x.getKey()

x.getTrafficInfo(x.t_WeeklyTraf)
time.sleep(2)
x.getTrafficInfo(x.t_WeekendTraf)
time.sleep(2)
x.getTrafficInfo(x.t_SpecialAlerts)
time.sleep(2)
x.getTrafficInfo(x.t_TrafficSpeed)
time.sleep(2)
#Fetch Construction Info
x.getConstructionInfo(x.c_CWAMPS)
time.sleep(2)
x.getConstructionInfo(x.c_BMPS)
time.sleep(2)
x.getConstructionInfo(x.c_BKMPS)
time.sleep(2)
x.getConstructionInfo(x.c_MMPS)
time.sleep(2)
x.getConstructionInfo(x.c_SIMPS)
time.sleep(2)
x.getConstructionInfo(x.c_CS)
time.sleep(2)
x.getConstructionInfo(x.c_SWMUCIS)
time.sleep(2)
#Fetch Parking Info
x.getParkingInfo(x.p_ParkReminder)
time.sleep(2)
x.getParkingInfo(x.p_Locations)
time.sleep(2)
x.getParkingInfo(x.p_Signs)
time.sleep(2)
#Fetch Truck Info
x.getTruckInfo(x.r_AllRoutes , x.kml)
time.sleep(2)
x.getTruckInfo(x.r_LowBridges , x.kml)
time.sleep(2)
x.getTruckInfo(x.r_ThroughRoutes , x.kml)
time.sleep(2)
x.getTruckInfo(x.r_LocalRoutes , x.kml)
time.sleep(2)
x.getTruckInfo(x.r_AllRoutes , x.zip)
time.sleep(2)
x.getTruckInfo(x.r_LowBridges , x.zip)
time.sleep(2)
x.getTruckInfo(x.r_ThroughRoutes , x.zip)
time.sleep(2)
x.getTruckInfo(x.r_LocalRoutes , x.zip)
time.sleep(2)
#Fetch Bike Info
#kml
x.getBikeInfo(x.b_BikeRacks, x.kml)
time.sleep(2)
x.getBikeInfo(x.b_BikeRoutes, x.kml)
time.sleep(2)
x.getBikeInfo(x.b_BikeShelters, x.kml)
time.sleep(2)
#zip
x.getBikeInfo(x.b_BikeShelters, x.zip)
time.sleep(2)
x.getBikeInfo(x.b_BikeRacks, x.zip)
time.sleep(2)
x.getBikeInfo(x.b_BikeRoutes, x.zip)



    
#print x.r.text <-- Returns the data collected in text format


