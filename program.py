import random

def randomFloat():
    value = round(random.uniform(0.50,2.0), 2)
    return value

class Move:  #We will create multiple moves with type distinctions will be picked randomly based on level and type
    def __init__(self, type, name, power, isDefensive):
        self.type = type
        self.name = name
        self.power = power
        self.isDefensive = isDefensive
        if isDefensive:
            self.category = "defensive"
        else:
            self.category = "attack"

    
  
quick_attack = Move('normal', 'Quick Attack', 10, False)
harden = Move('normal', 'Harden', 0, True)
ember = Move('fire', 'Ember', 20, False)
leaf_cutter = Move('grass', 'Leaf Cutter', 20, False)
bubble = Move('water', 'Bubble',  20, False)
flame = Move('fire', 'Flame',  40, False)
water_gun= Move('water', 'Water Gun', 40, False)
vine_strike= Move('grass', 'Vine Strike', 40, False)
cut =  Move('normal', 'Cut', 20, False)
pound = Move('normal', 'Pound', 25, False)


NormalMoves = [quick_attack, harden, pound, cut]
fireMoves = [ember, flame]
waterMoves = [bubble, water_gun]
grassMoves = [leaf_cutter, vine_strike]

class Pokemon:
    def __init__(self, Element_type):
        self.Element_type = Element_type
        self.level = random.randint(1,10)
        self.hp = 100
        self.attack = randomFloat()
        self.defense = randomFloat()
        self.speed = randomFloat()
        self.moves = []

    def selectMoves(self):
        type = self.Element_type
        selectionBreaker = 0
        while selectionBreaker < 2:
                randomValue = int(random.randint(0,3))
                newMove = NormalMoves[randomValue]
                if newMove in self.moves:
                    continue
                else:
                    self.moves.append(newMove)
                    selectionBreaker +=1
        if type == 'fire':
            self.moves.append(fireMoves[0])
            self.moves.append(fireMoves[1])
        elif type == 'water':
            self.moves.append(waterMoves[0])
            self.moves.append(waterMoves[1])
        elif type == 'grass':   
            self.moves.append(grassMoves[0])
            self.moves.append(grassMoves[1])

Bulbasaur = Pokemon('grass')
Charmander = Pokemon('fire')
Squirtle = Pokemon('water')
            








