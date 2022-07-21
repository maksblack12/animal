import random



ENERGY_LOSS=1
ENERGY_GAIN=2
HEALTH_GAIN=1
FOOD_CHACE=0.5
SIMULATION_TIME=100 #random.randint(1,10)



class Animal:
	def __init__(self, health, energy, species):
		self.health = health
		self.energy = energy
		self.species = species
		self.position=[0,0]

	def move(self):
		self.position[0]+=random.randint(-1,1)
		self.position[1]+=random.randint(-1,1)
		self.energy-=ENERGY_LOSS

	def eat(self):
		if random.uniform(0,1)>FOOD_CHACE:
			print("mniam, mniam")
			self.energy+=ENERGY_GAIN
			self.health+=HEALTH_GAIN

	def print(self):
		print( self.species,self.health, self.energy,self.position)

	def do_stuff(self):
		self.move()
		self.eat()
		self.print()

animals=[
	Animal(100, 200, "dog"),
	Animal(900, 100, "kitty cat"),
	Animal(200, 100, "horse")
]

for x in range(SIMULATION_TIME):
	for animal in animals:
		animal.do_stuff()
	print("\n")

