# Guess Number clumsy version
# by robin
# @2019/09/09

for guess in range(1, 11):
    answer = raw_input("Is your number "+ str(guess) + "- yes or no?")
    while answer != "yes" and answer != "no":
        answer = raw_input("Is your number "+ str(guess) +"- yes or no?")
    if answer == "yes":
        print "I gussed the number!"
        break
if answer == "no":
    print "You're lying!"
