import random
import re

def gen_question(cat):
    """
    cat: contains the category specified by the user
    politics_quest, entertainment_quest, sports_quest: is a dictionary of the questions in each category
    quest, answer: contains randomly generated questions and its corresponding answer
    user_answer: takes in the answer of the user to the generated question
    second_chance: allows user change answer if unsure
    """
    

    politics_quest = {"How many local governments are in Nigeria?": 
                      ["(A) 774","(B) 750", "(C) 420", "(D) 600", "Ans: A"],

                    "Nigerian's current constitution was written in what year?": 
                    ["(A) 1973", "(B) 1999", "(C) 1927", "(D) 1989", "Ans: B"],

                    "What is the lowest possible political office in Nigeria": 
                    ["(A) Ward councillor", "(B) Local Government Chairman", "(C) Youth Leader", "(D) Party Chairman", "Ans: A"],

                    "Who is the current President of Nigeria?": 
                    ["(A) Nnamdi Azikiwe", "(B) Kashim Shettima","(C) Bola Ahmed Tinubu", "(D) Muhammadu Buhari", "Ans: C"],

                    "Who is the current Senate President of Nigeria?":
                    ["(A) Ahmad Lawan","(B) Abubakar Bukola Saraki", "(C) Ibrahim Gobir","(D) Godswill Akpabio", "Ans: D"],

                    "What year did the End SARS protest occur?": 
                    ["(A) 2020", "(B) 2021", "(C) 1920", "(D) 2022", "Ans: B"],}  
    
    entertainment_quest = {"Tiwa Savage was married to which popular entertainment manager?": 
                           ["(A) Bizzle", "(B) Tee Billz", "(C) Asa Asika", "(D) Johnny Drille", "Ans: A"],

                            "Funke Akindele came into limelight after starring in which 90s sitcom?": 
                            ["(A) Jenifa", "(B) Jenifa's Diary", "(C) Omo Ghetto","(D) I Need To Know", "Ans: D"],

                            "What is Pasuma's nickname?": 
                            ["(A) Ogaranya","(B) Oganla One", "(C) Mr Paso Wonder", "(D) O.B.O", "Ans: B"],

                            "What character did Reminisce play in King of Boys?": 
                            ["(A) Alagba Ibile", "(B) Scorpion","(C) Makanaki", "(D) Oga At The Top", "Ans: C"],

                            "What Netflix movie does Temi Otedola star in?":
                              ["(A) Citation", "(B) October 1st", "(C) The Figurine", "(D) Wedding Party", "Ans: A"],

                            "What's the name of Wizkid's clothing line?": 
                            ["(A) Wizzy Baby","(B) Star Boy", "(C) Smile Clothings", "(D) Gucci", "Ans: B"]
                            }
    
    sports_quest = {"The Olympics are held every how many years?": 
                    ["(A) 4 years", "(B) 3 years", "(C) 20 years", "(D) 10 years", "Ans: A"],

                    "What sport is best known as the 'king of sports'?": 
                    ["(A) Basketball", "(B) Tennis", "(C) Soccer", "(D) Long jump", "Ans: C"],

                    "According to the official FIFA rulebook, how long can a goalkeeper hold the ball?": 
                    ["(A) 4 seconds", "(B) 1 min", "(C) 12 seconds","(D)6 seconds", "Ans: D"],

                    "Premier League club Liverpool is also known by which nickname?": 
                    ["(A) Blue", "(B) Gunners","(C) Eagles","(D) Red", "Ans: D"],

                    "How many players are in a football team?": 
                    ["(A) 6 players", "(B) 11 players", "(C) 13 players", "(D) 5 players", "Ans: B"],
                    
                    "What is the Nigerian Male Football team called?": 
                    ["(A) The Falcon", "(B) Super Eagles", "(C) The Kitten", "(D) Red Devils", "Ans: B"]
                    }
    
    if cat == "Politics":
        quest, options = random.choice(list(politics_quest.items()))
    elif cat == "Sports":
        quest, options = random.choice(list(sports_quest.items()))
    else:
        quest, options = random.choice(list(entertainment_quest.items()))
    
    return quest, options


def validate_answer(quest, options):
    while True:
        print(quest)
        for i in options:
            if options.index(i) == 4:
                continue
            else:
                print(i)
        user_answer = input().upper()
        second_chance = input("Is that your final answer: ").lower().strip()
        if user_answer == options[-1][-1] and second_chance == "yes":
            print("You are correct")
            return 1
        elif second_chance == "no":
            continue
        else:
            print("You are wrong")
            return 0


def collate_score(score):
    """
    Calculates the score of the user
    """

    total = 0
    for i in score:
        total += i
    return total


def qualifiers_file(qualifier):
    """
    writes qualifier's name to the text file, qualifiers.txt
    """

    with open("qualifiers.txt", "a") as file:
        file.write(qualifier+"\n")


def display_qualifiers():
    """
    displays the qualifiers in the qualifiers.txt file to the user
    """

    with open("qualifiers.txt") as file:
        for line in file:
            line = line.rstrip()
            print(line)


def rules(name):
    """
    prints out the rules of the game

    :param name: holds the name of the user
    """

    print(f"""-------------------------------------------------------------------------------
Welcome {name}! This is a Trivia game on Nigerian politics, football and sports. 
You have three questions to attempt, one from each category. If you get all three, you qualify 
to be a contestant in the main competition. NOTE: you can't answer more than one question from 
each category
---------------------------------------------------------------------------------------------
""")


def main():
    """
    categories: a tuple that contains the various categories of the game
    cat_attempted: is a list that keeps the category attempted by the user. 
                    It checks against reanswering categories already attempted
    quest_answered: keeps account of how many questions the user has answered
    scores: a list that keeps the score of the user
    user_name: holds the name of the user
    total_score: stores the collated score

    """
    
    categories = ("Politics", "Entertainment", "Sports")
    cat_attempted = []
    quest_answered = 0
    scores = []
    while True:
        user_name = input("Username: ").capitalize().strip()
        if re.search(r"[A-za-z]+", user_name) and len(user_name) > 2:
            break
        else:
            print("Invalid username")
    rules(user_name)
    while quest_answered < 3:
        print("To begin input either one of the three categories(Politics, Entertainment, Sports)")
        category = input().capitalize().strip()
        if category in categories:
            if category not in cat_attempted:
                quest, options = gen_question(category)
                score = validate_answer(quest, options)
                quest_answered += 1 
                cat_attempted.append(category)
                scores.append(score)
            else:
                print("Category has been chosen")
        else:
            print("Invalid category")
    total_score = collate_score(scores)
    print(total_score)
    if total_score == 3:
        print("You have qualified")
        qualifiers_file(user_name)
    else: 
        print("You are disqualified")
    display_qualifiers()

if __name__ == "__main__":
    main()







    
