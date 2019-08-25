from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import license, fname, lname, mbutton, driving

# Create your views here.

from .ht61 import *
from .range_speed import *
from .analytics import * 

startButton = mbutton(False)
hButton = mbutton(False)
cButton = mbutton(True)

def FrontPageView(request):
	return render(request,'ht6p.html')



def TripView(request):

	all_License = license.objects.all()
	all_Fname = fname.objects.all()
	all_Lname = lname.objects.all()
	ll = len(all_License)
	ff = len(all_Fname)
	nn = len(all_Lname)
	userbegin(all_License[ll-1].content,all_Fname[ff-1].content,all_Lname[nn-1].content)

	all_currspeed = driving.objects.all()

	return render(request, 'mytrip.html', {'all_speed': all_currspeed})

def SummaryView(request):
	global startButton
	all_License = license.objects.all()
	ll = len(all_License)
	trips = getTripNo(all_License[ll-1].content)
	#changeformat()
	fans = calculate()
	myresult = city(fans[0],fans[1])
	addresult(all_License[ll-1].content,myresult)
	return render(request,'summary.html', {'mytrips':trips, 'finalres':myresult})

def startState(request):
	global startButton
	startButton.state = True
	drivingtrip()
	return HttpResponseRedirect('/trip/')

def stopState(request):
	x = driving.objects.all()
	num = len(x)

	if (num != 0):
		mytime = stopthetrip(x[num-1].speed)

	else: 
		mytime = stopthetrip(0)

	myplace = changearea(hButton.state,cButton.state)
	x.delete()
	filltripdata(mytime,myplace)

	return HttpResponseRedirect('/trip/')

def ChangeHState(request):
	global hButton
	global cButton
	if (hButton.state):
		hButton.state = False
		cButton.state = True
		changearea(hButton.state,cButton.state)
	else:
		hButton.state = True
		cButton.state = False
		changearea(hButton.state,cButton.state)
	return HttpResponseRedirect('/trip/')


def ChangeCState(request):
	global hButton
	global cButton
	if (cButton.state):
		cButton.state = False
		hButton.state = True
		changearea(hButton.state,cButton.state)
	else:
		cButton.state = True
		hButton.state = False
		changearea(hButton.state,cButton.state)
	return HttpResponseRedirect('/trip/')


def addSpeed(request):
	
	
	x = driving.objects.all()
	num = len(x)
	if (num != 0):
		ans = pausethetrip(x[num-1].speed)
	else: 
		ans = pausethetrip(0)
	new_speed = driving(speed = request.POST['speed'])
	new_speed.save()

	return HttpResponseRedirect('/trip/')

def addLicense(request):
	#find an attribute that has content in the post request
	new_license = license(content = request.POST['content'])
	new_license.save()
	return HttpResponseRedirect('/ht6p/')
	#create a new username object and save it
	#redirect browser to original browser /htp6/


def addFname(request):
	#find an attribute that has content in the post request
	newfname = fname(content = request.POST['content'])
	newfname.save()
	return HttpResponseRedirect('/ht6p/')
	#create a new username object and save it
	#redirect browser to original browser /htp6/

def addLname(request):
	#find an attribute that has content in the post request
	new_lname = lname(content = request.POST['content'])
	new_lname.save()
	return HttpResponseRedirect('/ht6p/')
	#create a new username object and save it
	#redirect browser to original browser /htp6/