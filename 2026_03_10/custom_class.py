# Custom class
# naming covention
# PascalCase : class name
# CamelCase : object name
# snake_case : anything else

# class Car:
#     def __init__(self, color, engine_type):
#         self.color = color
#         self.engine_type = engine_type

# tesla = Car("green", "electric")
# # tesla.color = "red"
# # tesla.engine_type = "electric"

# print(tesla.color)
# How to list all the atributes?
# print(vars(tesla))

# constructor
# def __init__(self):
# when is called?
from car import Car

tesla = Car(color="green", engine_type="electric")
print(vars(tesla))
tesla.start_engine()
print(vars(tesla))

for i in range(1, 100):
    tesla.speed_up(1)
    print(tesla.speed)
    
for i in range(1, 100):
    tesla.speed_down(1)
    print(tesla.speed)
    