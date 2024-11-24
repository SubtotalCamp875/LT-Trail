import random
from colorama import Fore

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
        self.tokens = 100
        self.wheels = 0
        self.axles = 0
        self.tongues = 0
        self.knowledge = 0
        self.money = 0



class Date():
    def __init__(self):
        self.day = 1
        self.month = ''
        self.year = 1848
        self.monthIndex = 3
        self.monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def updateMonth(self):
        self.month = self.monthList[self.monthIndex]

    def increaseDay(self, n, update=False):
        for _ in range(n):
            self.day += 1
            if self.day > self.dayList[self.monthIndex]:
                self.day = 1
                self.increaseMonth()
            if update == True:
                if Wait == True:
                    time.sleep(0.5)
                print(self.month, str(self.day) + ',', self.year)

    def increaseMonth(self):
        self.monthIndex += 1
        if self.monthIndex > 11:
            self.monthIndex = 0
            self.year += 1
        self.month = self.monthList[self.monthIndex]


def VocabList(l:list = [1, 2, 3]):
    ls1 = {
        0: ["Divulge", "v", "to tell; to reveal (as a secret)", "The reporter was fired when she divulged information from a classified document."],
        1: ["Abet", "v", "to assist or encourage, especially in wrongdoing", "Jim refused to abet the criminal's escape by hiding him in the basement."],
        2: ["Ardor", "n", "an intense feeling of devotion or eagerness", "The defending troops fought with ardor ebcause the emeny would not be taking any prisoners."],
        3: ["Dogmatic", "adj", "arrogant and stubborn about one's beliefs", "Beause of the professer's dogmatic approach, the students were afraid to ask questions."],
        4: ["Insipid", "adj", "lacking favor; dull; not at all simulating", "My mom wanted me to be an accountant, but I found the classes boring and insipid."],
        5: ["Proclivity", "n", "a natural leaning or tendency", "Abigail's procivility for history led her to write a book on the founders of her home town."],
        6: ["Extraneous", "adj", "not essentail; not constituing a vital part", "The professor felt that the extraneous paragraph in the essay detracted from the more important infomation."],
        7: ["Coerce", "v", "to force by using presssure, intimadation, or threats", "Jerry preferred basketball', but ihs father coerced him into palying football."],
        8: ["Jaundiced", "adj", "prejudice; hostile", "Gabe had jaunduced view of Iraq after losing his wife in the Gulf War."],
        9: ["Occlude", "v", "to block the passage of", "A large mass of clay occuleded the water pipe, causing a dangerous rise in pressure."],
        10: ["Meticulous", "adj", "extremely, sometimes excessively, carefule about small details; precise", "With meticulous care, he crafted a miniature dollhouse for his daughter."],
        11: ["Temerity", "n", "recklessness; a foolish disregurd of danger", "I couldn't believe that Bret had the temerity to bungee jump over a lake full of alligators."],
        12: ["Rote", "n", "a habitual repetitive routine or procedure", "Kristan memorized the piano sonata through rote, by practiciing the song over and over until she could play it perfectly."],
        13: ["Ascribe", "v", "to credit as to the cuase or the source", "The carpenter ascribed the rotten floorboards to a leaky roof."],
        14: ["Gregarious", "adj", "sociable; fond of the company of others", "Just before he was diagnosed with clinical depression, Raji went from being gregarious to being anitsocial."]
    }

    ls2 = {
        0: ["Disabuse", "v", "to free someone from believing something false", "Pam felt it was time to disabuse her son of his belief in the tooth fairy."],
        1: ["Heresy", "n", "the act of holding a belief that goes against established doctrine", "During the inquisition, those found guilty of heresy were sometimes burned at the sake."],
        2: ["Audit", "v", "to check the accruacy of financial accounts and records", "When sienna is ready to graduate, the university will audit her records to verify that she took all the required classes."],
        3: ["Motley", "adj", "made up of dissimilar parts; being of many colors", "The international clown convention was a motley sight in the otherwise dull exhibition center."],
        4: ["Libation", "n", "a drink, especially an alcoholic one", "When we visited the vineyard, we were offered a small libation at the end of our tour."],
        5: ["Docile", "adj", "easy to teach or manage; obedient", "The poodle, usually doctile, went mad and attacked its owner."],
        6: ["Restive", "adj", "restless and impatient", "Two restive students sat in chairs outside the principals office waiting to be called inside."],
        7: ["Banter", "n", "teasing; playful converseration", "At the reunion, ruth enjoyed listening to the banter of her husband and his old college roommate."],
        8: ["Castigate", "v", "to criticize or punish serverly", "The parson castigated the boy for noisily chewing gum in church."],
        9: ["Anathema", "n", "a hated, repellant person or thing", "Cannibalism is anathema to almost every society on the planet."],
        10: ["Gauche", "adj", "lacking social grace; tactless", "Some people use a fork to eat pizza because they think it is gauche to use their fingers."],
        11: ["Ignominy", "n", "public shame, disgrace, or dishonor", "The mayor fell from public acclaim to complete ignomny in a week when her cocaine habit was discovered."],
        12: ["Dither", "v", "to hesitate nervously", "When asked if he had completed his homework assignment, luke dithered, knwoing that he had forgotten about it."],
        13: ["Emaciated", "adj", "extremely thin; wasted away", "Dead from starvation, the emacieted prisoner was buried in the camp cemetery."],
        14: ["Repine", "v", "to be discontent as though yearning for something; complain", "Nathan repined loudly in his room after getting grounded for picking on his sister."]
    }

    ls3 = {
        0: ["Irascible", "adj", "easily angered", "We walk on eggshells around marty because he is so irascible."],
        1: ["Bacchanalian", "adj", "wild and drunken", "Adam paid for his bacchanalian weekend when he flunked the exam on monday."],
        2: ["Maudlin", "adj", "foolishly sentimenttal; ridiculously emotional", "The scame artist put forth a maudlin display of outrage when his victims accused him of stealing their money."],
        3: ["Extradite", "v", "to turn over or deliver to the legal jurisdiction of antoehr government or authority", "After two months of incarceration in sacramento, the suspect was extradited to florida."],
        4: ["Furitive", "adj", "stealthy; secretive", "Not wanting to be rude, jean cast only a furtive glance at the man's prominent scar."],
        5: ["Mettle", "n", "courage and determination", "The secret mission behind enemy lines would require soldiers who have mettle because many probably wouldn't be coming back."],
        6: ["Conflate", "v", "to combine into one", "When henry wrote about cavemen hunting dinosaurs, his teacher explained that he had conflated two ideas."],
        7: ["Mercenary", "n", "a professional solder hired bu a foreign army", "Thought american by bith, the mercaenary fought for france."],
        8: ["Bastion", "n", "a strong defense or fort (or something likened to it)", "The united states has been called the bastion of democracy."],
        9: ["Avarice", "n", "greed; desire for wealth", "He became a doctor, not to save lives, but to appease his avarice."],
        10: ["Jettison", "v", "to cast overboard; to discard", "The passengers quickly jettisoned the heavy cargo from the damaged plane."],
        11: ["Solvent", "adj", "able to pay all debts and financial obligations", "The owner of the company must keep the business solvent or else vendors will refuse to be business with him."],
        12: ["Ostracize", "v", "to banish; to shut from a group or society by common consent", "The strict religious community ostracized eli when he married a woman of another faith."],
        13: ["Tackle", "n", "the equipment for a specific activity", "At the dive shop, you can rent tackle for today's trip to half moon cove."],
        14: ["Copious", "adj", "numerousl large in quanity", "It is good to drink a copious amount of water before and after working out."]
    }


    allVocab = [ls1, ls2, ls3]
    total = []
    for i in range(len(l)):
        total.append(allVocab[l[i]-1])
    return(total)
    
