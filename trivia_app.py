import random

def gen_question(cat):
        """
        cat: contains the category specified by the user
        politics_quest, entertainment_quest, sports_quest: is a dictionary of the questions in each category
        quest, answer: contains randomly generated questions and its corresponding answer
        user_answer: takes in the answer of the user to the generated question
        second_chance: allows user change answer if unsure
        """
        

        politics_quest = {"Who is the current President of Nigeria?": "bola ahmed tinubu",
                    "Who is the current Senate President of Nigeria?": "godswill akpabio",
                    "What year did the End SARS protest occur?": "2021",
                    "How many local governments are in Nigeria?": "774",
                    "Nigerian's current constitution was written in what year?": "1999",
                    "What is the lowest possible political office in Nigeria": "ward council"}  
        entertainment_quest = {"Tiwa Savage was married to which popular entertainment manager?": "bizzle",
                               "Funke Akindele came into limelight after starring in which 90s sitcom?": "i need to know",
                               "What is Pasuma's nickname?": "oganla one",
                               "What character did Reminisce play in King of Boys?": "makanaki",
                               "What Netflix movie does Temi Otedola star in?": "citation",
                               "What's the name of Wizkid's clothing line?": "star boy"
                               }
        sports_quest = {"The Olympics are held every how many years?": "4 years",
                        "What sport is best known as the 'king of sports'?": "soccer",
                        "Who has won more tennis grand slam titles, Venus Williams or Serena Williams?": "serena williams",
                        "According to the official FIFA rulebook, how long can a goalkeeper hold the ball?": "6 seconds",
                        "Premier League club Liverpool is also known by which nickname?": "red",
                        "Who is the only soccer player in history to win five FIFA Ballons d'OR?": "lionel messi"}
        if cat == "Politics":
            quest, answer = random.choice(list(politics_quest.items()))
        elif cat == "Sports":
            quest, answer = random.choice(list(sports_quest.items()))
        else:
            quest, answer = random.choice(list(entertainment_quest.items()))
        while True:
            user_answer = input(quest+": ").lower().strip()
            second_chance = input("Is that your final answer: ").lower().strip()
            if user_answer == answer and second_chance == "yes":
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
    user_name = input("Username: ").capitalize().strip()
    rules(user_name)
    while quest_answered < 3:
        print("To begin input either one of the three categories(Politics, Entertainment, Sports)")
        category = input().capitalize().strip()
        if category in categories:
            if category not in cat_attempted:
                score = gen_question(category)
                quest_answered += 1 
                cat_attempted.append(category)
                scores.append(score)
            else:
                print("Category has been chosen")
                break
        else:
            print("Invalid category")
            break
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







    