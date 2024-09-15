from colorama import Fore
import sys, time

class Characters:
    def __init__(self):
        self.names = ['', '', '', '', '']
        self.health = [70, 70, 70, 70, 70] #great, good, fair, poor
        self.alive = [True, True, True, True, True]
        self.conditions = ['None', 'None', 'None', 'None']
        self.pace = 'steady'
        self.readingRate = 'entertaining'

    def __list__(self):
        return(str(self.names))
    
    def rename(self):
        for i in range(4):
            changeConfirmation = ''
            i += 1
            if self.names[i] == '': self.names[i] = input(f'What would you like to name character {i}? ')
            else:
                while changeConfirmation not in ['y', 'n']: 
                    changeConfirmation = input(f'Character {i+1} is currently named {self.names[i]}. Would you like to change it? (y/n) ')
                if changeConfirmation == 'y':
                    self.names = input(f'What would you like to change {self.names[i]}\'s name to? ')
                else: pass

    def renameLeader(self): 
        self.names[0] = input('\nWhat is the name of the wagon leader? ')


class Supplies():
    def __init__(self):
        self.oxen = 0
        self.clothing = 0
        self.tokens = 0
        self.wheels = 0
        self.axles = 0
        self.tongues = 0
        self.knowledge = 0
        self.money = 0



def MainMenu():
    while True:
        menuOption = input(Fore.YELLOW + '\nWelcome to Lit Term Trail!\n' + Fore.RESET + 'You may:\n1.) Travel the trail \n2.) Learn about the trail \n3.) Choose management options \n4.) End \nWhat is your choice? ')

        match menuOption:
            case '1': 
                break
            case '2':
                print('test')
                dummyInput = input(Fore.GREEN + '\n[Press Enter to continue]' + Fore.RESET + '\nTry taking a journey by covered wagon across' + Fore.CYAN + ' 2000 ' + Fore.RESET + 'miles of plains, rivers, and mountins. \nTry! On the plains, will you slosh your oxen through mud and water-filled ruts\nor will you plod through dust' + Fore.CYAN + ' 6 ' + Fore.RESET + 'inches deep?')
                dummyInput = input(Fore.BLUE + 'How will you cross the rivers? ' + Fore.RESET + 'If you have' + Fore.YELLOW + ' money ' + Fore.RESET + 'you might take a ferry (if there is a ferry). \nOr, you can ford the river and hope you and your wagon arn\'t swallowed alive!')
                dummyInput = input(Fore.BLUE + 'What about the supplies? ' + Fore.RESET + 'Well, if you\'re low on ' + Fore.YELLOW + 'knowledge' + Fore.RESET + ' you can spend tokens.')
                dummyInput = input('At the Dalles, you can try navigating the ' + Fore.RED + 'Columbian River' + Fore.RESET + ', \nbut if running the rapids with makeshift raft makes you queasy, better pay for the ' + Fore.RED + 'Barlow Road' + Fore.RESET + '.')
                dummyInput = input('If for some reason you don\'t survive \n' + Fore.RED + '-- your wagon burns, or thieves steals your oxen, or you run out of provisions, or you die of cholera --' + Fore.RESET + ' \ndon\'t give up! Try again... and again... \nuntil your name is up with the others in history.')
            case '3': 
                managementOptions = input(Fore.YELLOW + '\nManagement Options!\n' + Fore.RESET + 'You may:\n1.) Leave \nWhat is your choice? ')
                while managementOptions not in ['1']: managementOptions = input(InvalidOption)
                match managementOptions:
                    case '1': pass
            case '4': sys.exit(Fore.RED + 'Game Stopped' + Fore.RESET)



