'''
Clock Angle Problem:
Given a time say 6:32 find the angle between the Hour Hand and Minute Hand

Mathematical Solution:
1. The Minute Hand rotates through 360 degree every hour (60 mins) which gives you 6 degree every minute.
2. The Hour Hand rotates through 360 degree every 12hour (720 mins) which gives you 0.5 degree every minute

Mathematical Equation for the problem:
1. Angle of the Hour Hand = 0.5 X ((60 X H) + M)
2. Angle of the Minute Hand = 6 X M
3. Angle between the Hands = Absolute value of(Angle of Hour Hand - Angle of Min Hand)

H - Hours
M - Minutes

The solution to the Problem above 6:32 is
1. Angle of Hour Hand = 0.5 X ((60 X 6) + 32) = 0.5 X 392 = 196
2. Angle of Minute Hand = 6 X 32 = 192
3. Angle between the Hands = 196 - 192 = 4

'''

__author__="Ganesh"

hour = input ("Enter the hours in 12 hour clock")
minute = input ("Enter the minutes in an hour")

hourHandAngle = 0.5 * ((60*hour) + minute)
minHandAngle = 6 * minute
angleBtwHands = abs(hourHandAngle - minHandAngle)
print "Angle Between Hands of Hours and Minutes", hour, ":", minute, angleBtwHands