"""
structure of 'total' vocab list

total =
[
    {
        0: [
            'Divulge', 
            'v', 
            'to tell; to reveal (as a secret)',
            'The reporter was fired when she divulged information from a classified document.'
        ],
        1: [],
        2: []
    },
    {},
    {}
]
"""


def Menu(character, supplies, date):
    supplies = QuizOptions(supplies)



def QuizOptions(supplies):
    quizOption = input(Fore.YELLOW + '\nQuiz Menu\n' + Fore.RESET + f'0.) Leave.\n1.) Take a quiz (1 token).\n2.) Change list of vocabs.\nYou currently have {supplies.tokens} tokens\nYour option:')
    while quizOption not in ['1', '2', '0']: quizOption = input(InvalidOption)
    match quizOption:
        case '0': pass
        case '1': supplies = Quiz(supplies)
        case '2': SelectVocab()
    return(supplies)



def Quiz(supplies):
    total = VocabList(SelectedLesson)
    word1, word2, word3 = [], [], []
    name = 0
    verbTense = 1
    definition = 2
    example = 3
    supplies.tokens -= 1

    for i in range(3):
        listNum = random.randint(0, len(total)-1)
        dictNum = random.randint(0, len(total[listNum])-1)
        if i == 0: word1 = total[listNum][dictNum]
        if i == 1: word2 = total[listNum][dictNum]
        if i == 2: word3 = total[listNum][dictNum]

    ansNum = random.randint(0, 3)-1
    vocabOptionList = [word1, word2, word3]

    print(Fore.YELLOW + '\nQuizzes\n' + Fore.RESET + f'You currently have {supplies.tokens} tokens\nSelect the definition to the given word: ' + Fore.CYAN + f'{vocabOptionList[ansNum][name]}' + Fore.RESET + f'\n\n1.) {word1[verbTense]}, {word1[definition]}\n2.) {word2[verbTense]}, {word2[definition]}\n3.) {word3[verbTense]}, {word3[definition]}\n\n' + Fore.GREEN + 'Need a hint? Press "h" (It will cost 1 token)' + Fore.RESET, end = '')
    while True:
        quizOption = input('\nWhat is the answer? ')
        while quizOption not in ['1', '2', '3', 'h']: quizOption = input(InvalidOption)

        if quizOption == 'h':
            supplies.tokens -= 1
            print(vocabOptionList[ansNum][example])
        elif int(quizOption) == ansNum + 1:
            knowledgeGained = random.randint(50, 200)
            print(Fore.GREEN + f'That was the right answer! Congrats! You earned ' + Fore.CYAN + f'{knowledgeGained}' + Fore.GREEN + ' knowledge!' + Fore.RESET)
            break
        else: 
            print(Fore.RED + f'That was not the right answer!' + Fore.RESET)
            break



def main():
    global InvalidOption
    global Wait
    global SelectedLesson
    InvalidOption = 'Please selection a available option: '
    Wait = True
    SelectedLesson = [1]
    character = Characters()
    supplies = Supplies()
    date = Date()


    while True:
        Menu(character, supplies, date)
    


if __name__ == "__main__":
    main()