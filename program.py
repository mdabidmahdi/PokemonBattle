import random

def randomFloat():
    value = round(random.uniform(0.50,2.0), 2)
    return value

class Move:  #We will create multiple moves with type distinctions will be picked randomly based on level and type
    def __init__(self, type, name, damage, isDefensive):
        self.type = type
        self.name = name
        self.damage = damage
        self.isDefensive = isDefensive
        if isDefensive:
            self.category = "defensive"
        else:
            self.category = "attack"

   

quick_attack = Move('normal', 'quick attack', 10, False)
harden = Move('normal', 'harden', 0, True)
ember = Move('fire', 'ember', 20, False)
leaf_cutter = Move('grass', 'leaf cutter', 20, False)
bubble = Move('water', 'bubble',  20, False)
flame = Move('fire', 'flame',  40, False)
water_gun= Move('water', 'water gun', 40, False)
vine_strike= Move('grass', 'vine strike', 40, False)
cut =  Move('normal', 'cut', 20, False)
pound = Move('normal', 'pound', 25, False)


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
        defense = round(random.uniform(1,1.5), 2)
        self.hp = 100 * defense
        self.attack = randomFloat()
        self.speed = randomFloat()
        self.FULLHP = self.hp
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
    def hpConversion(self, damage):
        full = self.FULLHP
        outputPercentage = (damage / full ) * 100
        int(outputPercentage)
        return outputPercentage 
  
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
         self.player1.selectPokemon()
         self.player1.pokemon.selectMoves()


         self.player2 = Player(0, "CPU")
         self.player2.randomPokemon()
         self.player2.pokemon.selectMoves()
         self.winner = winner
         self.loser = loser
         self.turn = turn


    








    def startBattle(self):
        def winnerChecker():     
            if self.player1.pokemon.hp <= 0:
                self.winner = self.player2.name
                self.loser = self.player1.name
                print("Defeat!, Player 2 is the winner of this battle. ")
            if self.player2.pokemon.hp <= 0:    
                self.winner = self.player1.name
                self.loser = self.player2.name           
                print("Victory!, Player 1 is the winner of this battle. ")                                
                
                       




        print('Let the battle begin! ' + 'Your pokemon is: ' + self.player1.pokemon.name)
        print('Your  facing off  ' + self.player2.name + ", Their pokemon is: " + self.player2.pokemon.name)
        playerPokemon = self.player1.pokemon
        cpuPokemon = self.player2.pokemon
        while self.player1.pokemon.hp != 0 and self.player2.pokemon.hp  != 0:
            battle_turn = self.turn
            player_turn = self.player1.turn
            cpu_turn = self.player2.turn
            cpu_turn = 0
            player_turn = 1
            currentPlayerHp = playerPokemon.hpConversion(playerPokemon.hp)
            currentCPUHp =  cpuPokemon.hpConversion(cpuPokemon.hp)
            while player_turn == battle_turn:
                    print("============================================================")
                    print( self.player1.name +"'s " + playerPokemon.name + "s health is at: " + str(int(currentPlayerHp)) + "%")
                    print( self.player2.name +"'s " + cpuPokemon.name + "s health is at:"  + str(int(currentCPUHp)) + "%")
                    
                    outputDamage = 0
                    hpincrease = 0
                    choice = input("Would you like to attack or heal?(a/h) ")
                    if choice.lower() == 'a':
                        movesList = []
                        for x in playerPokemon.moves:
                            print(x.name)

                            movesList.append(str(x.name))

                        selectedMove = str(input("Select a move you would like to use: "))
                        moveChecker = 0
                
                        if selectedMove in  movesList:
                            outputMove = None
                            moveChecker = 1
                            for y in playerPokemon.moves:
                                 if selectedMove.lower() == y.name.lower():
                                    outputMove = y  
                                    
                        if moveChecker != 1:
                            print("Please select a correct move. ")
                            continue
                        if moveChecker == 1:
                            if outputMove.type != cpuPokemon.weakness and outputMove.type != cpuPokemon.immunity and outputMove.isDefensive != True: 
                                outputDamage = outputMove.damage * playerPokemon.attack
                                cpuPokemon.hp -= outputDamage
                                player_turn = 0
                                cpu_turn = 1
                                print("============================================================")
                                print( self.player1.name +"'s " + playerPokemon.name + " just used " + selectedMove)
                                print("You hit them for " + str(int(outputDamage)))
                                currentCPUHp = cpuPokemon.hpConversion(cpuPokemon.hp)
                                
                                
                                break    
                            if outputMove.type == cpuPokemon.weakness and outputMove.isDefensive != True: 
                                Elmentalmultiplier = 2.0
                                outputDamage = outputMove.damage * playerPokemon.attack * Elmentalmultiplier
                                cpuPokemon.hp -= outputDamage
                                player_turn = 0
                                cpu_turn = 1
                                print("============================================================")
                                print(self.player1.name +"'s " + playerPokemon.name + " just used " + selectedMove)
                                print("It's super effective! ")
                                print("You hit them for " + str(int(outputDamage)))
                                currentCPUHp = cpuPokemon.hpConversion(cpuPokemon.hp)
                                
                                break
                            if outputMove.type == cpuPokemon.immunity and outputMove.isDefensive != True:
                                Elmentalmultiplier = 0.5
                                outputDamage = outputMove.damage * playerPokemon.attack * Elmentalmultiplier
                                cpuPokemon.hp -= outputDamage
                                player_turn = 0
                                cpu_turn = 1
                                print("============================================================")
                                print(self.player1.name +"'s " + playerPokemon.name + " just used " + selectedMove)
                                print("It's not very effective! ")
                                print("You hit them for " + str(int(outputDamage)))
                                currentCPUHp = cpuPokemon.hpConversion(cpuPokemon.hp)
                                
                                
                                break
                            if outputMove.isDefensive == True:
                                hpincrease = 25
                                player_turn = 0
                                cpu_turn = 1
                            
                    elif choice.lower() == "h" and self.player1.healChances != 0:
                        print("============================================================")
                        print(self.player1.name + " just healed their pokemon!")
                        playerPokemon.hp += int(playerPokemon.FULLHP * 0.30)
                        playerPokemonCPUHp = playerPokemon.hpConversion(playerPokemon.hp)
                        self.player1.healChances -=1
                        player_turn = 0
                        cpu_turn = 1
                        break

                    elif choice.lower() == "h" and self.player1.healChances == 0:
                        print('You are out of heals! no heals available')
                        continue


                    
            while cpu_turn == 1:
                cpuDamage = 0
                cpu_hp_increase = 0
                if self.player2.pokemon.hp > 25:
                    choice = 'a'
                elif self.player2.pokemon.hp < 25 and self.player2.healChances != 0:
                    choice = 'h'
                else: choice = 'a'    
                if choice.lower() == 'a':
                        randomMoveSelectInt = random.randint(0,3)
                        cpuMove = cpuPokemon.moves[randomMoveSelectInt]
                        if cpuMove.type != playerPokemon.weakness and cpuMove.type != playerPokemon.immunity and cpuMove.isDefensive != True: 
                            cpuDamage = cpuMove.damage * cpuPokemon.attack
                            playerPokemon.hp -= cpuDamage
                            
                            print("============================================================")
                            print(self.player2.name +"'s " + cpuPokemon.name + " just used " + cpuMove.name)
                            print("They hit you for " + str(int(cpuDamage)))
                            currentPlayerHp = playerPokemon.hpConversion(playerPokemon.hp)  
                            player_turn = 1
                            cpu_turn = 0    
                            break

                        if cpuMove.type == playerPokemon.weakness and cpuMove.isDefensive != True: 
                            Elmentalmultiplier = 2.0
                            cpuDamage = cpuMove.damage * cpuPokemon.attack * Elmentalmultiplier
                            playerPokemon.hp -= cpuDamage
                            print("============================================================")
                            print(self.player2.name +"'s " + cpuPokemon.name + " just used " + cpuMove.name)
                            print("They hit you for " + str(int(cpuDamage)))
                            print("It's super effective! ")
                            currentPlayerHp = playerPokemon.hpConversion(playerPokemon.hp)  
                                
                            player_turn = 1
                            cpu_turn = 0
                            break
                            
                        if cpuMove.type == playerPokemon.immunity and cpuMove.isDefensive != True:
                            Elmentalmultiplier = 0.5
                            cpuDamage = cpuMove.damage * cpuPokemon.attack * Elmentalmultiplier
                            playerPokemon.hp -= cpuDamage
                            print("============================================================")
                            print(self.player2.name +"'s " + cpuPokemon.name + " just used " + cpuMove.name)
                            print("They hit you for " + str(int(cpuDamage)))
                            print("It's not very effective.")
                            currentPlayerHp = playerPokemon.hpConversion(playerPokemon.hp)  
                            player_turn = 1
                            cpu_turn = 0

                            break
                        if cpuMove.isDefensive == True:
                            print(cpuPokemon.name + " just used " + cpuMove.name)
                            hpincrease = 25
                            player_turn = 0
                            cpu_turn = 1
                            break
                    
                elif choice.lower() == "h" and self.player1.healChances != 0:
                    
                    self.player2.heal()
                    player_turn = 1
                    cpu_turn = 0
                                    
       
    




BattleStart = Battle('none', 'none', 1)
BattleStart.startBattle()




#Fix harden usage
#Fix heal usage
#Fix win and lose conditions