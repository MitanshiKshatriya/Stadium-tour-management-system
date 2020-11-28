import sys,datetime
import tsp_dynamic,DistMatrix
import sqlite3
tour=sqlite3.connect('stadiumTour.db')
tr=tour.cursor()
#stadium starts
def displaycities():
      sql="SELECT * from stadium;"
      tr.execute(sql)
      result=tr.fetchall();
      #print(result)
      #for record in result:
            #print (record)
      print("Sno\tStadium Name\tCity\tZipcode\tCapacity")
      for record in result:
            print(record[0],"\t",record[1],"\t",record[2],"\t",record[3],"\t",
                  record[4],"\t")

def searchcities():
      name=input('Enter the name')
      sql="SELECT sname,city from stadium WHERE city='"+name+"';"
      tr.execute(sql)
      result=tr.fetchone()
      if result==None:
            print("no record found")
      else:
            print(result[0],",",result[1],"\n")

def shrtst_path():
      w=DistMatrix.createDistMatrix()
      l=tsp_dynamic.travel(w)
      print("shortest Path is:")
      for i in range(len(l[1])):
        print(l[1][i],"->",end=" ")
      print('\nTotal cost is-',l[0])


#stadium ends


#staff starts
def displaystaff():
      sql="SELECT * from staff;"
      tr.execute(sql)
      result=tr.fetchall();
      #print(result)
      #for record in result:
            #print (record)
      print("Stid\tStaff name\tJob")
      for record in result:
            print(record[0],"\t",record[1],"\t",record[2])


def searchstaff():
      name=input('Enter the name: ')
      sql="SELECT stid,sname,job from staff WHERE Sname='"+name+"';"
      tr.execute(sql)
      result=tr.fetchone()
      if result==None:
            print("no record found")
      else:
            print(result[0],",",result[1],",",result[2],"\n")

def updatestaff():
      
      print("""
                  1.Insert
                  2.Delete
                  3.Update
            """)
      c=int(input("enter c hoice"))
      if c==1:
            try:
                  x=int(input('Enter stid:'))
                  y=input('Enter sname')
                  z=input('enter job')
                  tr.execute("insert into staff values(?,?,?)",(x,y,z))
                  tour.commit()
                  print ("One record added successfully.")
            except:
                  print ("Error in operation.")

                  tour.rollback()

      elif c==2:
            try:
                  x=input('Enter the staff name to be deleted:')
                  tr.execute("delete from staff where sname='"+x+"';")
                  print('delete sucessfull')
                  tour.commit()
            except:
                  print('error in Operation')

                  tour.rollback()
                  
      elif c==3:
            try:
                  w=input('Enter the staff name to be update')
                  x=int(input('Enter stid:'))
                  y=input('Enter sname')
                  z=input('enter job')
                  tr.execute('update staff set stid=?,sname=?,job=? where sname=?;',(w,x,y,z))
                  tour.commit()
                  print("record updated sucessfully")
            except:
                  print ("Error in operation.")

                  tour.rollback()
            

            
      
#staff ends

#equpments starts

def displayequipments():
      sql="SELECT * from equipments;"
      tr.execute(sql)
      result=tr.fetchall();
      #print(result)
      #for record in result:
            #print (record)
      print("equipID\tEName\tQty")
      for record in result:
            print(record[0],"\t",record[1],"\t",record[2])

def searchequipments():
      name=input('Enter the equipment: ')
      sql="SELECT equipID,Ename,Qty from Equipments WHERE Ename='"+name+"';"
      tr.execute(sql)
      result=tr.fetchone()
      if result==None:
            print("no record found")
      else:
            #
            print(result[0],",",result[1],",",result[2],"\n")

def updateequipments():
      
      print("""
                  1.Insert
                  2.Delete
                  3.Update
            """)
      c=int(input("enter c hoice"))
      if c==1:
            try:
                  x=int(input('Enter equipid:'))
                  y=input('Enter ename')
                  z=input('enter qty')
                  tr.execute("insert into equipments values(?,?,?)",(x,y,z))
                  tour.commit()
                  print ("One record added successfully.")
            except:
                  print ("Error in operation.")

                  tour.rollback()

      elif c==2:
            try:
                  x=input('Enter the ename name to be deleted:')
                  tr.execute("delete from equipments where Ename='"+x+"';")
                  print('delete sucessfull')
                  tour.commit()
            except:
                  print('error in Operation')

                  tour.rollback()
                  
      elif c==3:
            try:
                  w=input('Enter the ename name to be update')
                  x=int(input('Enter equipid:'))
                  y=input('Enter ename')
                  z=input('enter qty')
                  tr.execute('update equipments set equipID=?,Ename=?,Qty=? where Ename=?;',(w,x,y,z))
                  tour.commit()
                  print("record updated sucessfully")
            except:
                  print ("Error in operation.")

                  tour.rollback()



