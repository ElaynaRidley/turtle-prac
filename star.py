# Elayna Ridley
# Aug 30 2017
from turtle import *
color('yellow', 'red')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
