class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayinfo(self):
        print 'Price is $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed) + "MPH"
        print 'Total Miles: ' + str(self.miles) + 'miles'
    
    def drive(self):
        print 'Driving'
        self.miles += 10

    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
            self.miles -= 5

bike1 = Bike(99.99, 12)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(139.99, 20)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()