#equipment ends

#merchandise starts
def displaymerchandise():
      sql="SELECT * from merchandise;"
      tr.execute(sql)
      result=tr.fetchall();
      #print(result)
      #for record in result:
            #print (record)
      print("Type\tHoodie\tQty\tprice")
      for record in result:
            print(record[0],"\t",record[1],"\t",record[2],"\t",record[3])

def searchmerchandise():
      name=input('Enter the type of merchandise: ')
      sql="SELECT * from merchandise WHERE Type='"+name+"';"
      tr.execute(sql)
      result=tr.fetchone()
      if result==None:
            print("no record found")
      else:
            #
            print(result[0],",",result[1],",",result[2],",",result[3],"\n")


def updatemerchandise():
      
      print("""
                  1.Insert
                  2.Delete
                  3.Update
            """)
      c=int(input("enter c hoice"))
      if c==1:
            try:
                  x=int(input('Enter type:'))
                  y=input('Enter merch_id')
                  z=input('enter quantity')
                  v=input('enter price')
                  tr.execute("insert into merchandise values(?,?,?)",(x,y,z,v))
                  tour.commit()
                  print ("One record added successfully.")
            except:
                  print ("Error in operation.")

                  tour.rollback()

      elif c==2:
            try:
                  x=input('Enter the type of merch to be deleted:')
                  tr.execute("delete from merchandise where type='"+x+"';")
                  print('delete sucessfull')
                  tour.commit()
            except:
                  print('error in Operation')

                  tour.rollback()
                  
      elif c==3:
            try:
                  w=input('Enter the ename name to be update')
                  x=int(input('Enter type:'))
                  y=input('Enter merch_id')
                  z=input('enter quantity')
                  v=input('enter price')
                  
                  tr.execute('update merchandise set type=?,merch_id=?,quantity=?,price=? where =?;',(w,x,y,z,v))
                  tour.commit()
                  print("record updated sucessfully")
            except:
                  print ("Error in operation.")

                  tour.rollback()
#merchandise ends

      
def cities():
      done=False
      while done==False:
            print("""==========Touring Cities=========
                  1.Display the cities
                  2.Search a city
                  3.Generate shortest path
                  4.Go to main menu
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                  displaycities()
            elif choice==2:
                  searchcities()
            elif choice==3:
                  shrtst_path()
            elif choice==4:
                  main()


def staff():
      done=False
      while done==False:
            print("""==========Staff module==========
                  1.Display Staff
                  2.Search a Staff
                  3.Update staff table
                  4.Go to main menu
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                  displaystaff()
            elif choice==2:
                  searchstaff()
            elif choice==3:
                  updatestaff()
            elif choice==4:
                  main()

def equipments():
      done=False
      while done==False:
            print("""==========Staff module==========
                  1.Display Equpments
                  2.Search a Equipment
                  3.Update Equipment table
                  4.Go to main menu
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                  displayequipments()
            elif choice==2:
                  searchequipments()
            elif choice==3:
                  updateequipments()
            elif choice==4:
                  main()

def merchandise():
      done=False
      while done==False:
            print("""==========Staff module==========
                  1.Display Merchandise
                  2.Search a Merchandise
                  3.Update Merchandise table
                  4.Go to main menu
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                  displayemerchandise()
            elif choice==2:
                  searchmerchandise()
            elif choice==3:
                  updatemerchandise()
            elif choice==4:
                  main()

def main():            
      done=False
      while done==False:
            print(""" ======STADIUM TOUR MANAGEMENT MENU=======
                  1. Touring cities
                  2. Staff
                  3. Equipments
                  4.Merchandise
                  5. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        cities()
            elif choice==2:
                        staff()
            elif choice==3:
                        equipments()
            elif choice==4:
                  merchandise()
            elif choice==5:
                  sys.exit()
                  
main()
