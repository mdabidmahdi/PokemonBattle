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
    def __init__(self, Element_type, name, trainer):
        self.trainer = trainer
        self.name = name
        self.Element_type = Element_type
        self.level = random.randint(1,10)
        self.hp = 100
        self.attack = randomFloat()
        self.defense = randomFloat()
        self.speed = randomFloat()
        self.moves = []
        if self.Element_type == 'fire':
             self.weakness = 'water'
             self.immunity = 'grass'
        if self.Element_type == 'water':
            self.weakness = 'grass'
            self.immunity = 'fire'
        if self.Element_type == 'grass':
             self.weakness = 'fire'
             self.immunity = 'water'
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

playerName = input('What is your name? ')
class Player:
    def __init__(self, turn, name):
        self.turn = turn
        self.healChances = 3
        self.name = name
    def selectPokemon(self):
        while True:
            selection = input("What pokemon do you want to battle with? (Bulbasaur, Charmander, Squirtle)")
            if selection.lower() == 'bulbasaur':
                self.pokemon = Pokemon('grass', 'Bulbasaur', playerName)
                break
            elif selection.lower() == 'squirtle':
                self.pokemon = Pokemon('water', 'Squirtle', playerName)
                break
            elif selection.lower() == 'charmander':    
                self.pokemon = Pokemon('fire', 'Charmander', playerName)
                break
            else:
                print('Select a correct pokemon from the avaialbe ones.')
                continue
    def randomPokemon(self):
        randomValue = int(random.randint(1,3))
        if randomValue == 1:
                self.pokemon = Pokemon('grass', 'Bulbasaur', "CPU")      
        elif randomValue == 2:
                self.pokemon = Pokemon('water', 'Squirtle', "CPU")        
        elif randomValue == 3:    
                self.pokemon = Pokemon('fire', 'Charmander', "CPU")
    def heal(self):
         if self.pokemon.hp != 100 and self.healChances > 0:
            self.pokemon.hp + 35
            self.healChances -= 1
         else: print('Your pokeon is already at full health!')
                



class Battle:
    def __init__(self, winner, loser, turn):
         self.player1 = Player(0, playerName)
         self.player2 = Player(0, "CPU")
         self.winner = winner
         self.loser = loser
         self.turn = turn


    








    def startBattle(self):
        print('Let the battle begin! ' + 'Your pokemon is' + self.player1.pokemon.name)
        print('Your  facing off pokemon is' + self.player2.name + "Their pokemon is: " + self.player2.pokemon.name)
        self.player1.pokemon.hp =  self.player1.pokemon.hp * self.player1.pokemone.defense
        self.player2.pokemon.hp =  self.player2.pokemon.hp * self.player2.pokemone.defense
        playerPokemon = self.player1.pokemon
        cpuPokemon = self.player2.pokemon
        while self.player1.pokemon.hp != 0 and self.player2.pokemon.hp  != 0:
            battle_turn = self.turn
            player_turn = self.player1.turn
            cpu_turn = self.play2.turn

            if player_turn == 1:
                while True:
                    print( playerPokemon.name + "s health is at: " + playerPokemon.pokemon.hp)
                    print( cpuPokemon.name + "s health is at: " + cpuPokemon.pokemon.hp)
                    outputDamage = 0
                    hpincrease = 0
                    choice = input("Would you like to attack or heal?(a/h) ")
                    if choice.lower() == 'a':
                        for x in playerPokemon.moves:
                            print(x.name)
                        while True:
                            selectedMove = input("Select a move you would like to use: ")
                            for x in playerPokemon.moves:
                                    if selectedMove == x.name and x.isDefensive != True:
                                        if playerPokemon.weakness == cpuPokemon.weakness:
                                            Elmentalmultiplier = 2.0
                                            outputDamage = x.damage * playerPokemon.attack * Elmentalmultiplier
                                            cpuPokemon.hp - outputDamage
                                            player_turn = 0
                                            cpu_turn = 1
                                            break
                                        if playerPokemon.immunity == cpuPokemon.immunity:
                                            Elmentalmultiplier = 0.5
                                            outputDamage = x.damage * playerPokemon.attack * Elmentalmultiplier
                                            cpuPokemon.hp - outputDamage
                                            player_turn = 0
                                            cpu_turn = 1
                                            break
                                    else: 
                                        print("Selecta correct move: ")
                                        continue
                                    if x.isDefensive == True:
                                        hpincrease = 25
                                        player_turn = 0
                                        cpu_turn = 1
                                        break
                            break  
                        break              
                    elif choice.lower() == "h" and self.player1.healChances != 0:
                        self.player1.heal()
                        player_turn = 0
                        cpu_turn = 1
                        break
                    elif choice.lower() == "h" and self.player1.healChances == 0:
                        print('You are out of heals! no heals available')
                        continue




                    
            elif cpu_turn == 1:
                print( playerPokemon.name + "s health is at: " + playerPokemon.pokemon.hp)
                print( cpuPokemon.name + "s health is at: " + cpuPokemon.pokemon.hp)
                cpu_Damage = 0
                cpu_hp_increase = 0
                if self.player2.pokemon.hp > 25:
                    choice = 'a'
                elif self.player2.pokemon.hp < 25 and self.player2.healChances != 0:
                    choice = 'h'
                else: choice = 'a'    
                if choice.lower() == 'a':
                        randomMoveSelectInt = random.randint(0,3)
                        selectedMove = cpuPokemon.moves[randomMoveSelectInt]
                        if selectedMove == x.name and x.isDefensive != True:
                            if playerPokemon.weakness == cpuPokemon.weakness:
                                Elmentalmultiplier = 2.0
                                cpuDamage = x.damage * playerPokemon.attack * Elmentalmultiplier
                                playerPokemon.hp - cpu_Damage

                                player_turn = 1
                                cpu_turn = 0
                            
                            if playerPokemon.immunity == cpuPokemon.immunity:
                                Elmentalmultiplier = 0.5
                                outputDamage = x.damage * playerPokemon.attack * Elmentalmultiplier
                                playerPokemon.hp - cpu_Damage

                                player_turn = 1
                                cpu_turn = 0
                            if x.isDefensive == True:
                                hpincrease = 25
                                player_turn = 0
                                cpu_turn = 1
                    
                elif choice.lower() == "h" and self.player1.healChances != 0:
                    self.player2.heal()
                    player_turn = 1
                    cpu_turn = 0
                                    
        if self.player1.pokemon.hp == 0:
                self.winner = self.player2.name
                self.loser = self.player1.name
                print("Defeat!, Player 2 is the winner of this battle. ")
        if self.player2.pokemon.hp == 0:    
                self.winner = self.player1.name
                self.loser = self.player2.name           
                print("Victory!, Player 1 is the winner of this battle. ")                                

                       

    







userPlayer = Player(0, 1, playerName)
userPlayer.selectPokemon()
userPlayer.pokemon.selectMoves()

