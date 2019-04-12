print("Hello world")
# This is a single-line comment
cars = 5
driving = True
# cars = 5 → "5"

print("I have %d cars" % cars)
print("I have " + str(cars) + " cars")

age = input("How old are you")
print(age + "? My daughter is older than you.")

# Make a list of at least 5 colors
colors = ["blue", "yellow", "orange", "green", "red"]
colors.append("cyan")

print(colors)

colors.pop(0)
print(colors)

print(len(colors))
print(colors[1])
