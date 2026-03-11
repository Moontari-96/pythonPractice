import time
from turtle import Turtle, done

john = Turtle()
print(john)
john.shape("turtle")
john.color("red", "green")
while True:
    john.forward(5)
    john.left(5)
    time.sleep(1)
done()