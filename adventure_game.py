def print_sleep(msg, num):
    import time
    print(msg)
    time.sleep(num)


def intro():
    print_sleep("You will play a educational game against your enemy", 1)
    print_sleep("5 questions will be asked in the category", 1)
    print_sleep("If you get more than 80% of questions correct, "
                "you'll have a chance to roll a dice", 1)
    print_sleep("If your dice returns number between 2 and 6, "
                "you win. Otherwise you loose", 1)
    print_sleep("If you score less than 80%, you still "
                "have a chance to win", 1)
    print_sleep("You and your enemy will roll a dice. If your number "
                "is bigger than enemy's, you win", 1)
    print_sleep("Good luck with the game", 1)


def rollDice():
    import random
    return random.randint(1, 6)


def findIfYouWon(count):
    if (count > 3):
        print_sleep("Rolling Dice", 1)
        num = rollDice()
        print_sleep("Your number is " + str(num), 1)
        if (num == 1):
            print_sleep("You Lost! Bad Luck.", 1)
        else:
            print_sleep("You won with good Luck", 1)
    else:
        print_sleep("Rolling your Dice", 1)
        num = rollDice()
        print_sleep("Your number is " + str(num), 1)
        print_sleep("Rolling your enemy's dice", 1)
        num2 = rollDice()
        print_sleep("The number is " + str(num2), 1)
        if (num > num2 + 1):
            print_sleep("You won. Lucky you!", 1)
        else:
            print_sleep("Well, you lost. Don't depend"
                        "on luck to win. Study!", 1)


def playJava():
    count = 0
    questions = ['In an instance method or a constructor, ' +
                 '"this" is a reference to the current object',
                 'The modifiers public and static cannot written ' +
                 'in either order "public static" or "static public".',
                 'Variable name can begin with a letter, "$", or "_".',
                 'Assignment operator is evaluated Left to Right.',
                 'A .class file contains bytecodes?',
                 'Constructor overloading is not possible in Java',
                 'All binary operators except for the ' +
                 'assignment operators are evaluated from Left to Right',
                 'Garbage Collection is manual process',
                 'Class can inherit only one class',
                 'Interfaces can be instantiated',
                 'James Gosling is father of Java?']
    print_sleep("This game will test your knowledge in Java programming", 1)
    print_sleep("Now let's start", 1)
    print_sleep("This is a true false question type 'T' or 't' for" +
                "true and 'F' or 'f' for false", 1)
    count = askQuestion(questions)
    print(count)
    findIfYouWon(count)
    playAgain()


def askQuestion(questions):
    import random
    count = 0
    for i in range(5):
        qIndex = random.randint(0, len(questions) - 1)
        ans = input(questions[qIndex] + ": ")
        while ans != 'T' and ans != 'F' and ans != 't' and ans != 'f':
            ans = input("This is a true false question: type 'T' or 't' " +
                        "for true and 'F' or 'f' for false: ")
        if qIndex % 2 == 0 and (ans == "T" or ans == "t"):
            count += 1
        elif qIndex % 2 == 1 and (ans == "F" or ans == "f"):
            count += 1
    return count


def playAgain():
    ans = input("Do you want to play again? Type: 'Y' or 'N' :")
    if "y" == ans or "Y" == ans:
        playJava()
    else:
        if "N" == ans or "n" == ans:
            print_sleep("Bye, bye", 1)
        else:
            print_sleep("Invalid response", 1)
            playAgain()


def playgame():
    intro()
    playJava()


playgame()
