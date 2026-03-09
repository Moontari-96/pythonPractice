# random module
import random

# print(random.randint(1, 100))

# import joon_module

# print(joon_module.MY_NATURAL_COUNTRY)

# random_float = random.random()
# print(random_float)

# how to generate 0 - 10???
# print(int(random_float * 10))

random_value = random.randint(0, 10)
if random_value % 2 == 0:
  print("You get Head")
else:
  print("You get Tail")