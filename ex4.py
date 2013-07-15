# We'll start with 100 cars.
cars = 100
# The .0 part isn't really necessary because at no point will it be involved in division with a whole number.  Division by a whole number with another whole number is the only operation that would become inaccurate without a fractional section on at least one number.
space_in_a_car = 4.0
# We'll start with 30 drivers.
drivers = 30
# We'll start with 90 passengers.  It's probably not a coincidence that that's 3 times as many drivers.
passengers = 90
# stands to reason that counting cars without drivers would give a count of cars_not_driven
cars_not_driven = cars - drivers
# just for extra descriptiveness we can say that cars_driven is equal to drivers.
cars_driven = drivers
# a simple method of calculating total carpool capacity.  unsure why this figure is not used again in this exercise (so far).
carpool_capacity = cars_driven * space_in_a_car
# this would be more accurate if either passengers or cars_driven included a ".0".
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
