#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time;  # This is required to include time module.
import datetime;  # This is required to include time module.
import WazeRouteCalculator
import unicodedata




from_address='Via a Loma del Rio, Arraijan, Panama'
#to_address='Via Interamericana, Puente de las Americas, Panama'
#from_address = 'Interamericana, Arraijan, Panama'
to_address = 'Puente de las Americas, Panama'

while True:
     try:
         f = open("traffic.txt", "a");
         while True:
             try:
                  time.sleep(10)
                  today = datetime.datetime.today()
                  Registro = str(today) + ',Via a Loma del Rio, Arraijan, Panama, Puente de las Americas, Panama,'
                  
                  route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address)
                  try:
                      route_time,route_distance=route.calc_route_info()
                  except WazeRouteCalculator.WRCError as err:
                      print (err)
                  else:
                      pass
                  #print ('Time %.2f minutes, distance %.2f km. %.f', route_time, route_distance, ticks)
                  Registro = Registro + "%.2f" % route_time + ',' + "%.2f" % route_distance + ','
                  Notification = WazeRouteCalculator.WazeRouteNotification()
                  ticks = time.time()
                  try:
                      rNotification,alerts=Notification.get_notification(ticks)
                  except WazeRouteCalculator.WRCError as err:
                      print (err)
                  else:
                       pass
                  #print "%.2f" % alerts
                  if alerts :
                     for key in rNotification:
                     # print key
                     # print key ['type']
                     # print key ['subtype']
                     # print key ['street']
                     # print key ['nearBy']
                     # print key ['location']['x']
                     # print key ['location']['y']
                         try:
                              if key.get('nearBy'):
                                 nearBy = key['nearBy']
                              else:
                                 nearBy = " " 
                              if key.get('street'):
                                 street = key['street']
                              else:
                                 street = " " 
                              Registro = Registro + key ['type'] + ',' + key ['subtype']  + ',' +   street  + ',' +  nearBy  + ',' + "%.14f" % key ['location']['x']  + ',' + "%.14f" % key ['location']['y'] + ','
                         except TypeError:  
    					       print ('Error TypeError... Alerts Continue')
                  else: 
                        Registro = Registro + ','
             		 
                  try:
                      # if the Registro is a unicode string, normalize it
                      Registro = unicodedata.normalize('NFKD', Registro).encode('ascii','ignore')
                  except TypeError:
                     # if it was not a unicode string => OK, do nothing
                       print ('Error TypeError... unicode Continue')
					   
                  print (Registro)
                  Registro = Registro + '\n'
                  f.write(Registro)
             except IOError:
                  # if it was not a unicode string => OK, do nothing
				    print ('Error IOError... Inner Loop Continue')
             else:
         	        pass
     				
     except IOError:
                  # if it was not a unicode string => OK, do nothing
             print ('Error IOError... Outter loop Continue')
     else:
	         pass