def SelectDifficulty():
    difficulty = ''
    while difficulty not in ['1', '2', '3']: 
        difficulty = input(Fore.YELLOW + '\nSelect Character' + Fore.RESET + '\nMany kinds of people made the trip to Oregon.\nYou may:\n1.) Be a printer from Boston \n2.) Be a librarian from Ohia \n3.) Be a farmer from Illinois \n4.) Find out the Difference between these choices\nWhat is your choice? ')
        
        if difficulty == '4':
            dummyInput = input(Fore.GREEN + '\n[Press Enter to continue]' + Fore.RESET + '\nTraveling to Oregon isn\'t easy! but if you\'re a printer, you\'ll have more money for supplies and services than a librarian or a farmer.\n\nHowever, the harder you have to try, the more points you deserve! Therefore, the farmer earns the greatest number of points and printer earns the least.')
    return difficulty



def SelectCharacterNames(character):
    character.renameLeader()
    character.rename()

    while True:
        confirmation = input(f'\nParty Members:\n1.) {character.names[0]} \n2.) {character.names[1]} \n3.) {character.names[2]} \n4.) {character.names[3]} \n5.) {character.names[4]} \nAre these names correct? (y/n) ')
        while confirmation not in ['y', 'n']: confirmation = input(InvalidOption)
        if confirmation == 'y': break
        if confirmation == 'n':
            characterSelection = input('Which charcter would you like to change? ')
            while characterSelection not in ['1', '2', '3', '4', '5']: characterSelection = input(InvalidOption)
            character.names[int(characterSelection)-1] = input(f'What would you like to rename {character.names[int(characterSelection)-1]} to? ')



def MonthSelection():
    month = ''
    while month not in ['1', '2', '3', '4', '5']: 
        month = input(Fore.YELLOW + '\nMonth Selection' + Fore.RESET + '\nIt is 1848. Your jumping off place for Oregon is Independence Missouri. You must decide which month to leave Independence.\n1.) March \n2.) April \n3.) May \n4.) June \n5.) July \n6.) Ask for advice\nWhat is your choice? ')
        if month == '6':
            dummyInput = input(Fore.GREEN + '\n[Press Enter to continue]' + Fore.RESET + 'You attend for public meeting for "folks with the California - Oregon fever" You\'re told:\n\nIf you leave too early, there won\'t be any grass for your oxen to eat. If you leave too late, you may not get to Oregon before winter comes. If you leave at just the right time, there will be green grass and the weather will still be cool.')
    match month:
        case '1': month = 'March'
        case '2': month = 'April'
        case '3': month = 'may'
        case '4': month = 'June'
        case '5': month = 'July'
    return month



