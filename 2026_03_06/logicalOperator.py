# Logical Operators
# A and B : Both should be True
# X or Y : One of them is True
# not E : The opposite value True <-> False

value = 3.2
# if isinstance(value, int) and \
#   value > 5:
#   print("Correct")
# else:
#   print("Not correct")


if not isinstance(value, float):
  print(f"{value} is not float")
else :
  print(f"{value} is float")