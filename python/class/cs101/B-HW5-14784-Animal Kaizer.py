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
        
        damage = self.atk
        protect = animal.defense
        
        if self.role == 'Mage':
            damage = self.atk + 0.8 * animal.atk
            
        if self.role == 'Warrior':
            protect *= 0.75
    
        totaldamage = damage - protect
        
        if animal.role == 'Tank':
            totaldamage *= 0.5
            

        truedamage = max(0, int(totaldamage))
        
        animal.hp -= truedamage
        
        if animal.hp <= 0:
            animal.hp = 0
            animal.state = 'Dead'
        
    
# Write your code here
line = input().split()

queries = int(line[0])

animals = int(line[1])

animal_dict = {}
for _ in range(animals):
    collect = list(input().split())
    animal, atk, hp, defense, role = collect[0], int(collect[1]), int(collect[2]), int(collect[3]), collect[4]
    
    animal_dict[animal] = Animal(animal, atk, hp, defense, role)
    
for _ in range(queries):
    attack, defend = input().split()
    attacker = animal_dict[attack]
    defender = animal_dict[defend]

    attacker.attack(defender)
    
for values in animal_dict.values():
    if values.state == 'Alive':
        print(values)