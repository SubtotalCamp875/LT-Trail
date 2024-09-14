from colorama import Fore
import sys

class Characters:
    def __init__(self):
        self.names = ['', '', '', '', '']
        self.health = ['good', 'good', 'good', 'good', 'good'] #great, good, fair, poor
        self.alive = [True, True, True, True, True]
        self.conditions = ['None', 'None', 'None', 'None']

    def __list__(self):
        return(str(self.names))
    
    def rename(self):
        for i in range(4):
            changeConfirmation = ''
            i += 1
            if self.names[i] == '': self.names[i] = input(f'What would you like to name character {i}? ')
            else:
                while changeConfirmation not in ['y', 'n']: 
                    changeConfirmation = input(f'Character {i} is currently named {self.names[i]}. Would you like to change it? (y/n) ')
                if changeConfirmation == 'y':
                    self.names = input(f'What would you like to change {self.names[i]}\'s name to? ')
                else: pass

    def renameLeader(self): 
        self.names[0] = input('\nWhat is the name of the wagon leader? ')




def MainMenu():
    while True:
        menuOption = input(Fore.YELLOW + '\nWelcome to Lit Term Trail!\n' + Fore.RESET + 'You may:\n1.) Travel the Trail \n2.) Learn about the trail \n3.) Choose management options \n4.) End \nWhat is your choice? ')

        match menuOption:
            case '1': 
                break
            case '2': 
                dummyInput = input(Fore.GREEN + '\n[Press Enter to continue]' + Fore.RESET + '\nTry taking a journey by covered wagon acress 2000 miles of  plains, rivers, and mountins. Try! On the plains, will you slosh your oxen through mud and water-filled ruts or will you plod through dust 6 sixes deep?')
                dummyInput = input('How will you cross the rivers? if you have money you might take a ferry (if there is a ferry). Or, you can ford the river and hope you and your wagon arn\'t swallowed alive!')
                dummyInput = input('What about the supplies? Well, if you\'re low on food you can hunt. And there are bears in the mountains.')
                dummyInput = input('At the Dalles, you can try navigating the Columbian River, but if running the rapids with makeshift raft makes you queasy, better take the Barlow Road.')
                dummyInput = input('If for some reason you don\'t survive -- your wagon burns, or thieves steals your oxen, or you run out of provisions, or you die of cholera -- don\'t give up! Try again... and again... until your name is up with the others in history.')
            case '3': 
                managementOptions = ''
                while managementOptions != '1':
                    managementOptions = input(Fore.YELLOW + 'Management Options!\n' + Fore.RESET + 'You may:\n1.) Leave \nWhat is your choice? ')
            case '4': sys.exit(Fore.RED + 'Game Stopped' + Fore.RESET)



def SelectDifficulty():
    difficulty = ''
    while difficulty not in ['1', '2', '3']: 
        difficulty = input(Fore.YELLOW + '\nSelect Character' + Fore.RESET + '\nMany kinds of people made the trip to Oregon.\nYou may:\n1.) Be a printer from Boston \n2.) Be a librarian from Ohia \n3.) Be a farmer from Illinois \n4.) Find out the Difference between these choices\nWhat is your choice? ')
        
        if difficulty == '4':
            dummyInput = input(Fore.GREEN + '\n[Press Enter to continue]' + Fore.RESET + '\nTraveling to Oregon isn\'t easy! but if you\'re a printer, you\'ll have more money for supplies and services than a librarian or a farmer.\n\nHowever, the harder you have to try, the more points you deserve! Therefore, the farmer earns the greatest number of points and printer earns the least.')    

def SelectCharacterNames(character):
    character.renameLeader()
    character.rename()

    while True:
        confirmation = input(f'\nParty Members:\n1.) {character.names[0]} \n2.) {character.names[1]} \n3.) {character.names[2]} \n4.) {character.names[3]} \n5.) {character.names[4]} \nAre these names correct? (y/n) ')
        while confirmation not in ['y', 'n']: confirmation = input('Please selection a available option: ')
        if confirmation == 'y': break
        if confirmation == 'n':
            characterSelection = input('Which charcter would you like to change? ')
            while characterSelection not in ['1', '2', '3', '4', '5']: characterSelection = input('Please selection a available option: ')
            character.names[int(characterSelection)-1] = input(f'What would you like to rename {character.names[int(characterSelection)-1]} to? ')


def main():
    MainMenu()
    SelectDifficulty()
    character = Characters()
    SelectCharacterNames(character)

if __name__ == "__main__":
    main()