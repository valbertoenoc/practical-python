# bounce.py
#
# Exercise 1.5

height = 100
bounce_height = 3/5
num_bounces = 1
while num_bounces <= 10:
    height = bounce_height*height
    print(num_bounces, round(height, 4))
    num_bounces += 1
