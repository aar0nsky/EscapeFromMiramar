# Text Adventure
import os
import sys
import json

def play():
    configData = loadConfig('game.json')
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
            print(command_keys[4]+':')
            for item in inventory:
                print('* ' + str(item) + '(' + str(inventory.get(item)) + ')')
        elif action_input in command_values[5]:
            print(command_keys[5])
            print('Key Binding \t\t\t\t\t Action')
            print('==============================================================')
            for x in range(0,len(commands)):
                if len(command_values[x]) > 2:
                    tabs = '\t\t'
                else:
                    tabs = '\t\t\t\t\t'
                print(str(command_values[x]) + tabs + str(command_keys[x]))
        elif action_input in command_values[6]:
            print(command_keys[6])
            exit()
        else:
            print("Invalid action!")

def loadConfig(filename):
    with open(filename) as json_data_file:
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

play()