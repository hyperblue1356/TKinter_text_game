# TO DO:

# Fix user race choice

# Change questions to appear as coming from Honour
# Turn into adventure game??
# Create further stats
# Create function so user can check their stats, items, health
# Create function so questions appear as if they are being typed one letter at a time.

import time

def ask_question(question_no):
    """ Function to ask player specific questions"""

    questionsdict = {1: "I am the remnants of Honour, What is your name?",
                     2: "What is your age?",
                     3: "Choose a race you would like to know more about",
                     4: "Would you like to know about another race?: ",
                     5: "What race are you?: ",
                     6: "Choose an order you would like to know more about: ",
                     7: "Would you like to know about another order?: ",
                     8: "What order are you?: ",
                     }
    for char in questionsdict[question_no]:
        print(char, end="")
        time.sleep(0.1)


races_russian = {"алехи": "Высокий, загар кожи, быстый и умный. алехи не мирны, они воины,"
                          " светлые глаза и темные глаза и валосы ",

                 "видень": "светлая кожа, рыжие волосы, светлые глаза и темные глаза",

                 "ункалаки": "светлая загорелая кожаб рыжие волосы, Высокий"}

races_english = {"Alethi": "Common features- tall stature, tan skin, black hair, lighteyes and darkeyes.",

                 "Veden": "Common features- fair skin, red hair, lighteyes and darkeyes",

                 "Unkalaki": "Common features: light tan skin (or just fair skin like the Vedens,"
                             " supposedly lighter than the Alethi), "
                             "red hair, strong back molars to break shells and claws (result of Parshendi hybrids"}


knights_radiant_eng = {"Windrunners": "Exemplify the virtues of Protection and Leading. "
                                      "Their Surges are Adhesion and Gravitation.",

                       "Skybreakers": "Exemplify the virtues of Law and Justice."
                                      " Their Surges are Gravitation and Division",

                       "Dustbringers": "Their Surges are Division and Abrasion",

                       "Edgedancers": "Their Surges are Abrasion and Progression",

                       "Truthwatchers": " Their Surges are Progression and Illumination.",

                       "Lightweavers": "Their Surges are Illumination and Transformation.",

                       "Elsecallers": "Their Surges are Transformation and Transportation.",

                       "Willshapers": "Their Surges are Transportation and Cohesion.",

                       "Stonewards": "Their Surges are Cohesion and Tension.",

                       "Bondsmiths":  "Their Surges are Tension and Adhesion"}


player_info_eng = ()

# Race classes

class Veden:

    def __init__(self, common_features):
        self.common_features = common_features

    def race_info(self):
        return "{}".format(self.common_features)


race_2 = Veden("Common features- fair skin, red hair, lighteyes and darkeyes")

race_2.race_info()


class Unkalaki:

    def __init__(self, common_features):
        self.common_features = common_features

    def race_info(self):
        return "{}".format(self.common_features)


race_3 = Unkalaki("Common features:"
                  " light tan skin (or just fair skin like the Vedens)"
                  " (supposedly lighter than the Alethi), red hair, strong back molars to break shells and claws"
                  " (result of Parshendi hybrids)".casefold())

race_3.race_info()


class Alethi:

    def __init__(self, common_features):
        self.common_features = common_features

    def race_info(self):
        return "{}".format(self.common_features)


race_1 = Alethi("Common features- tall stature, tan skin, black hair, lighteyes and darkeyes.")

race_1.race_info()


# Radiant classes


class Windrunner:

    def __init__(self, radiant_order, atributes, abilities):
        self.radiant_order = radiant_order
        self.atributes = atributes
        self.abilities = abilities
        self.all = radiant_order + "," + atributes + "," + abilities

    def radiant_info(self):
        return "{} {} {}".format(self.radiant_order, self.atributes, self.abilities)


radiant_1 = Windrunner("windrunner:", "Exemplify the virtues of Protection and Leading.",
                       "Their Surges are Adhesion and Gravitation.")

radiant_1.radiant_info()


class Skybreaker:

    def __init__(self, radiant_order, atributes, abilities):
        self.radiant_order = radiant_order
        self.atributes = atributes
        self.abilities = abilities
        self.all = radiant_order + "," + atributes + "," + abilities

    def radiant_info(self):
        return "{} {} {}".format(self.radiant_order, self.atributes, self.abilities)


