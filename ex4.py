# Tne number of available cars
cars = 100

# How much space in each car?
space_in_a_car = 4.0

# How many drivers have we got?
drivers = 30

# How many passengers are there?
passengers = 90

# cars_not_driven equals the number of cars minus the number of drivers
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
