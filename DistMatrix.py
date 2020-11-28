import sys
import sqlite3

tour=sqlite3.connect('stadiumTour.db')
tr=tour.cursor()


cities=[[0 for x in range(8)] for y in range(8)]

def createDistMatrix():
    sql="select city0,city1,city2,city3,city4,city5,city6,city7 from DISTMATRIX1;"
    tr.execute(sql)
    result=tr.fetchall()


    for i in range(0,8):
        for j in range(0,8):
            cities[i][j]=result[i][j]
    return cities




		

    






