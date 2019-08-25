import MySQLdb
import math
import sys
import csv
from time import process_time

count = 0

from .views import *
from .models import *
from .pyclass import Button
from .pyclass import Person
from .range_speed import *
from .analytics import *

flag = False 

curr = 0
timearr=[]
place = []

ebutton = Button(False)
startbutton = Button(False)
hbutton = Button(False)
cbutton =  Button(False)
sbutton = Button(False)

def filltripdata(mytime,myplace):
	config = {
			'host':'ht6db.cgs3zwhwsvzg.us-east-2.rds.amazonaws.com',
			'user':'clarice',
			'password':'ht6-project',
			'database':'test',
			'port':3306
		}
	conn = MySQLdb.connect(**config)
	cursor = conn.cursor()

	num = len(mytime)
	for x in range (num):
		val = (x,timearr[x],place[x])
		cursor.execute("INSERT INTO tripdata (time,speed,area) VALUES (%s, %s, %s);",val)

	conn.commit()
	cursor.close()
	conn.close()

def changearea (h,c):
	global place
	ela = round(time.process_time())
	if (h):
		x = "city"
	else:
		x = "highway"
	plist = [x] * ela
	place.extend(plist)
	return place 


def pausethetrip (cspeed):
	global curr
	global timeaerr
	global place
	ela = round(time.process_time())
	mlist = [cspeed] * ela
	timearr.extend(mlist)

def stopthetrip (cspeed):
	global timearr
	global place
	ela = round(time.process_time())
	mlist = [cspeed] * ela
	timearr.extend(mlist)
	return timearr
	



def drivingtrip ():
	global timearr
	global curr
	global place
	place = []
	timearr = []


def getTripNo (license):
	config = {
			'host':'ht6db.cgs3zwhwsvzg.us-east-2.rds.amazonaws.com',
			'user':'clarice',
			'password':'ht6-project',
			'database':'test',
			'port':3306
		}

	conn = MySQLdb.connect(**config)
	cursor = conn.cursor()
	cursor.execute("SELECT tripno FROM general WHERE license = %s;", (license,))
	total = (cursor.fetchone())[0]
	conn.commit()
	cursor.close()
	conn.close()

	return total



#def changeformat ():
	#config = {
	#		'host':'ht6db.cgs3zwhwsvzg.us-east-2.rds.amazonaws.com',
#			'user':'clarice',
	#		'password':'ht6-project',
	#		'database':'test',
	#		'port':3306
	#	}

#	conn = MySQLdb.connect(**config)
#	cursor = conn.cursor()

#	QUERY = 'SELECT * FROM test.tripdata'
#	cursor.execute(QUERY)
#	result = cursor.fetchall()

	#c = csv.writer(open('mynewtrip.csv','wb'))
#	for x in result:
#		c.writerow(x)

	#conn.commit()
#	cursor.close()
	#conn.close()

def addresult(license, score):
	config = {
			'host':'ht6db.cgs3zwhwsvzg.us-east-2.rds.amazonaws.com',
			'user':'clarice',
			'password':'ht6-project',
			'database':'test',
			'port':3306
		}

	conn = MySQLdb.connect(**config)
	cursor = conn.cursor()
	cursor.execute("INSERT INTO trip (license,score) VALUES (%s,%s);",(license,score))
	conn.commit()
	cursor.close()
	conn.close()


def userbegin (license, fname, lname):
		config = {
			'host':'ht6db.cgs3zwhwsvzg.us-east-2.rds.amazonaws.com',
			'user':'clarice',
			'password':'ht6-project',
			'database':'test',
			'port':3306
		}

		conn = MySQLdb.connect(**config)
		cursor = conn.cursor()

		cursor.execute("SELECT EXISTS (SELECT fname FROM general WHERE license = %s);",(license,))
		times = (cursor.fetchone())[0]


		if (times == 0):
				val = (license,fname,lname,0)
				cursor.execute("INSERT INTO general (license,fname,lname, tripno) VALUES (%s, %s, %s, %s);",val)
		
		else:
			cursor.execute("SELECT tripno FROM general WHERE license = %s;", (license,))
			track = (cursor.fetchone())[0]
			cursor.execute("UPDATE general SET tripno = %s WHERE license = %s;", (track +1, license))
	 # while (ebutton.state):
				 #if (sbutton.state):
							#change tripno general
							#result = CalcResult()
							#cursor.execute("INSERT INTO trip (license, time, dist, score) VALUES (%s, %s, %s);",(x.license, result[0], result[1], result[2]))
		


		conn.commit()
		cursor.close()
		conn.close()


def displayres (license):
		config = {
			'host':'ht6db.cgs3zwhwsvzg.us-east-2.rds.amazonaws.com',
			'user':'clarice',
			'password':'ht6-project',
			'database':'test',
			'port':3306
		}

		score = 0
		conn = mysql.connector.connect(**config)
		cursor = conn.cursor()

		cursor.execute("SELECT tripno FROM general WHERE license = %s;",(license,))
		total = (cursor.fetchone())[0]
		print(total)

		cursor.execute("SELECT SUM(score) FROM trip WHERE license = %s;",  (license,))
		sum = (cursor.fetchone())[0]
		print(sum/total)
		
		
		conn.commit()
		cursor.close()
		conn.close()


