from ast import Continue
import datetime
import time
t = time.localtime()
current_time = time.strftime("%H:%M", t)    #For printing current time

while True:     
      print("-"*60)
      print(" "*25,"LOGIN"," "*27)          #Header
      print("-"*60)
      print("TIME:",current_time)
      print()
      usernm=input("Enter Username:").lower()
      paswd=input("Enter Password :")
      print()
      if paswd=="1234" and usernm=="admin":                                                #Starting loop
            import mysql.connector as c
            con=c.connect(host="localhost",                         #Connection with the database
                        user="root",
                        passwd="1234",
                        database="tourism")
            cursor=con.cursor()

            print("*"*60)
            print("-"*60)
            print(" "*20,"TOURISM MANAGEMENT SYSTEM"," "*27)          #Header
            print("-"*60)
            print("*"*60)
            print()
            print()
            print("*"*60)
            print()
            while True:
                  print()
                  print(" "*25,"Home Page"," "*27)          #Header
                  print(" "*25,"-"*9," "*27)
                  print()
                  print("Select your choice:")                     #Menu to select a choice
                  print()
                  print('''
                  1.Driver record
                  2.Vehicle record
                  3.Tour Packages
                  4.Booking record
                  5.Transaction record
                  6.Sign out''')
                  print()
                  ch=int(input("Enter your choice:"))
                  print()
                  if ch==1:                                         #Driver records
                        print("*"*60)
                        print("-"*60)
                        print(" "*25,"DRIVER DATA"," "*27)
                        print("-"*60)
                        print("*"*60)
                        while True:
                              print()
                              print("Choose your choice:")
                              print()                                       #Menu of drivers
                              print('''                                   
                              1.Add a new driver's record.
                              2.Show all driver's record.
                              3.Search a driver's record.
                              4.Delete a driver's record.
                              5.Update a driver's record
                              6.return to Home Page''')
                              print()

                              op1=int(input("Enter your choice:"))
                              print()


                              if op1==1:                              #Adding a new driver's record
                                    while True:
                                          try:
                                                dr_id=int(input("Enter the driver id:"))
                                                dr_name=input("Enter the driver's name:")
                                                dr_aadhar=int(input("Enter the driver's aadhar number:"))
                                                dr_add=input("Enter the driver's address:")
                                                dr_ph=int(input("Enter the driver's phone number:"))
                                                dr_status=input("Enter the driver's status:")
                                                query="insert into driver(Driver_id,Driver_name,Aadhar_number,Address,Phone,status)values({},'{}',{},'{}',{},'{}')".format(dr_id,dr_name,dr_aadhar,dr_add,dr_ph,dr_status)
                                                cursor.execute(query)
                                                con.commit()
                                                print()
                                                print("Data added successfully")
                                                print()
                                                
                                          except :
                                                print()
                                                print("Driver ID already exist")
                                                print()
                                          ch=input("do you want to add another driver's record? (Y/N):").lower()
                                          print()
                                          if ch=="y":
                                                continue
                                          else:
                                                break

                              elif op1==2:                         #Displaying existing records
                                    header='{:<15}{:<15}{:<15} {:<15}{:<15}{:<15}'.format('Driver_id','Driver_name','Aadhar_number','Address','Phone','status')
                                    print(header)
                                    print("-"*83)
                                    print()
                                    cursor.execute("select * from driver")
                                    record=cursor.fetchall()
                                    for i in record:        
                                          print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
                                    print()
                                    print("Total records of Drivers:",cursor.rowcount)

                              elif op1==3:                       #Searching a driver's record
                                    header='{:<15}{:<15}{:<15} {:<15}{:<15}{:<15}'.format('Driver_id','Driver_name','Aadhar_number','Address','Phone','status')        
                                    serid=int(input("Enter the ID of the driver to be searched:"))
                                    print()
                                    cursor.execute("select Driver_id from driver")
                                    r=cursor.fetchall()
                                    c=0
                                    
                                    for i in range(len(r)):
                                                if r[i][0] ==serid :
                                                      cursor.execute("SELECT * FROM driver WHERE Driver_id=%s", (serid,))
                                                      record=cursor.fetchall()
                                                      for i in record:
                                                            print(header)
                                                            print("-"*83)
                                                            print()
                                                            print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
                                                else:
                                                  c+=1
                                    if c==len(r):
                                          print("Driver ID does not exist")       
                                    
      
                              elif op1==4:                       #Deleting a driver's record
                                    delid=int(input("Enter the ID of the driver to be deleted:")) 
                                    print()
                                    cursor.execute("select Driver_id from driver")
                                    r=cursor.fetchall()
                                    c=0                              
                                    for i in range(len(r)):
                                                if r[i][0] ==delid :
                                                      cursor.execute("DELETE FROM driver WHERE Driver_id=%s", (delid,))
                                                      con.commit()
                                                      print("Deleted successfully!!")
                                                else:
                                                  c+=1
                                    if c==len(r):
                                          print("Driver ID does not exist")   


                              elif op1==5:                   #Updating a driver's record
                                    drid=int(input("Enter the ID of the driver to be updated:"))
                                    while True:                                   
                                          print()
                                          cursor.execute("select Driver_id from driver")
                                          record=cursor.fetchall()
                                          c=0
                                          
                                          for i in range(len(record)):
                                                if record[i][0] ==drid :
                                                      
                                                            up1=int(input('''
                                                            What do you want to update?:
                                                            
                                                            1.Driver_name
                                                            2.Aadhar_number
                                                            3.Address
                                                            4.Phone
                                                            5.Status
                                                            6.return

                                                            Enter your choice:'''))
                                                            if up1==1:
                                                                  upname=input("Enter the updated name:")
                                                                  cursor.execute("UPDATE driver SET Driver_name=%s WHERE Driver_id=%s",(upname,drid))
                                                                  con.commit()
                                                                  print()
                                                                  print("Updated successfully!!")
                                                                  print()

                                                            elif up1==2:
                                                                  upadno=int(input("Enter the updated Aadhar number:"))
                                                                  cursor.execute("UPDATE driver SET Aadhar_number=%s WHERE Driver_id=%s",(upadno,drid))
                                                                  con.commit()
                                                                  print()
                                                                  print("Updated successfully!!")
                                                                  print()

                                                            elif up1==3:
                                                                  upadd=input("Enter the updated Address:")
                                                                  cursor.execute("UPDATE driver SET Address=%s WHERE Driver_id=%s",(upadd,drid))
                                                                  con.commit()
                                                                  print()
                                                                  print("Updated successfully!!")
                                                                  print()

                                                            elif up1==4:
                                                                  upphno=int(input("Enter the updated Phone number:"))
                                                                  cursor.execute("UPDATE driver SET Phone=%s WHERE Driver_id=%s",(upphno,drid))
                                                                  con.commit()
                                                                  print()
                                                                  print("Updated successfully!!")
                                                                  print()

                                                            elif up1==5:
                                                                  upstat=input("Enter the updated Status:")
                                                                  cursor.execute("UPDATE driver SET status=%s WHERE Driver_id=%s",(upstat,drid))
                                                                  con.commit()
                                                                  print()
                                                                  print("Updated successfully!!")
                                                                  print()
                                                            
                                                            elif up1==6:
                                                                  break
                                                            else:
                                                                  print("Invalid Input")
                                                else:
                                                      c+=1
                                          if c==len(record):
                                                print("Driver ID does not exist.")
                                                print()
                                          ch=input("Do you want to update any other data?(Y/N)").lower()
                                          if ch=="y":
                                                continue
                                          else:
                                                break
                                                                                                
                              elif op1==6:       # to go back to the main menu
                                    break
                              print()                        
                              ch=input("Do tou want to continue in Driver database? (Y/N):").lower()
                              if ch=="y":
                                    continue
                              else:
                                    break

                  if ch==2:                    #Vehicle records
                        print("*"*60)
                        print("-"*60)
                        print(" "*25,"VEHICLE DATA"," "*27)
                        print("-"*60)
                        print("*"*60)
                        while True:
                              print()
                              print("Choose your choice:")            #Menu of vehicles
                              print()
                              print('''
                              1.Add a new Vehicle's record.
                              2.Show all vehicle's record.
                              3.Search a vehicle's record.
                              4.Delete a vehicle's record.
                              5.Update a vehicle's record
                              6.return to Home Page''')
                              print()

                              op1=int(input("Enter your choice:"))
                              print()


                              if op1==1:                        #Adding a new vehicle's records
                                    while True:
                                          try:
                                                print()
                                                vid=int(input("Enter the Vehicle id:"))
                                                name=input("Enter the Vehicle name:")
                                                r=float(input("Enter the rent of the vehicle:"))
                                                ft=input("Enter the fuel type of the vehicle:")
                                                avg=int(input("Enter the Average mileage:"))
                                                stat=input("Enter the Vehicle's status:")
                                                query="insert into vehicles(vehicle_id,vehicle_name,rent,fuel_type,Average,status)values({},'{}',{},'{}',{},'{}')".format(vid,name,r,ft,avg,stat)
                                                cursor.execute(query)
                                                con.commit()
                                                print()
                                                print("Data added successfully")
                                                print()
                                          except :
                                                print("Vehicle ID already exist")
                                                
                                          ch=input("do you want to add another vehicle's record? (Y/N):").lower()
                                          if ch=="y":
                                                continue
                                          else:
                                                break

                              elif op1==2:                  #Displaying vehicle's records
                                    header='{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format('vehicle_id','vehicle_name','rent','fuel_type','Average mileage','status')
                                    print(header)
                                    print("-"*120)
                                    print()
                                    cursor.execute("select * from vehicles")
                                    record=cursor.fetchall()
                                    for i in record:        
                                          print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
                                    print()
                                    print("Total numbers of records=",cursor.rowcount)

                              elif op1==3:              #Searching a vehicle's records
                                    header='{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format('vehicle_id','vehicle_name','rent','fuel_type','Average','status')       
                                    serid=int(input("Enter the ID of the vehicle to be searched:"))
                                    print()
                                    cursor.execute("select vehicle_id from vehicles")
                                    r=cursor.fetchall()
                                    c=0
                                    
                                    for i in range(len(r)):
                                                if r[i][0] ==serid :
                                                      cursor.execute("SELECT * FROM vehicles WHERE vehicle_id=%s", (serid,))
                                                      record=cursor.fetchall()
                                                      for i in record:
                                                            print(header)
                                                            print("-"*120)
                                                            print()                                                      
                                                            print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
                                                else:
                                                      c+=1
                                    if c==len(r):
                                          print("Vehicle ID not found")

                              elif op1==4:                  #Deleting a vehicle's records
                                    delid=int(input("Enter the ID of the vehicle to be deleted:"))
                                    print()
                                    cursor.execute("select vehicle_id from vehicles")
                                    r=cursor.fetchall()
                                    c=0
                                    
                                    for i in range(len(r)):
                                                if r[i][0] ==delid:
                                                      cursor.execute("DELETE FROM vehicles WHERE vehicle_id=%s", (delid,))
                                                      con.commit()
                                                      print("Deleted successfully!!")
                                                else:
                                                      c+=1
                                    if c==len(r):
                                          print("Vehicle ID not found!!")


                              elif op1==5:                 #Updating a vehicle's record
                                    vid=int(input("Enter the ID of the vehicle to be updated:"))
                                    print()
                                    cursor.execute("select vehicle_id from vehicles")
                                    record=cursor.fetchall()
                                    c=0
                                    
                                    for i in range(len(record)):
                                          if record[i][0] ==vid :
                                                
                                                      up1=int(input('''
                                                      What do you want to update?:
                                                      
                                                      1.vehicle_name
                                                      2.rent
                                                      3.fuel_type
                                                      4.Average mileage
                                                      5.status
                                                      6.Return

                                                      Enter your choice:'''))
                                                      if up1==1:
                                                            upname=input("Enter the updated name:")
                                                            cursor.execute("UPDATE vehicles SET vehicle_name=%s WHERE vehicle_id=%s",(upname,vid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()

                                                      elif up1==2:
                                                            uprent=float(input("Enter the updated Rent:"))
                                                            cursor.execute("UPDATE vehicles SET rent=%s WHERE vehicle_id=%s",(uprent,vid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()

                                                      elif up1==3:
                                                            upft=input("Enter the updated Fueltype:")
                                                            cursor.execute("UPDATE vehicles SET fuel_type=%s WHERE vehicle_id=%s",(upft,vid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()

                                                      elif up1==4:
                                                            upavg=int(input("Enter the updated Average milage:"))
                                                            cursor.execute("UPDATE vehicles SET Average=%s WHERE vehicle_id=%s",(upavg,vid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()

                                                      elif up1==5:
                                                            upstat=input("Enter the updated Status:")
                                                            cursor.execute("UPDATE vehicles SET status=%s WHERE vehicle_id=%s",(upstat,vid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()

                                                      elif up1==6:
                                                            break
                                                      else:
                                                            print("Invalid Input")
                                          else:
                                                c+=1
                                    if c==len(record):
                                          print("Vehicle ID does not exist.")
                                    
                              elif op1==6:            #To go back to the main menu
                                    break                                
                              print()
                              ch=input("Do tou want to continue in Vehicle database? (Y/N):").lower()
                              if ch=="y":
                                    continue
                              else:
                                    break
                  
                  elif ch==3:                         #Tour packages
                        print("*"*60)
                        print("-"*60)
                        print(" "*23,"Tour Packages"," "*27)
                        print("-"*60)
                        print("*"*60)
                        print()
                        while True:                              #Menu of tour packages
                              print('''
                                    1.Add a new Tour package.
                                    2.Show all Tour packages.
                                    3.Search a Tour package.
                                    4.Delete a Tour Package.
                                    5.Update a Tour package.
                                    6.Return to Home Page''')
                              print()
                              op3=int(input("Enter your choice:"))

                              if op3==1:                            #Adding a new tour packages
                                    while True:

                                          try:
                                                pk_id=int(input("Enter the Tour package id:"))
                                                destinations=input("Enter the destinations:")
                                                du=int(input("Enter the Tour duration:"))
                                                cost=float(input("Enter the Tour cost:"))
                                                query="insert into pakages(pakage_id,destinations,duration,cost)values({},'{}',{},{})".format(pk_id,destinations,du,cost)
                                                cursor.execute(query)
                                                con.commit()
                                                print()
                                                print("Data added successfully")
                                                print()
                                                ch=input("do you want to add another Tour Package? (Y/N):").lower()
                                                if ch=="y":
                                                   continue
                                                else:
                                                   break
                                          except :
                                                print()
                                                print("Package ID already exist")
                                                print()
                                          ch=input("do you want to add another Tour Package? (Y/N):").lower()
                                          if ch=="y":
                                                continue
                                          else:
                                                break
                              elif op3==2:                  #Displaying the tour packages
                                    print()
                                    header='{:<15}{:<45}{:<25}{:<25}'.format('Package ID','Destinations','Durations','cost')
                                    print(header)
                                    print("-"*100)
                                    print()
                                    cursor.execute("select * from pakages")
                                    record=cursor.fetchall()
                                    for i in record:        
                                          print("{:<15}{:<45}{:<25}{:<25}".format(i[0],i[1],i[2],i[3]))
                                    print()

                              elif op3==3:                #Searching a tour package
                                    header='{:<15}{:<45}{:<25}{:<25}'.format('Package ID','Destinations','Durations','cost')
                                    serid=int(input("Enter the ID of the Tour package to be searched:"))
                                    print()
                                    cursor.execute("select pakage_id from pakages")
                                    r=cursor.fetchall()
                                    c=0
                                    
                                    for i in range(len(r)):
                                                if r[i][0] ==serid :
                                                      cursor.execute("SELECT * FROM pakages WHERE pakage_id=%s", (serid,))
                                                      record=cursor.fetchall()
                                                      for i in record:
                                                            print(header)
                                                            print("-"*140)
                                                            print()
                                                            
                                                            print("{:<25}{:<25}{:<25}{:<25}{:<25}{:<25}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
                                                else:
                                                      c+=1
                                    if c==len(r):
                                          print("Package ID not found")

                              
                              
                              elif op3==4:                   #Deleting a tour package
                                          delid=int(input("Enter the ID of the Package to be deleted:"))
                                          print()
                                          cursor.execute("select pakage_id from pakages")
                                          r=cursor.fetchall()
                                          c=0
                                          
                                          for i in range(len(r)):
                                                      if r[i][0] ==delid:
                                                            cursor.execute("DELETE FROM pakages WHERE pakage_id=%s", (delid,))
                                                            con.commit()
                                                            print("Deleted successfully!!")
                                                      else:
                                                            c+=1
                                          if c==len(r):
                                                print("Package ID not found!!")

                              elif op3==5:                     #Updating a tour package
                                    pkid=int(input("Enter the ID of the Package to be updated:"))
                                    print()
                                    cursor.execute("select pakage_id from pakages")
                                    record=cursor.fetchall()
                                    c=0
                                    
                                    for i in range(len(record)):
                                          if record[i][0] ==pkid :
                                                
                                                      up1=int(input('''
                                                      What do you want to update?:
                                                      
                                                      1.Destinations
                                                      2.duration
                                                      3.cost
                                                      4.Return

                                                      Enter your choice:'''))
                                                      if up1==1:
                                                            updest=input("Enter the updated destinations:")
                                                            cursor.execute("UPDATE pakages SET destinations=%s WHERE pakage_id=%s",(updest,pkid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()
                                                      elif up1==2:
                                                            updur=float(input("Enter the updated duration:"))
                                                            cursor.execute("UPDATE pakages SET duration=%s WHERE pakage_id=%s",(updur,pkid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()

                                                      elif up1==3:
                                                            upcost=input("Enter the updated cost:")
                                                            cursor.execute("UPDATE pakages SET cost=%s WHERE pakage_id=%s",(upcost,pkid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()
                                                
                                                      elif up1==4:
                                                            break
                                                      else:
                                                            print()
                                                            print("Invalid Input")
                                          else:
                                                c+=1
                                    if c==len(record):
                                          print("Package ID does not exist.")


                              else:
                                    print()
                                    print("Invalid input")
                                    break
                              print()
                              ch=input("Do tou want to continue in Package database? (Y/N):").lower()        #Choice to continue using the tour packages
                              if ch=="y":
                                    continue
                              else:
                                    break
                  
                  elif ch==4:                          #Bookings
                        print("*"*60)
                        print("-"*60)
                        print(" "*25,"BOOKINGS"," "*27)
                        print("-"*60)
                        print("*"*60)
                        while True:
                              print()
                              print("Choose your choice:")              #Menu of Bookings
                              print()
                              print('''
                              1.New booking
                              2.Show bookings
                              3.Search a booking
                              4.Delete a booking
                              5.Update a booking
                              6.Return to Home Page''')
                              op2=int(input("Enter your choice:"))
                              print()
                              if op2==1:                          #Adding a new booking
                                    while True:
                                      try:
                                          print("VEHICLES AVAILABLE:")
                                          print("-"*21)    
                                          print()
                                          header='{:<25}{:<25}{:<25}{:<25}{:<25}{:<25}'.format('vehicle_id','vehicle_name','rent','fuel_type','Average','status')
                                          print(header)
                                          print("-"*145)
                                          print()
                                          cursor.execute("select * from vehicles")
                                          record=cursor.fetchall()
                                          for i in record:        
                                                print("{:<25}{:<25}{:<25}{:<25}{:<25}{:<25}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
                                          print()
                                          print()

                                          print("DRIVERS AVAILABLE:")
                                          print("-"*21)                            
                                          print()
                                          header='{:<15}{:<15}{:<15} {:<15}{:<15}{:<15}'.format('Driver_id','Driver_name','Aadhar_number','Address','Phone','status')
                                          print(header)
                                          print("-"*83)
                                          print()
                                          cursor.execute("select * from driver")
                                          record=cursor.fetchall()
                                          for i in record:        
                                                print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
                                          print()
                                          print()

                                          print("TOUR PACKAGES AVAILABLE:") 
                                          print("-"*21)
                                          print()
                                          header='{:<15}{:<45}{:<25}{:<25}'.format('Package ID','Destinations','Durations','cost')
                                          print(header)
                                          print("-"*100)
                                          print()
                                          cursor.execute("select * from pakages")
                                          record=cursor.fetchall()
                                          for i in record:        
                                                print("{:<15}{:<45}{:<25}{:<25}".format(i[0],i[1],i[2],i[3]))
                                          print()
                                          print()
                                          bid=int(input("Enter the booking id:"))
                                          did=int(input("enter the ID of the Driver selected:"))
                                          vid=int(input("enter the ID of the Vehicle selected:"))
                                          pid=int(input("enter the ID of the Tour Package selected:"))
                                          name=input("Enter name of the customer:")
                                          adno=int(input("Enter Aadhar number of the customer:"))
                                          add=input("Enter Address of the customer:")
                                          phno=int(input("Enter Phone number of the customer:"))
                                          query="insert into bookings(booking_id, driverid, vehicleid, pakageid, name, Aadhar_number, address, phone_number)values({},{},{},{},'{}',{},'{}',{})".format(bid,did,vid,pid,name,adno,add,phno)
                                          cursor.execute(query)
                                          con.commit()
                                          print()
                                          print("Data added successfully")
                                          print()
                                      except :
                                          print()
                                          print("Booking ID already exist")
                                          print()
                                      ch=input("do you want to add another Tour Customer? (Y/N):").lower()
                                      if ch=="y":
                                          continue
                                      else:
                                          break

                              elif op2==2:                         #Displaying all bookings
                                    print()
                                    header='{:<15}{:<15}{:<15}{:<15}{:<30}{:<25}{:<20}{:<15}'.format('booking_id', 'driver_id', 'vehicle_id', 'pakage_id', 'Name', 'Aadhar_number', 'address', 'phone_number')
                                    print(header)
                                    print("-"*170)
                                    print()
                                    cursor.execute("select * from bookings")
                                    record=cursor.fetchall()
                                    for i in record:        
                                          print("{:<15}{:<15}{:<15}{:<15}{:<30}{:<25}{:<20}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                                    print()

                              elif op2==3:                     #Searching for a booking
                                    header='{:<15}{:<15}{:<15}{:<15}{:<30}{:<25}{:<30}{:<15}'.format('booking_id', 'driver_id', 'vehicle_id', 'pakage_id', 'Name', 'Aadhar_number', 'address', 'phone_number')
                                    serid=int(input("Enter the ID of the Customer to be searched:"))
                                    print()
                                    cursor.execute("select booking_id from bookings")
                                    r=cursor.fetchall()
                                    c=0
                                    
                                    for i in range(len(r)):
                                                if r[i][0] ==serid :
                                                      cursor.execute("SELECT * FROM bookings WHERE booking_id=%s", (serid,))
                                                      record=cursor.fetchall()
                                                      for i in record:
                                                            print(header)
                                                            print("-"*170)
                                                            print()
                                                            print("{:<15}{:<15}{:<15}{:<15}{:<25}{:<15}{:<30}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                                                else:
                                                      c+=1
                                    if c==len(r):
                                          print("Booking ID not found")

                              elif op2==4:                    #Deleting a booking record
                                    delid=int(input("Enter the ID of the Customer to be deleted:"))
                                    print()
                                    cursor.execute("select booking_id from bookings")
                                    r=cursor.fetchall()
                                    c=0
                                    
                                    for i in range(len(r)):
                                                if r[i][0] ==delid :
                                                      cursor.execute("DELETE FROM pakages WHERE pakage_id=%s", (delid,))
                                                      con.commit()
                                                      print("Deleted successfully!!") 
                                                else:
                                                      c+=1
                                    if c==len(r):
                                          print()
                                          print("Booking ID not found")
                                          print()

                              elif op2==5:               #Updating booking records
                                    upid=int(input("Enter the ID of the Customer to be updated:"))
                                    print()
                                    cursor.execute("select booking_id from bookings")
                                    record=cursor.fetchall()
                                    c=0
                                    
                                    for i in range(len(record)):
                                          if record[i][0] ==upid :
                                                
                                                      up1=int(input('''
                                                      What do you want to update?:
                                                      
                                                      1.Driver ID selected
                                                      2.Vehicle ID selected
                                                      3.Package ID selected
                                                      4.Customer name
                                                      5.Aadhar number
                                                      6.Address
                                                      7.Phone Number
                                                      8.Return to Home Page

                                                      Enter your choice:'''))
                                                      if up1==1:
                                                            udrid=input("Enter the updated Driver ID selected:")
                                                            cursor.execute("UPDATE bookings SET driverid=%s WHERE booking_id=%s",(udrid,upid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()
                                                      elif up1==2:
                                                            uvid=input("Enter the updated Vehicle ID selected::")
                                                            cursor.execute("UPDATE bookings SET vehicleid=%s WHERE booking_id=%s",(uvid,upid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()

                                                      elif up1==3:
                                                            upakid=input("Enter the updated Package ID selected::")
                                                            cursor.execute("UPDATE bookings SET pakageid=%s WHERE booking_id=%s",(upakid,upid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()
                                                      elif up1==4:
                                                            upname=input("Enter the updated Name of the customer:")
                                                            cursor.execute("UPDATE bookings SET name=%s WHERE booking_id=%s",(upname,upid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()
                                                      elif up1==5:
                                                            upaadhar=input("Enter the updated Aadhar number of the customer:")
                                                            cursor.execute("UPDATE bookings SET Aadhar_number=%s WHERE booking_id=%s",(upaadhar,upid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()
                                                      elif up1==6:
                                                            upadd=input("Enter the updated Address of the customer:")
                                                            cursor.execute("UPDATE bookings SET address=%s WHERE booking_id=%s",(upadd,upid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()
                                                      elif up1==7:
                                                            upphno=input("Enter the updated phone_number of the customer:")
                                                            cursor.execute("UPDATE bookings SET phone_number=%s WHERE booking_id=%s",(upphno,upid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()
                                                      

                                                      elif up1==8:
                                                            break
                                                      else:
                                                            print("Invalid Input")
                                          else:
                                                c+=1
                                    if c==len(record):
                                          print()
                                          print("Booking ID does not exist.")
                                    
                              elif op2==6:
                                    break  
                              ch=input("Do tou want to continue in Booking database? (Y/N):").lower()                #Option to continue using the bookings table
                              if ch=="y":
                                    continue
                              else:
                                    break
                  elif ch==5:                             #Transactions
                        print("*"*60)
                        print("-"*60)
                        print(" "*23,"Transactions"," "*27)
                        print("-"*60)
                        print("*"*60)
                        print()
                        while True:                             #Menu of Transactions
                              print('''
                                    1.Add new Transaction.
                                    2.Show all Transactions.
                                    3.Search a Transaction
                                    4.Delete a Transaction
                                    5.Update a Transaction.
                                    6.Return to Home Page''')
                              print()
                              op3=int(input("Enter your choice:"))

                              if op3==1:                             #Adding a Transaction record
                                    while True:

                                          try:
                                                tr_id=int(input("Enter the Transaction id:"))
                                                nm=input("Enter the name of the customer:")
                                                amt=float(input("Enter the Transaction amount:"))
                                                dt=input("Enter the date of transaction (YYYY/MM/DD) :")
                                                query="insert into transaction(transaction_id,name,amount,date_of_transaction)values({},'{}',{},'{}')".format(tr_id,nm,amt,dt)
                                                cursor.execute(query)
                                                con.commit()
                                                print()
                                                print("Data added successfully")
                                                print()
                                                ch=input("do you want to add another Transaction? (Y/N):").lower()
                                                if ch=="y":
                                                   continue
                                                else:
                                                   break
                                          except :
                                                print("transaction ID already exist")
                                                print()
                                          ch=input("do you want to add another Transaction? (Y/N):").lower()
                                          if ch=="y":
                                                continue
                                          else:
                                                break
                              elif op3==2:                             #Displaying all transactions
                                    print()
                                    header='{:<25}{:<35}{:<25}{:<25}'.format('Transaction ID','Name','Amount','Date_of_transaction')
                                    print(header)
                                    print("-"*100)
                                    print()
                                    cursor.execute("select * from transaction")
                                    record=cursor.fetchall()
                                    for i in record:        
                                          print("{:<25}{:<35}{:<25}{:<25}".format(i[0],i[1],i[2],str(i[3])))
                                    print()

                              elif op3==3:                          #Searching a transaction
                                    header='{:<25}{:<45}{:<25}{:<25}'.format('Transaction ID','Name','Amount','Date')
                                    serid=int(input("Enter the ID of the Transaction to be searched:"))
                                    print()
                                    cursor.execute("select transaction_id from transaction")
                                    r=cursor.fetchall()
                                    c=0
                                    
                                    for i in range(len(r)):
                                                if r[i][0] ==serid :
                                                      cursor.execute("SELECT * FROM transaction WHERE transaction_id=%s", (serid,))
                                                      record=cursor.fetchall()
                                                      for i in record:
                                                            print(header)
                                                            print("-"*140)
                                                            print()                                                      
                                                            print("{:<25}{:<25}{:<25}{:<25}{:<25}{:<25}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
                                                else:
                                                      c+=1
                                    if c==len(r):
                                          print("Transaction ID not found")
                                                
                              elif op3==4:                             #Deleting a Transaction
                                          delid=int(input("Enter the ID of the Transaction to be deleted:"))
                                          print()
                                          cursor.execute("select transaction_id from transaction")
                                          r=cursor.fetchall()
                                          c=0
                                          
                                          for i in range(len(r)):
                                                      if r[i][0] ==delid:
                                                            cursor.execute("DELETE FROM transaction WHERE transaction_id=%s", (delid,))
                                                            con.commit()
                                                            print("Deleted successfully!!")
                                                      else:
                                                            c+=1
                                          if c==len(r):
                                                print("Transaction ID not found!!")

                              elif op3==5:                            #Updating a transaction
                                    trid=int(input("Enter the ID of the Transaction to be updated:"))
                                    print()
                                    cursor.execute("select transaction_id from transaction")
                                    record=cursor.fetchall()
                                    c=0                              
                                    for i in range(len(record)):
                                          if record[i][0] ==trid :
                                                
                                                      up1=int(input('''
                                                      What do you want to update?:
                                                      
                                                      1.Name
                                                      2.amount
                                                      3.date
                                                      4.Return to Home Page

                                                      Enter your choice:'''))
                                                      if up1==1:
                                                            upname=input("Enter the updated Name of the customer:")
                                                            cursor.execute("UPDATE transaction SET name=%s WHERE transaction_id=%s",(name,trid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()

                                                      elif up1==2:
                                                            upamt=input("Enter the updated amount of transaction:")
                                                            cursor.execute("UPDATE transaction SET amount=%s WHERE transaction_id=%s",(upamt,trid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()
                                                      elif up1==3:
                                                            updt=input("Enter the updated date of transaction:")
                                                            cursor.execute("UPDATE transaction SET date_of_transaction=%s WHERE transaction_id=%s",(updt,trid))
                                                            con.commit()
                                                            print()
                                                            print("Updated successfully!!")
                                                            print()
                                                      elif up1==4:
                                                            break
                                                      else:
                                                            print("Invalid Input")
                                          else:
                                                c+=1
                                    if c==len(record):
                                          print()
                                          print("Package ID does not exist.")


                              else:
                                    print("Invalid input")
                                    break
                              print()
                              ch=input("Do tou want to continue in Transaction database? (Y/N):").lower()           #Choice to go back to the main menu
                              if ch=="y":
                                    continue
                              else:
                                    break
                  elif ch==6:
                        print()                          #Choice to end the program
                        print("signing out.....")
                        print()
                        break
                  else:
                        continue
      else:
            print("Wrong Password")
      if 2>1:
            continue

                        
