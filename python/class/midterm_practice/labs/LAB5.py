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
            print(f"{animal.name} is already dead")
            return
        
        attack = self.atk

        
        if self.role == 'Mage':
            attack = self.atk + 0.8 * animal.atk
       
        defend = animal.defense
        if self.role == 'Warrior':
            defend *= 0.75


        totaldamage = attack - defend
        
        if animal.role == 'Tank':
            totaldamage *= 0.5
        
        totaldamage = max(0, int(totaldamage))
        animal.hp -= totaldamage
        if animal.hp <= 0:
            animal.hp = 0
            animal.state = 'Dead'
            
            

line = list(map(int,input().split()))
queries = line[0]
people = line[1]

animaldic = {}
for _ in range(people):
    name, atk, hp, defense, role = input().split()
    atk, hp, defense = int(atk), int(hp), int(defense)
    
    animaldic[name] = Animal(name, atk, hp, defense, role)
    
for _ in range(queries):
    alpha, beta = input().split()
    predator = animaldic[alpha]
    prey = animaldic[beta]
    predator.attack(prey)
    
for animal in animaldic.values():
    if animal.state == 'Alive':
        print(animal)
