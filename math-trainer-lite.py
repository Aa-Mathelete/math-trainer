# Math Trainer Lite (TI-84 Plus CE Python Compatible)
# Covers 6 levels: basic math, multiplication/division,
# logs/exponents, trig, AMC-style word problems, quadratics
## THIS VERSION WILL WORK ON MOST CALCULATORS

import random
import math

# ----- Level Generators -----

def level1():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    if random.choice([0,1]) == 0:
        return str(a) + " + " + str(b), a + b
    else:
        return str(a) + " - " + str(b), a - b

def level2():
    if random.choice([0,1]) == 0:
        a = random.randint(2,12)
        b = random.randint(2,12)
        return str(a) + " x " + str(b), a * b
    else:
        b = random.randint(2,12)
        ans = random.randint(2,12)
        a = b * ans
        return str(a) + " ÷ " + str(b), ans

def level3():
    if random.choice([0,1]) == 0:
        base = random.randint(2,5)
        exp = random.randint(2,4)
        return str(base) + "^" + str(exp), base ** exp
    else:
        base = random.randint(2,4)
        exp = random.randint(2,4)
        return "log_" + str(base) + "(" + str(base**exp) + ")", exp

def level4():
    choice = random.choice([0,1,2])
    if choice == 0:
        deg = random.choice([30,45,60,90,180])
        return "Convert " + str(deg) + "° to rad", round(deg*math.pi/180,3)
    elif choice == 1:
        rad = random.choice([math.pi/6, math.pi/4, math.pi/3, math.pi/2, math.pi])
        return "Convert " + str(rad) + " rad to °", round(rad*180/math.pi)
    else:
        ang = random.choice([0,30,45,60,90])
        func = random.choice(["sin","cos","tan"])
        if func=="sin": ans=round(math.sin(math.radians(ang)),3)
        elif func=="cos": ans=round(math.cos(math.radians(ang)),3)
        else: ans=round(math.tan(math.radians(ang)),3)
        return func + "(" + str(ang) + "°)", ans

def level5():
    problems = [
        ("If 15% of a number is 45, what is the number?",300),
        ("What is 25% of 80?",20),
        ("If 3x + 7 = 22, what is x?",5),
        ("Area of a square with side 6?",36),
        ("If 2/3 of a number is 18, what is the number?",27),
    ]
    q,a = random.choice(problems)
    return q,a

def level6():
    problems = [
        ("x^2 - 5x + 6 = 0", [2,3]),
        ("x^2 - 7x + 12 = 0", [3,4]),
        ("x^2 + 5x + 6 = 0", [-2,-3]),
        ("x^2 - 9 = 0", [3,-3]),
        ("x^2 - 4x + 4 = 0", [2,2])
    ]
    q,roots = random.choice(problems)
    return q, roots

# ----- Main Quiz Engine -----

def ask_problem(level):
    if level==1: q,ans=level1()
    elif level==2: q,ans=level2()
    elif level==3: q,ans=level3()
    elif level==4: q,ans=level4()
    elif level==5: q,ans=level5()
    else: q,ans=level6()

    print("\nQ: " + q)
    if level==6:
        # Quadratics: ask root by root
        correct=0
        for i in range(2):
            try:
                user=int(input("Enter root " + str(i+1) + ": "))
                if user in ans:
                    print("Correct")
                    correct+=1
                else:
                    print("Wrong. Possible roots:", ans)
            except:
                print("Invalid")
        return correct==2
    else:
        try:
            user=float(input("Your answer: "))
            if round(user,3)==round(ans,3):
                print("Correct!")
                return True
            else:
                print("Wrong. Ans =", ans)
                return False
        except:
            print("Invalid")
            return False

def main():
    while True:
        print("\n--- Math Trainer Lite ---")
        print("1. Level 1: Add/Sub")
        print("2. Level 2: Mult/Div")
        print("3. Level 3: Logs/Exponents")
        print("4. Level 4: Trig")
        print("5. Level 5: Word Problems")
        print("6. Level 6: Quadratics")
        print("7. Quit")
        choice=input("Choose: ")
        if choice in ["1","2","3","4","5","6"]:
            lvl=int(choice)
            score=0
            for i in range(3):  # 3 questions per round
                if ask_problem(lvl):
                    score+=1
            print("Score:",score,"/ 3")
        elif choice=="7":
            break
        else:
            print("Invalid.")

main()