radiant_2 = Skybreaker("Skybreaker: ", "Exemplify the virtues of Law and Justice. ",
                       "Their Surges are Gravitation and Division")

radiant_2.radiant_info()


class Dustbringer:

    def __init__(self, radiant_order, atributes, abilities):
        self.radiant_order = radiant_order
        self.atributes = atributes
        self.abilities = abilities
        self.all = radiant_order + "," + atributes + "," + abilities

    def radiant_info(self):
        return "{} {} {}".format(self.radiant_order, self.atributes, self.abilities)


radiant_3 = Dustbringer("dustbringer: ", "virtues unknown. ", "Their Surges are Division and Abrasion")

radiant_3.radiant_info()

user_race_eng = ()

user_order_eng = ()


class Edgedancer:

    def __init__(self, radiant_order, attributes, abilities):
        self.radiant_order = radiant_order
        self.attributes = attributes
        self.abilities = abilities
        self.all = radiant_order + "," + attributes + "," + abilities

    def radiant_info(self):
        return "{} {} {}".format(self.radiant_order, self.attributes, self.abilities)


radiant_4 = Edgedancer("Edgedancers: ", "virtues unknown. ", "Their Surges are Abrasion and Progression")

radiant_4.radiant_info()


class Truthwatcher:

    def __init__(self, radiant_order, atributes, abilities):
        self.radiant_order = radiant_order
        self.atributes = atributes
        self.abilities = abilities
        self.all = radiant_order + "," + atributes + "," + abilities

    def radiant_info(self):
        return "{} {} {}".format(self.radiant_order, self.atributes, self.abilities)


radiant_5 = Truthwatcher("Truthwatcher: ", "Virtues unknown.", "Their Surges are Progression and Illumination.")

radiant_5.radiant_info()


class Lightweaver:

    def __init__(self, radiant_order, attributes, abilities):
        self.radiant_order = radiant_order
        self.attributes = attributes
        self.abilities = abilities
        self.all = radiant_order + "," + attributes + "," + abilities

    def radiant_info(self):
        return "{} {} {}".format(self.radiant_order, self.attributes, self.abilities)


radiant_6 = Lightweaver("Lightweaver: ", "Virtues unknown", "Their Surges are Illumination and Transformation.")

radiant_6.radiant_info()


class Elsecaller:

    def __init__(self, radiant_order, attributes, abilities):
        self.radiant_order = radiant_order
        self.attributes = attributes
        self.abilities = abilities
        self.all = radiant_order + "," + attributes + "," + abilities

    def radiant_info(self):
        return "{} {} {}".format(self.radiant_order, self.attributes, self.abilities)


radiant_7 = Elsecaller("Lightweaver: ", "Virtues unknown", "Their Surges are Transformation and Transportation.")

radiant_7.radiant_info()


class Willshaper:

    def __init__(self, radiant_order, attributes, abilities):
        self.radiant_order = radiant_order
        self.attributes = attributes
        self.abilities = abilities
        self.all = radiant_order + "," + attributes + "," + abilities

    def radiant_info(self):
        return "{} {} {}".format(self.radiant_order, self.attributes, self.abilities)


radiant_8 = Willshaper("Willshaper: ", "Virtues unknown.", "Their Surges are Transportation and Cohesion.")
radiant_8.radiant_info()


class Stoneward:

    def __init__(self, radiant_order, attributes, abilities):
        self.radiant_order = radiant_order
        self.attributes = attributes
        self.abilities = abilities
        self.all = radiant_order + "," + attributes + "," + abilities

    def radiant_info(self):
        return "{} {} {}".format(self.radiant_order, self.attributes, self.abilities)


radiant_9 = Stoneward("Stoneward: ", "Virtues unknown.", "Their Surges are Cohesion and Tension.")

radiant_9.radiant_info()


class Bondsmith:

    def __init__(self, radiant_order, attributes, abilities):
        self.radiant_order = radiant_order
        self.attributes = attributes
        self.abilities = abilities
        self.all = radiant_order + "," + attributes + "," + abilities

    def radiant_info(self):
        return "{} {} {}".format(self.radiant_order, self.attributes, self.abilities)


radiant_10 = Bondsmith("Bondsmith: ", "Virtues unknown.", "Their Surges are Tension and Adhesion")

radiant_10.radiant_info()



# example of how could be stored in dictionARY??

