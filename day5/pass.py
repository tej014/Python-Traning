# Leaving a for loop, while loop, or if block completely empty causes an IndentationError because Python expects at least one statement inside an indented block Writing pass satisfies Python's syntax rules without changing loop behavior
#pass: Does nothing; simply acts as an empty placeholder inside a block
#we can also use it in if else
for i in range(10):
    pass
print("some usefull work")