###Flight simulator.
# Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth).
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop2

# - until user breaks the loop
# Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations").
# With every simulation step the orentation should be corrected, applied and printed out.
# If you can thing of any other features, you can add them.
# This code shoud be runnable with 'python kol1.py'.
# If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
# Do your best, show off with good, clean, well structured code - this is more important than number of features.
# After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
# Good Luck


###############
# at least 2 classes
# about 5 methods each
# use "if __name__ "
# pep 8
# proper names for variables
# INPROVED SIMULATION

import numpy as np
from time import sleep
import sys




class Plane:
    def __init__(self, planeName, tilt, weather):
        if isinstance (tilt, (int, float)):
            self.tilt = tilt
        else:
            print "Proper tilt parameter must be float or int."
        if isinstance(planeName, str):
            self.name = planeName
        else:
            print "Proper plane name parameter must be a string."

        self.weather = weather


    def correct_tilt(self):
        if self.tilt > 0:
            self.tilt -= 4
        else:
            self.tilt += 4

    def amount_of_cycles_input(self):
        i = input("How many cycles do you want? Recommended values are bigger then 7\n")
        return i

    def weather_status(self):
        print self.weather.print_weather()

    def start_simulation(self):

        i = self.amount_of_cycles_input()

        print "Look at the weather before the simulation: \n\t"
        self.weather_status()
        sleep(5)

        print "Simulation has started and it will last for {} cycles." \
              " Press ctl^C to stop earlier.".format(i)
        print "Starting orientation of {0} in degrees --> {1}".format(self.name, self.tilt).rjust(25)

        j = 0
        while 1 > 0:
            self.tilt += np.random.randint(-3, 3) + np.random.random()
            print str(j) + ")  " + "Current orientation of {0} in degrees -> {1}".format(self.name, self.tilt).rjust(25)

            self.correct_tilt()


            j += 1
            sleep(0.7)
            if j == i:
                print "SIMULATION HAS ENDED. I HOPE YOU ENJOYED :)."
                sys.exit()

            ##
            # tilt correction

class Weather:
    def __init__(self):
        self.humidity = str(np.random.random()*100)+"%"
        self.fog = np.random.choice( ["none", "thin", "average", "really bad"])
        self.rain = np.random.choice( ["none", "drizzle", "average", "storm"])

    def print_weather(self):
        print "The humidity: {}".format(self.humidity)
        print "Fog status : {}".format(self.fog)
        print "Rain status : {}".format(self.rain)

    def change_param(self, param, value):
        setattr(self, param, value)


if __name__ == '__main__':
	weather1 = Weather()
	weather1.change_param("rain", 'drizzle')
	test1 = Plane("Boeing", 35, weather1)
	test1.start_simulation()



