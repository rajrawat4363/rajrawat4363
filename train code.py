class train:
    def __init__(self,name,fare,seat):
        self.name=name
        self.fare=fare
        self.seat=seat
    def getInfo(self):
        print(f"name of the train is{self.name}")
        print(f"seat available for booking{self.seat}")
    def fareTicket(self):
        print(f"the amount for the booking is Rs{self.fare}")
    def seatInfo(self):
        if (self.seat>0):
            print(f"seat remaing for booking{self.seat}")
            self.seat=self.seat-2
        else:
            print("try it in tatkal ")

raj=train("the Rajdhani Express:1234567",200,100)
raj.getInfo()
raj.fareTicket()
raj.seatInfo()
raj.seatInfo()
