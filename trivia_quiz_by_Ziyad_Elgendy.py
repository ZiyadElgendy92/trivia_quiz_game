#IPND stage 2 project (code your own quiz), submitted by Ziyad Elgendy.

#blank elements.
blanks= [ "__1__",  "__2__", "__3__", "__4__"]

#level strings and answers lists.
level_easy="Einstein is one of the most famous __1__ of all time. His work on theoretical __2__ live on today and he serves as an inspiration to young scientists around the world. He produced perhaps one of the most famous equations ever: E = mc^2 __3__ equals mass multiplied by the speed of __4__ squared."
answer_easy=["scientists", "physics", "energy", "light"]

level_medium="The __1__ is Earth's only natural satellite. it's __2__ is only about one fifth (17%) as strong as it is on Earth. The NASA __3__ 11 mission in 1969 was the first manned Moon landing. the first person to set foot on the Moon was Neil __4__."
answer_medium=["Moon", "gravity", "Apollo", "Armstrong"]

level_hard="__1__ is the first element on the periodic table, it is highly flammable and is the most common element found in our universe. \n__2__ comes in a number of different forms (allotropes), these include diamond, graphite and impure forms such as coal. \n__3__ is an element with the chemical symbol O and atomic number 8, it is essential to human life, it is found in the air we breathe and the water we drink. \n__4__ is a chemical element with the symbol He and atomic number 2, because it is lighter than air it is commonly used to fill airships, blimps and balloons. As it doesn't burn or react with other chemicals, it is relatively safe to use for this purpose."
answer_hard=["Hydrogen", "Carbon", "Oxygen", "Helium"]

#levels parameters initial values.
counter=0
wrong_answers=0
trials=5

#the play_game procedure takes in the level paragraph, the blanks list and the answers list and runs the game, then it  returns the paragraph with the correct answers when typed in correctly and returns "Game Over!" if 5 wrong answers are typed in for one blank.
def play_game(level, blanks, answer, counter, wrong_answers, trials):
    level_list=level.split()
    for word in level_list:
        replacement =blank_replace(word, blanks)
        if replacement != None:
            print "\n"+level
            user_input=raw_input("\n what should go in blank "+replacement+"? :")
            while user_input!=answer[counter]:
                wrong_answers+=1
                if wrong_answers==trials:
                    return "\n Game Over!"
                else:
                    print "\n wrong answer! you have "+str (trials-wrong_answers)+" trial(s) left \n"+level
                    user_input=raw_input("\n what should go in blank "+replacement+"? :")
            if user_input==answer[counter]:
                print "\n that's correct!"
                level=level.replace(replacement,user_input)
                counter+=1
                wrong_answers=0
    return "\n"+level+ "\n\ncongratulations! you have completed the QUIZ."
    
#the blank_replace procedure takes in a word from the problem paragraph and a blank element from the blanks list and returns the blank to be replaced if the word is a blank, if  the word isn't a blank then it returns None.
def blank_replace(word, blanks):
    for blank in blanks:
        if blank in word:
            return blank
    return None
 
#the start procedure runs the game according to chosen difficulty. 
def start():  
    print "Welcome to the QUIZ!\nyou will have 5 trials for each answer, type in your answers to proceed "
    difficulty=raw_input("select difficulty (easy, medium, hard):")
    while difficulty not in ("easy", "medium", "hard"): 
        print"that wasn't a valid answer"
        difficulty=raw_input("select difficulty to start (easy, medium, hard):")
    if difficulty =="easy":
        print play_game(level_easy, blanks, answer_easy,  counter, wrong_answers, trials)
    elif difficulty =="medium":
        print play_game(level_medium, blanks, answer_medium,  counter, wrong_answers, trials)
    elif difficulty =="hard":
        print play_game(level_hard, blanks, answer_hard,  counter, wrong_answers, trials) 
        
start()