def FirstShop(difficulty, month, supplies):
    match difficulty:
        case '1': balance = 1600.0
        case '2': balance = 800.0
        case '3': balance = 400.0
    yokeAmount, oxenCost, knowledgeCost, clothingCost, tokenCost, partsCost, totalCost = 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

    dummyInput = input(Fore.GREEN + '\n[Press Enter to continue]' + Fore.RESET + f'\nBefore leaving Independence you should buy equipment and supplies. \nYou have ${balance} in cash, but you don\'t have to spend it all now.')
    dummyInput = input('You can buy whatever you need at the Bitmoji Store')
    dummyInput = input('\nHello, I\'m LT. So you\'re going to Oregon! \nI can fix you up with what you need: \n\n- a team of oxen to pull your wagon\n- clothing for both summer and winter')
    dummyInput = input('- plenty of knowledge for the trip\n- tokens for pop quizzes\n- spare parts for your wagon')


    while True:
        shopOption = input(Fore.YELLOW + f'\nBitmoji Store\nIndependence, Missouri\n{month} 1, 1848' + Fore.RESET + f'\n0.) Leave Store\n1.) Oxen: ${oxenCost}0 \n2.) Knowledge: ${knowledgeCost}0 \n3.) Clothing ${clothingCost}0 \n4.) Tokens: ${tokenCost}0 \n5.) Spare Parts: ${partsCost}0\n=============================\nTotal Bill: ${totalCost}0\n\nAmount you have: ${balance}0\nWhich item would you like to buy? ')

        match shopOption:
            case '0':
                if yokeAmount == 0: 
                    print(Fore.RED + 'Don\'t forget, you\'ll need oxen to pull your wagon' + Fore.RESET)
                    time.sleep(2)
                elif totalCost > balance: 
                    print(Fore.RED + f'Okay, that comes to a total of ${totalCost}0. But I see that you only have ${balance}0. \nWe\'d better go over the list again' + Fore.RESET)
                    time.sleep(2)
                else: break

            case '1':
                yokeAmount = input(Fore.CYAN + f'\nBitmoji Store\nIndependence, Missouri' + Fore.YELLOW + f'\nBill so far: ${totalCost}0' + Fore.RESET + '\nThere are 2 oxen in a yoke;\nI recommend at least 3 yoke.\nI charge $40 a yoke.\nHow many yoke do you want? (1 min, 9 max) ')
                while True:
                    if yokeAmount.isdigit() == False: yokeAmount = input(InvalidOption)
                    elif float(yokeAmount) > 9 or float(yokeAmount) < 1: yokeAmount = input(InvalidOption)
                    else: break
                oxenCost = float(yokeAmount) * 40
                supplies.oxen = int(yokeAmount) * 2

            case '2':
                knowledgeAmount = input(Fore.CYAN + f'\nBitmoji Store\nIndependence, Missouri' + Fore.YELLOW + f'\nBill so far: ${totalCost}0' + Fore.RESET + '\nI recommend you take at least 200 points of knowledge for each person in your family. \nI see that you have 5 people in all. You\'ll need pens, ink, paper, and books. \nMy price is 20 cent per knowledge.\nHow many points of knowledge do you want? (2000 max) ')
                while True:
                    if knowledgeAmount.isdigit() == False: knowledgeAmount = input(InvalidOption)
                    elif float(knowledgeAmount) > 2000 or float(knowledgeAmount) < 0: knowledgeAmount = input(InvalidOption)
                    else: break
                knowledgeCost = float(knowledgeAmount) * 0.2
                supplies.knowledge = int(knowledgeAmount)

            case '3':
                clothingAmount = input(Fore.CYAN + f'\nBitmoji Store\nIndependence, Missouri' + Fore.YELLOW + f'\nBill so far: ${totalCost}0' + Fore.RESET + 'nYou\'ll need warm clothing in the mountains. \nI recommend taking at least 2 sets of clothes per person. \nEach set is $10.00. \nHow many sets of clothes do you want? (160 max) ')
                while True:
                    if clothingAmount.isdigit() == False: clothingAmount = input(InvalidOption)
                    elif float(clothingAmount) > 160 or float(clothingAmount) < 0: clothingAmount = input(InvalidOption)
                    else: break
                clothingCost = float(clothingAmount) * 10
                supplies.clothing = int(clothingAmount)

            case '4':
                tokenAmount = input(Fore.CYAN + f'\nBitmoji Store\nIndependence, Missouri' + Fore.YELLOW + f'\nBill so far: ${totalCost}0' + Fore.RESET + 'I sell tokens in stacks of 20.\nEach stack cost $2.00\nHow many stacks do you want? (800 max) ')
                while True:
                    if tokenAmount.isdigit() == False: tokenAmount = input(InvalidOption)
                    elif float(tokenAmount) > 800 or float(tokenAmount) < 0: tokenAmount = input(InvalidOption)
                    else: break
                tokenCost = float(tokenAmount) * 2
                supplies.tokens = int(tokenAmount) * 20

            case '5':
                print(Fore.CYAN + f'\nBitmoji Store\nIndependence, Missouri' + Fore.YELLOW + f'\nBill so far: ${totalCost}0' + Fore.RESET + '\nIt\'s a good idea to have a few spare parts for your wagon\nHere are the prices:\nwagon wheel - $10 each\nwagon axle - $10 each\nwagon tongue - $10 each\n')
                wheelAmount = input('How many wagon wheels? ')
                while wheelAmount.isdigit() == False: wheelAmount = input(InvalidOption)
                axleAmount = input('How many wagon axles? ')
                while axleAmount.isdigit() == False: axleAmount = input(InvalidOption)
                tongueAmount = input('How many wagon tongues? ')
                while tongueAmount.isdigit() == False: tongueAmount = input(InvalidOption)
            
                partsCost = (float(wheelAmount) + float(axleAmount) + float(tongueAmount)) * 10
                supplies.wheels, supplies.axles, supplies.tongues = int(wheelAmount), int(axleAmount), int(tongueAmount)

        totalCost = oxenCost + knowledgeCost + clothingCost + tokenCost + partsCost
        supplies.money = balance - totalCost
    dummyInput = input(Fore.GREEN + '\n[Press Enter to continue]' + Fore.RESET + f'\nWell then, you\'re ready to start. Good Luck! \nYou have a long and difficult journey ahead of you.')



