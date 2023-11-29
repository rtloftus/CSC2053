class Car:
    def __init__ (self, color, engine_type, gas_tank, odometer):
        self.color = color
        self.engine_type = engine_type
        self.gas_tank = gas_tank
        self.odometer = odometer
    
    def __str__(self):
        return "This car is", self.color, ", has", self.engine_type, "engine, has", self.gas_tank, "gallons of gas, and", self.odometer, "miles."
    
    def drive(self):
        if self.engine_type == "4_cylinder":
            self.gas_tank = self.gas_tank - 3
            self.odometer = self.odometer + 90
        elif self.engine_type == "V8":
            self.gas_tank = self.gas_tank - 4
            self.odometer = self.odometer + 50
      

    def get_gas_tank(self):
        return self.gas_tank
    
    def get_odometer(self):
        return self.odometer
    


    


        
    
