class Button:
    def __init__(self, state):
        self.state = state

    def turnon(self):
        self.state = True

    def turnoff(self):
        self.state = False

    def getstate(self):
        return (self.state)



class Person:
    def __init__(self,license,fname,lname,tripno):
        self.license = license
        self.fname = fname
        self.lname = lname
        self.tripno = tripno

    def addtrip(self):
        self.tripno +=1
