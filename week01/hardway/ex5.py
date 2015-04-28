"""Exercise 5: More Variables and Printing."""

name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weigth = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weigth)
print("Actually that's not too heavy.")
print("He's got %s and %s hair." % (eyes, hair))
print("His teet are usually %s depending on the coffee" % teeth)

# this line is tricky, try to get it exactly right
sum = age + height + weigth
print("If i add %d, %d, and %d I get %d." % (age, height, weigth, sum))
