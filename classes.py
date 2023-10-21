class Car:
    """A simple example class"""
    # Class attribute
    wheels = 4

    def __init__(self, make, model):
        # Instance attributes
        self.make = make
        self.model = model

    # Class method
    @classmethod
    def from_string(cls, car_string):
        make, model = car_string.split('-')
        return cls(make, model)
    
    def change_string(self, car_string):
        make, model = car_string.split('-')
        self.make=make
        self.model=model

if __name__=="__main__":
    car = Car('Ford', 'Fiesta')
    print(car.make, car.model, car.wheels)
    car2 = Car('Ford', 'Fiesta')
    car2.change_string('Ford-Fiesta2')
    print(car2.make, car2.model, car2.wheels)
    car3 = Car.from_string('Ford-Fiesta3')
    print(car3.make, car3.model, car3.wheels)
    print(Car.__doc__)


def scope_test():
    def do_local():# The default is binding variables in the local scope.
        spam = "local spam"

    def do_nonlocal():# nonlocal allows you to assign to variables in an outer (but non-global) scope.
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():# global allows you to assign to global variables.
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()# no change
    print("After local assignment:", spam)
    do_nonlocal()# change
    print("After nonlocal assignment:", spam)
    do_global()# change global
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)