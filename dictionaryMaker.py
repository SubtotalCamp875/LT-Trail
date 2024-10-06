import random

les1 = {
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
    10: ["Meticulous", "adj", "extremely, sometimes excessively, carefule about small details; precise", "With meticulous care', he crafted a miniature dollhouse for his daughter."],
    11: ["Temerity", "n", "recklessness; a foolish disregurd of danger", "I couldn't believe that Bret had the temerity to bungee jump over a lake full of alligators."],
    12: ["Rote", "n", "a habitual repetitive routine or procedure", "Kristan memorized the piano sonata through rote, by practiciing the song over and over until she could play it perfectly."],
    13: ["Ascribe", "v", "to credit as to the cuase or the source", "The carpenter ascribed the rotten floorboards to a leaky roof."],
    14: ["Gregarious", "adj", "sociable; fond of the company of others", "Just before he was diagnosed with clinical depression, Raji went from being gregarious to being anitsocial."],
}

wordList = [

'Divulge',
'Abet',
'Ardor',
'Dogmatic',
'Insipid',
'Proclivity',
'Extraneous',
'Coerce',
'Jaundiced',
'Occlude',
'Meticulous',
'Temerity',
'Rote',
'Ascribe',
'Gregarious',

]
speechList = [

'v',
'v',
'n',
'adj',
'adj',
'n',
'adj',
'v',
'adj',
'v',
'adj',
'n',
'n',
'v',
'adj',

]
defList = [

'to tell; to reveal (as a secret)',
'to assist or encourage, especially in wrongdoing',
'an intense feeling of devotion or eagerness',
'arrogant and stubborn about one\'s beliefs',
'lacking favor; dull; not at all simulating',
'a natural leaning or tendency',
'not essentail; not constituing a vital part',
'to force by using presssure, intimadation, or threats',
'prejudice; hostile',
'to block the passage of',
'extremely, sometimes excessively, carefule about small details; precise',
'recklessness; a foolish disregurd of danger',
'a habitual repetitive routine or procedure',
'to credit as to the cuase or the source',
'sociable; fond of the company of others',

]
exList = [

'The reporter was fired when she divulged information from a classified document.',
'Jim refused to abet the criminal\'s escape by hiding him in the basement.',
'The defending troops fought with ardor ebcause the emeny would not be taking any prisoners.',
'Beause of the professer\'s dogmatic approach, the students were afraid to ask questions.',
'My mom wanted me to be an accountant, but I found the classes boring and insipid.',
'Abigail\'s procivility for history led her to write a book on the founders of her home town.',
'The professor felt that the extraneous paragraph in the essay detracted from the more important infomation.',
'Jerry preferred basketball\', but ihs father coerced him into palying football.',
'Gabe had jaunduced view of Iraq after losing his wife in the Gulf War.',
'A large mass of clay occuleded the water pipe, causing a dangerous rise in pressure.',
'With meticulous care\', he crafted a miniature dollhouse for his daughter.',
'I couldn\'t believe that Bret had the temerity to bungee jump over a lake full of alligators.',
'Kristan memorized the piano sonata through rote, by practiciing the song over and over until she could play it perfectly.',
'The carpenter ascribed the rotten floorboards to a leaky roof.',
'Just before he was diagnosed with clinical depression, Raji went from being gregarious to being anitsocial.',

]

for i in range(len(wordList)):
    print(f'{i}: ["{wordList[i]}", "{speechList[i]}", "{defList[i]}", "{exList[i]}"],')