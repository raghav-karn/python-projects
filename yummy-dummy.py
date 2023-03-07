import random

foods = ["Hamburger",
		"Chocolate Cake",
		"Ice-Cream",
		"Raspberry Sorbet n' Tuile",
		"Popcorn"]

places = ["California",
		  "Cupertino",
		  "Apple Park",
		  "Shanghai",
		  "Mumbai",
		  "Kyoto"]

people = ["Joe Biden",
		  "Warren Edward Buffet",
		  "Gordon Ramsay",
		  "Marco Pierre White",
		  "Steve Wozniak",
		  "Tim Cook"]

food = random.choice(foods)
place = random.choice(places)
person1 = random.choice(people)
person2 = random.choice(people)

if person1 == person2:
	person2 = random.choice(people)

print(f"How 'bout to eat {food} at {place} with {person1} and {person2}?")
