class Animal():
    def __init__(self, name: str, atk: int, hp: int, defense: int, role: str):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.defense = defense
        self.role = role
        self.state = "Alive"    
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        if state == "Alive" or state == "Dead":
            self._state = state 

    def __str__(self):
        return f"{self.role} {self.name}: {self.hp}"
    
    def attack(self, animal: "Animal"):
        if self.state == 'Dead':
            print(f'{self.name} is already dead')
            return
        if animal.state == 'Dead':
            print(f'{animal.name} is already dead')
            return

        attackpower = self.atk
        if self.role == 'Mage':
            attackpower = self.atk + (0.8 * animal.atk)
        
        effectivedef = animal.defense
        if self.role == 'Warrior':
            effectivedef *= 0.75

        damage = attackpower - effectivedef
        if animal.role == 'Tank':
            damage *= 0.5

        damage = max(0, int(damage))

        animal.hp -= damage
        if animal.hp <= 0:
            animal.hp = 0
            animal.state = 'Dead'
        
    
# Write your code here
line_one = input().split()
queries, animals = int(line_one[0]), int(line_one[1])

animal_dict = {}
for _ in range(animals):
    kaiser = list(input().split())
    name, role = kaiser[0], kaiser[4]
    atk, hp, defense = int(kaiser[1]), int(kaiser[2]), int(kaiser[3])

    animal_dict[name] = Animal(name, atk, hp, defense, role)

for _ in range(queries):
    preyy, victimm = input().split()
    prey = animal_dict[preyy]
    victim = animal_dict[victimm]
    prey.attack(victim)

for animal in animal_dict.values():
    if animal.state == 'Alive':
        print(animal)
