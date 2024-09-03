import time


def quiz():
    print("𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓽𝓱𝓮 𝓺𝓾𝓲𝔃👋")
    print(" ")#To add extra line
    time.sleep(1)#To give the user some time before reading to read the line above

    print("In this game you are going to play general questions about Ethiopia.")
    print(" ")
    time.sleep(3)

    print("There are going to be 4 questions. Inorder to win you need to score at least half.")
    print(" ")
    time.sleep(3)

    print("𝓖𝓸𝓸𝓭 𝓛𝓾𝓬𝓴✨")
    print(" ")

    points=0#A variable that is used to count the number of points the user got by answering the quiz questions
    actual_answer1="africa"
    user_answer1=input("Where is Ethiopia located?")

    if user_answer1.lower()==actual_answer1:#used to check  if the answer the user entered is the same as the actual answer
        points=points+1#adds ppoint if the answer is correct
        print("Correct")
    else:
        print("Incorrect you lose 1 pt for this question")

    print(" ")
    actual_answer2="addis ababa"
    user_answer2=input("What is the capital city of Ethiopia?")
    if user_answer2.lower()==actual_answer2:
        points=points+1
        print("Correct")
    else:
        print("Incorrect you lose 1 pt for this question")


    print(" ")
    actual_answer3="injera"
    user_answer3=input("What is the widely eaten food in Ethiopia?")
    if user_answer3.lower()==actual_answer3:
        points=points+1
        print("Correct")
    else:
        print("Incorrect you lose 1 pt for this question")



    print(" ")
    actual_answer4="au"
    user_answer4=input("Which continental organization is located in Ethiopias capital city?")
    if user_answer4.lower()==actual_answer4:
        points=points+1
        print("Correct")
    else:
        print("Incorrect you lose 1 pt for this question")
    
    print(" ")
    if points>=2:#Checks if the user has at least answered two questions correctly and if so it will declare the user as winner else as loser.
        print(f"You won!You have scored {points} out of 4.")
    else:
        print(f"You lost!You have scored {points} out of 4.")



def main():


    quiz()


main()