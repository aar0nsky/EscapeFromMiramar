# Text Adventure
import os
import sys
import json

class Weapon:
    name = ""
    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagge1r"
        self.description = "A small dagger with some rust. " \
                            "Somewhat more dangerous than a rock."
        self.damage = 10

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "This sword is showing its age, " \
                            "but still has some fight in it."
        self.damage = 20

class RayGun(Weapon):
    def __init__(self):
        self.name = "Ray Gun"
        self.description = "This gun shoots rays of excellence at anyone"
        self.damage = 17.5

class Wand:
    def __init__(self):
        self.name = "Wand"
        self.description = "This wand is made from a piece of hay"
        self.damage = 3

def play():
    config_file = 'game.json'
    configData = loadConfig(config_file)
    character = loadCharacterData(configData)
    inventory = loadInventory(configData)
    commands = buildCommands()
    
    command_keys=list(commands.keys())
    command_values=list(commands.values())

    welcomeMessage(character.get('Name'))

    while True:
        action_input = get_player_input()
        if action_input in command_values[0]:
            print(command_keys[0])
        elif action_input in command_values[1]:
            print(command_keys[1])
        elif action_input in command_values[2]:
            print(command_keys[2])
        elif action_input in command_values[3]:
            print(command_keys[3])
        elif action_input in command_values[4]:
            clearScreen()
            print(command_keys[4]+':')
            for item in inventory:
                print('* ' + str(item) + '(' + str(inventory.get(item)) + ')')
        elif action_input in command_values[5]:
            clearScreen()
            print(command_keys[5] + '\n')

            print('Key Binding \t\t\t\t\t Action')
            print('==============================================================')
            for x in range(0,len(commands)):
                if len(command_values[x]) > 2:
                    tabs = '\t\t'
                else:
                    tabs = '\t\t\t\t\t'
                print(str(command_values[x]) + tabs + str(command_keys[x]))
        elif action_input in command_values[6]:
            print('Exiting...')
            saveConfig(configData,config_file)
            exit()
        else:
            print("Invalid action!")

def loadConfig(filename):
    with open(filename, 'r') as json_data_file:
        data = json.load(json_data_file)
    return data

def loadCharacterData(configData):
    character = {}
    character['Name']=configData['character']['name']
    return character

def loadInventory(configData):
    inventory = {}
    for item in configData['inventory']: 
        for quantity in configData['inventory'][item]:
            if(item == Dagger().name):
                inventory[Dagger()]=quantity
            else:
                inventory[item]=quantity
    return inventory

def buildCommands():
    commands = {}
    commands['Go North!']={'n','N'}
    commands['Go South!']={'s', 'S'}
    commands['Go East!']={'e', 'E'}
    commands['Go West!']={'w', 'W'}
    commands['Inventory']={'i', 'I'}
    commands['Help']={'h', 'H', 'help', 'Help', 'HELP'}
    commands['Quit']={'q','Q', 'quit', 'Quit', 'QUIT'}
    return commands

def welcomeMessage(characterName):
    clearScreen()
    print("===Escape from Miramar===")
    print("Welcome " + characterName + '!')

def get_player_input():
    return input('Action: ')

def clearScreen():
    if(sys.platform == 'Windows'):
        os.system('cls')
    else:
        os.system('clear')

def saveConfig(configData, filename):
    with open(filename, 'w') as json_data_file:
        json.dump(configData, json_data_file)

play()