class Car:
    __color = "red"
    __make = "Toyota"
    __model = "Tercel"

    def get_attr(self):
        print(f'Car: {self.__color} {self.__make} {self.__model}')

car = Car()
car.get_attr()
    