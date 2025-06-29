print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "Control Processing Unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "Random Access Memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does HTML stand for? ")
if answer.lower() == "Hypertext Markup Language":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does IP stand for? ")
if answer.lower() == "Internet Protocol":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does LAN stand for? ")
if answer.lower() == "Local Area Network":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")