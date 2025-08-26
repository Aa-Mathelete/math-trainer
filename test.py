# Math Trainer Lite for TI-84 Plus CE Python
# Simplified: Addition practice only

import random

def addition_practice():
    score = 0
    for i in range(5):  # 5 questions
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = int(input(str(a) + " + " + str(b) + " = "))
        if answer == a + b:
            print("Correct!")
            score += 1
        else:
            print("Wrong. The answer is", a + b)
    print("You got", score, "out of 5 correct.")

def main():
    while True:
        print("\n--- Math Trainer Lite ---")
        print("1. Addition Practice")
        print("2. Quit")
        choice = input("Choose: ")
        if choice == "1":
            addition_practice()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
# Math Trainer Lite for TI-84 Plus CE Python
# Simplified: Addition practice only

import random

def addition_practice():
    score = 0
    for i in range(5):  # 5 questions
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = int(input(str(a) + " + " + str(b) + " = "))
        if answer == a + b:
            print("Correct!")
            score += 1
        else:
            print("Wrong. The answer is", a + b)
    print("You got", score, "out of 5 correct.")

def main():
    while True:
        print("\n--- Math Trainer Lite ---")
        print("1. Addition Practice")
        print("2. Quit")
        choice = input("Choose: ")
        if choice == "1":
            addition_practice()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
