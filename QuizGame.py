#python mini project_1 _QuizGame (:
print("Welcome to my computer quiz!")

playing = input("Do you want to play?")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :) ")
score=0
answer = input("What does CPU stand for? ".lower())
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
print("You got" + " " + str(score) + "question correct!")
print("You got" + " " + str((score/2) *100) + "%.")