def CalculateHealth(character):
    avgHealth = 0
    for i in range(len(character.health)): avgHealth += character.health[i]
    avgHealth /= len(character.health)
    
    if avgHealth > 75: health = 'great'
    elif avgHealth > 50: health = 'good'
    elif avgHealth > 25: health = 'fair'
    elif avgHealth > 0: health = 'poor'

    return health 


def Menu(character, supplies, month):
    health = CalculateHealth(character)
    weather = 'cool' #WIP

    while True:
        print(Fore.MAGENTA + f'\nIndependence\n{month} 1, 1848' + Fore.RESET)
        print(Fore.YELLOW + f'Weather: {weather}\nHealth: {health}\nPace: {character.pace}\nReading Rate: {character.readingRate}' + Fore.RESET)
        option = input('1.) Continue on the trail\n2.) Check supplies\n3.) Change pace\n4.) Change reading rate\n5.) Stop to rest\n6.) Attempt to trade\n7.) Read for knowledge\nWhat is your choice? ')
        while option not in ['1', '2', '3', '4', '5', '6', '7']: option = input(InvalidOption)
        match option:
            case '1': break
            case '2': 
                dummyInput = input(Fore.YELLOW + '\nYour Supplies:' + Fore.RESET + f'\noxen: {supplies.oxen}\nsets of clothing: {supplies.clothing}\ntokens: {supplies.tokens}\nwagon wheels: {supplies.wheels}\nwagon axles: {supplies.axles}\nwagon tongues: {supplies.tongues}\npoints of knowledge: {supplies.knowledge}\nmoney left: ${supplies.money}0\n\n' + Fore.GREEN + '[Press Enter to continue]' + Fore.RESET)
            case '3':
                while True:
                    paceOption = input(f'\nChange pace (currently "{character.pace}")\nThe pace at which you travel can change. Your choices are: \n1.) a steady pace\n2.) a strenuous pace\n3.) a grueling pace\n4.) find out what these different paces mean\nWhat is your choice? ')
                    if paceOption == '4': 
                        print('option 4')
                        continue #wip
                    while paceOption not in ['1', '2', '3']: paceOption = input(InvalidOption)
                    break

                if paceOption == '1': character.pace = 'steady'
                elif paceOption == '2': character.pace = 'strenuous'
                elif paceOption == '3': character.pace = 'grueling'

            case '4':
                readingRateOptions = input(f'\nChange reading rate (currently "{character.readingRate}")\The amount of knowledge the people in your party consume each day can change. These amounts are: \n1.) entertaining - reads many hours a day.\n2.) enjoyable - party reads a small but satisfactory amount.\n3.) disappointing - very few pages read; everyone stays craving for more.\nWhat is your choice? ')
                while readingRateOptions not in ['1', '2', '3']: readingRateOptions = input(InvalidOption)

                if readingRateOptions == '1': character.readingRate = 'entertaining'
                elif readingRateOptions == '2': character.readingRate = 'satisfactory'
                elif readingRateOptions == '3': character.readingRate = 'disappointing'

            case '5':
                rest = input('\nHow many days would you like to rest? ')
                #WIP

            case '6':
                pass #WIP

            case '7':
                pass #WIP



def main():
    global InvalidOption
    InvalidOption = 'Please selection a available option: '
    character = Characters()
    supplies = Supplies()

    MainMenu()
    difficulty = SelectDifficulty()
    SelectCharacterNames(character)
    month = MonthSelection()
    FirstShop(difficulty, month, supplies)

    while True:
        Menu(character, supplies, month)
    


if __name__ == "__main__":
    main()