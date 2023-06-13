#class FlightSimu
class FlightSimulator:
    def __init__(self,plane):
        self.plane=plane
        self.is_flying=False

    def takeoff(self):
        if not self.is_flying:
            self.plane.start_engines()
            self.plane.takeoff()
            self.is_flying=True
            print("The plane has take off")

    def land(self):
        if self.is_flying:
            self.plane.land()
            self.plane.stop_engines()
            self.is_flying=False
            print("The plane landed")

    def turn_left(self,degrees):
        if self.is_flying:
            self.plane.turn_left(degrees)
            print(f"the plane has turned {degrees} left")

    def turn_right(self,degrees):
        if self.is_flying:
            self.plane.turn_right(degrees)
            print(f"the plane has turned {degrees} right")

    def ascend(self,altitude):
        if self.is_flying:
            self.plane.ascend(altitude)
            print(f"the plane ascended {altitude} feet")

    def descend(self,altitude):
        if self.is_flying:
            self.plane.descend(altitude)
            print(f"the plane descended {altitude} feet")

#class Samolot
class Plane:
    def __init__(self,name):
        self.name=name

    def start_engines(self):
        print(f"{self.name}: Engines started")

    def stop_engines(self):
        print(f"{self.name}: Engines stopped")

    def takeoff(self):
        print(f"{self.name}: Took off")

    def land(self):
        print(f"{self.name}: Landed")

    def turn_left(self,degrees):
        print(f"{self.name}: Turned left {degrees} degrees")

    def turn_right(self,degrees):
        print(f"{self.name}: Turned right {degrees} degrees")

    def ascend(self,altitude):
        print(f"{self.name}: Ascended {altitude} feet")

    def descend(self,altitude):
        print(f"{self.name}: Descended {altitude} feet")

# Examples:
plane=Plane("Tupolew Tu-154M")
simulator=FlightSimulator(plane)

simulator.takeoff()
simulator.ascend(100)
simulator.descend(50)
simulator.turn_left(100)
simulator.turn_right(100)