# locations = {0: {"desc": "You are sitting in front of a computer learning Python",
#                  "exits": {},
#                  "namedExits": {}},
#              1: {"desc": "You are standing at the end of a road before a small brick building",
#                  "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#                  "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
#              2: {"desc": "You are at the top of a hill",
#                  "exits": {"N": 5, "Q": 0},
#                  "namedExits": {"5": 5}},
#              3: {"desc": "You are inside a building, a well house for a small stream",
#                  "exits": {"W": 1, "Q": 0},
#                  "namedExits": {"1": 1}},
#              4: {"desc": "You are in a valley beside a stream",
#                  "exits": {"N": 1, "W": 2, "Q": 0},
#                  "namedExits": {"1": 1, "2": 2}},
#              5: {"desc": "You are in the forest",
#                  "exits": {"W": 2, "S": 1, "Q": 0},
#                  "namedExits": {"2": 2, "1": 1}}
#              }

languages = "Russian (Руский)", "English (Англиский)", "R", "Р", "E", "А"
lang_choice = ""
while lang_choice not in languages:
    lang_choice = input("Enter 'R' for Russian or 'E' for English (введите 'Р' для русского или 'A' для английского)")

    if lang_choice == "R" or lang_choice == "Р":
        print("вы играете на русском")  #"You are playing in Russian"
        break
    elif lang_choice == "E" or lang_choice == "А":
        print("You are playing in English")
        time.sleep(1)
        break
    else:
        print("please pick a language")

user_race_rus = ()
player_info_eng = ["Stats: "]

ask_question(1)

player_name = input("").upper()
player_info_eng.append(player_name)

print("\n")

ask_question(2)

player_age = input("")
player_info_eng.append(player_age)


print("Races: ")
print(*races_english, sep=", ")

# Language choice and Russian race choice

while lang_choice == "R" or languages == "Р":
    user_race_rus = input("выберите расу, чтобы узнать о них больше: ")# "Choose a race you would like to
    # know more about"
    if user_race_rus in races_russian and user_race_rus == "алехи" or user_race_rus == "ункалаки":
        print("вы {0}".format(user_race_rus))
        description = races_russian.get(user_race_rus, "Вы ")
        print(description)
    elif user_race_rus == "ведень":
        print("Вы видень")
    else:
        print("Кто ты?")
    break

while lang_choice == "E":
    user_race_eng_repeat = input("Choose a race you would like to know more about: ").upper()
    time.sleep(1)
    if "ALETHI" in user_race_eng_repeat:
        print(race_1.race_info())
    elif "VEDEN" in user_race_eng_repeat:
        print(race_2.race_info())
    elif "UNKALAKI" in user_race_eng_repeat:
        print(race_3.race_info())
        time.sleep(1)
    more_info = input("Would you like to know about another race?: ")
    time.sleep(1)
    if "no" in more_info:
        user_race_eng = input("What race are you?: ").upper()
        time.sleep(1)
        player_info_eng.append(user_race_eng)
        break
    else:
        print("That is not a race")


while lang_choice == "E":
    print("Knights orders: ")
    for key, value in knights_radiant_eng.items():
        print("{}".format(key))
    user_order_eng = input("Choose an order you would like to know more about: ").upper()
    time.sleep(1)

    if "WINDRUNNER" in user_order_eng:
        print(radiant_1.radiant_info())
    elif "SKYBREAKER" in user_order_eng:
        print(radiant_2.radiant_info())
    elif "DUSTBRINGER" in user_order_eng:
        print(radiant_3.radiant_info())
    elif "EDGEDANCER" in user_order_eng:
        print(radiant_4.radiant_info())
    elif "TRUTHWATCHER" in user_order_eng:
        print(radiant_5.radiant_info())
    elif "LIGHTWEAVER" in user_order_eng:
        print(radiant_6.radiant_info())
    elif "ELSECALLER" in user_order_eng:
        print(radiant_7.radiant_info())
    elif "WILLSHAPER" in user_order_eng:
        print(radiant_8.radiant_info())
    elif "STONEWARD" in user_order_eng:
        print(radiant_9.radiant_info())
    elif "BONDSMITH" in user_order_eng:
        print(radiant_10.radiant_info())
    more_info = input("Would you like to know about another order?: ")
    time.sleep(1)
    if "no" in more_info:
        user_race_eng = input("What order are you?: ").upper()
        time.sleep(1)
        player_info_eng.append(user_order_eng)
        break

print(*player_info_eng, sep=", ".upper())