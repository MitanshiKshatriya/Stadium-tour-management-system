import sqlite3
tour=sqlite3.connect('stadiumTour1.db')
tr=tour.cursor()
tr.execute("CREATE TABLE stadium (Sno INTEGER,Sname TEXT,city TEXT,zipcode INTEGER PRIMARY KEY,capacity INTEGER);")
tr.execute("INSERT INTO stadium values(1,'Levis Stadium','Santa Clara',95050,107550);")
tr.execute("INSERT INTO stadium values(2,'CenturyLink Field','Seattle',98101,59677);")
tr.execute("INSERT INTO stadium values(3,'Ohio Stadium','Columbus',43004,62897);")
tr.execute("INSERT INTO stadium values(4,'Mercedes-Benz Stadium','Atlanta',63579,116746 );")
tr.execute("INSERT INTO stadium values(5,'Ford Field','Detroit',48127,49464);")

tr.execute("CREATE TABLE staff (stid INT PRIMARY KEY, Sname TEXT, job TEXT);")
tr.execute("INSERT INTO staff values(1234,'melissa','Background Singer');")
tr.execute("INSERT INTO staff values(4591,'stella','Background Singer');")
tr.execute("INSERT INTO staff values(5609,'bob','technician');")
tr.execute("INSERT INTO staff values(8905,'joel','guitarist');")

tr.execute("CREATE TABLE equipments (equipID INT, Ename TEXT, Qty INT);")
tr.execute("INSERT INTO equipments values(1,'Guitar',5);")
tr.execute("INSERT INTO equipments values(2,'Drums',1);")
tr.execute("INSERT INTO equipments values(3,'Mike',20);")

tr.execute("CREATE TABLE Merchandise (Type     CHAR (20) NOT NULL, merch_id INTEGER   PRIMARY KEY,quantity INTEGER,price    DOUBLE);")
tr.execute("INSERT INTO Merchandise values('Tshirt',1,10000,12.99);")
tr.execute("INSERT INTO Merchandise values('Hoodie',2,5000,24.99);")
tr.execute("INSERT INTO Merchandise values('CD,3,5500,10.99);")
tr.execute("INSERT INTO Merchandise values('Bands',4,20000,3.99);")

tr.execute("Create table Dist2(name text,city0 double,city1 double,city2 double,city3 double,city4 double, city5 double, city6 double,city7 double,);")

tour.commit();

