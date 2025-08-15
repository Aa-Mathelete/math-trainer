# Math Trainer Program for TI MicroPython
# A comprehensive mental math training program with 6 difficulty levels

import random
import math
import time

class MathTrainer:
    def __init__(self):
        self.levels = {
            1: {"name": "Basic Math Skills", "info": "Addition and Subtraction", "skills": ["addition", "subtraction"]},
            2: {"name": "Basic Math Part 2", "info": "Multiplication and Division", "skills": ["multiplication", "division"]},
            3: {"name": "Logarithms & Exponents", "info": "Basic log and exponent questions", "skills": ["logarithms", "exponents"]},
            4: {"name": "Basic Trigonometry", "info": "Angles, lengths, degree-radian conversion", "skills": ["trigonometry"]},
            5: {"name": "AMC 8 Questions", "info": "Multiple choice word problems", "skills": ["word_problems"]},
            6: {"name": "Quadratics", "info": "Solve quadratics using guess and check", "skills": ["quadratics"]}
        }
        self.current_level = 1
        self.timed_mode = False
        self.num_questions = 5
        self.correct_answers = 0
        self.wrong_answers = 0
        self.start_time = 0
        
    def clear_screen(self):
        """Clear the screen (placeholder for TI implementation)"""
        print("\n" * 50)
        
    def display_menu(self):
        """Display the main level selection menu"""
        self.clear_screen()
        print("=== MATH TRAINER ===")
        print("Select a level:")
        print()
        
        for level_num, level_info in self.levels.items():
            print(f"{level_num}. {level_info['name']}")
            print(f"   {level_info['info']}")
            print()
            
        print("Enter level number (1-6):")
        
    def show_level_info(self, level):
        """Show detailed information about a selected level"""
        self.clear_screen()
        level_info = self.levels[level]
        print(f"=== {level_info['name'].upper()} ===")
        print(f"Skills tested: {level_info['info']}")
        print()
        
        if level == 1:
            print("Example problems:")
            print("  25 - 7 = ?")
            print("  35 + 67 = ?")
        elif level == 2:
            print("Example problems:")
            print("  5 * 6 = ?")
            print("  90 / 4 = ?")
        elif level == 3:
            print("Example problems:")
            print("  2^3 = ?")
            print("  log_2(8) = ?")
        elif level == 4:
            print("Example problems:")
            print("  Convert 180° to radians")
            print("  Find sin(30°)")
        elif level == 5:
            print("Example problems:")
            print("  If 15% of a number is 45, what is the number?")
            print("  Multiple choice format")
        elif level == 6:
            print("Example problems:")
            print("  x² - 5x + 6 = 0")
            print("  Solve for x using guess and check")
            
        print()
        print("Press ENTER to start this level")
        print("Press any other key to go back")
        
    def get_timed_preference(self):
        """Ask user if they want timed mode"""
        self.clear_screen()
        print("=== TIMING OPTION ===")
        print("Do you want problems to be timed?")
        print("1. Yes - Show timer on top screen")
        print("2. No - No timing")
        print()
        print("Enter choice (1 or 2):")
        
        while True:
            try:
                choice = input().strip()
                if choice == "1":
                    self.timed_mode = True
                    return
                elif choice == "2":
                    self.timed_mode = False
                    return
                else:
                    print("Please enter 1 or 2:")
            except:
                print("Please enter 1 or 2:")
                
    def get_question_count(self):
        """Get number of questions from user"""
        self.clear_screen()
        print("=== NUMBER OF QUESTIONS ===")
        print("How many questions do you want to solve?")
        print("Enter a number (1-20):")
        
        while True:
            try:
                count = int(input().strip())
                if 1 <= count <= 20:
                    self.num_questions = count
                    return
                else:
                    print("Please enter a number between 1 and 20:")
            except ValueError:
                print("Please enter a valid number:")
                
    def generate_level1_problem(self):
        """Generate addition/subtraction problems"""
        problem_type = random.choice(['simple_add', 'simple_sub'])
        
        if problem_type == 'simple_add':
            a = random.randint(10, 99)
            b = random.randint(1, 99)
            answer = a + b
            problem = f"{a} + {b} = ?"
            
        else:  # simple_sub
            a = random.randint(20, 99)
            b = random.randint(1, a-1)
            answer = a - b
            problem = f"{a} - {b} = ?"
            
        return problem, answer, f"Level 1: {problem_type}"
        
    def generate_level2_problem(self):
        """Generate multiplication/division problems"""
        problem_type = random.choice(['larger_mult', 'division', 'remainder_div', 'mixed_ops'])
        
        if problem_type == 'larger_mult':
            a = random.randint(10, 25)
            b = random.randint(2, 9)
            answer = a * b
            problem = f"{a} × {b} = ?"
            
        elif problem_type == 'division':
            # Create division with clean result
            b = random.randint(2, 12)
            answer = random.randint(2, 12)
            a = b * answer
            problem = f"{a} ÷ {b} = ?"
            
        elif problem_type == 'remainder_div':
            # Division with remainders
            a = random.randint(20, 50)
            b = random.randint(3, 9)
            answer = a // b
            problem = f"{a} ÷ {b} = ? (whole number part)"
            
        else:  # mixed_ops
            # Mixed operations like 3 × 4 + 2
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            c = random.randint(1, 10)
            answer = a * b + c
            problem = f"{a} × {b} + {c} = ?"
            
        return problem, answer, f"Level 2: {problem_type}"
        
    def generate_level3_problem(self):
        """Generate log and exponent problems"""
        problem_type = random.choice(['exponent', 'log'])
        
        if problem_type == 'exponent':
            base = random.randint(2, 5)
            exp = random.randint(2, 4)
            answer = base ** exp
            problem = f"{base}^{exp} = ?"
        else:
            # Simple log problems
            base = random.randint(2, 4)
            result = random.randint(2, 4)
            answer = result
            problem = f"log_{base}({base**result}) = ?"
            
        return problem, answer, f"Level 3: {problem_type}"
        
    def generate_level4_problem(self):
        """Generate trigonometry problems"""
        problem_type = random.choice(['degree_to_radian', 'radian_to_degree', 'trig_value'])
        
        if problem_type == 'degree_to_radian':
            degrees = random.choice([30, 45, 60, 90, 180, 270, 360])
            answer = round(degrees * math.pi / 180, 3)
            problem = f"Convert {degrees}° to radians"
        elif problem_type == 'radian_to_degree':
            radians = random.choice([math.pi/6, math.pi/4, math.pi/3, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi])
            answer = round(radians * 180 / math.pi)
            problem = f"Convert {radians} radians to degrees"
        else:
            angle = random.choice([0, 30, 45, 60, 90])
            func = random.choice(['sin', 'cos', 'tan'])
            if func == 'sin':
                answer = round(math.sin(math.radians(angle)), 3)
            elif func == 'cos':
                answer = round(math.cos(math.radians(angle)), 3)
            else:
                answer = round(math.tan(math.radians(angle)), 3)
            problem = f"{func}({angle}°) = ?"
            
        return problem, answer, f"Level 4: {problem_type}"
        
    def generate_level5_problem(self):
        """Generate AMC 8 style word problems"""
        problems = [
            # Percentage problems
            ("If 15% of a number is 45, what is the number?", 300, "A) 200  B) 250  C) 300  D) 350  E) 400"),
            ("What is 25% of 80?", 20, "A) 15  B) 20  C) 25  D) 30  E) 35"),
            ("If 20% of 150 is x, what is x?", 30, "A) 25  B) 30  C) 35  D) 40  E) 45"),
            
            # Algebra problems
            ("If 3x + 7 = 22, what is x?", 5, "A) 3  B) 4  C) 5  D) 6  E) 7"),
            ("If 2x - 5 = 11, what is x?", 8, "A) 6  B) 7  C) 8  D) 9  E) 10"),
            ("If 4x + 3 = 19, what is x?", 4, "A) 3  B) 4  C) 5  D) 6  E) 7"),
            
            # Geometry problems
            ("What is the area of a square with side length 6?", 36, "A) 24  B) 30  C) 36  D) 42  E) 48"),
            ("What is the perimeter of a rectangle with length 8 and width 5?", 26, "A) 20  B) 26  C) 30  D) 32  E) 40"),
            ("What is the area of a rectangle with length 7 and width 4?", 28, "A) 22  B) 28  C) 30  D) 32  E) 35"),
            
            # Fraction problems
            ("If 2/3 of a number is 18, what is the number?", 27, "A) 24  B) 27  C) 30  D) 33  E) 36"),
            ("If 3/4 of 40 is x, what is x?", 30, "A) 25  B) 30  C) 35  D) 40  E) 45"),
            ("If 1/5 of 100 is x, what is x?", 20, "A) 15  B) 20  C) 25  D) 30  E) 35"),
            
            # Number theory
            ("What is the sum of the first 5 positive integers?", 15, "A) 10  B) 15  C) 20  D) 25  E) 30"),
            ("What is the product of 3, 4, and 5?", 60, "A) 45  B) 50  C) 60  D) 70  E) 80"),
            ("If a number is divisible by both 3 and 4, what is the smallest such number?", 12, "A) 6  B) 12  C) 18  D) 24  E) 36"),
            
            # Word problems
            ("A store sells shirts for $15 each. If you buy 4 shirts, how much do you pay?", 60, "A) 45  B) 50  C) 60  D) 65  E) 70"),
            ("If you travel 60 miles in 2 hours, what is your speed in miles per hour?", 30, "A) 25  B) 30  C) 35  D) 40  E) 45"),
            ("If 5 workers can complete a job in 8 hours, how many hours would 10 workers take?", 4, "A) 2  B) 4  C) 6  D) 8  E) 10")
        ]
        
        problem, answer, choices = random.choice(problems)
        return problem, answer, choices
        
    def generate_level6_problem(self):
        """Generate quadratic problems"""
        # Simple factorable quadratics
        quadratics = [
            ("x² - 5x + 6 = 0", [2, 3], "x² - 5x + 6 = 0"),
            ("x² - 7x + 12 = 0", [3, 4], "x² - 7x + 12 = 0"),
            ("x² + 5x + 6 = 0", [-2, -3], "x² + 5x + 6 = 0"),
            ("x² - 9 = 0", [3, -3], "x² - 9 = 0"),
            ("x² - 4x + 4 = 0", [2, 2], "x² - 4x + 4 = 0")
        ]
        
        problem, answers, equation = random.choice(quadratics)
        return problem, answers, equation
        
    def generate_problem(self, level):
        """Generate a problem for the specified level"""
        if level == 1:
            return self.generate_level1_problem()
        elif level == 2:
            return self.generate_level2_problem()
        elif level == 3:
            return self.generate_level3_problem()
        elif level == 4:
            return self.generate_level4_problem()
        elif level == 5:
            return self.generate_level5_problem()
        elif level == 6:
            return self.generate_level6_problem()
            
    def show_solution(self, level, problem, answer, extra_info=""):
        """Show step-by-step solution"""
        self.clear_screen()
        print("=== STEP-BY-STEP SOLUTION ===")
        print(f"Problem: {problem}")
        print()
        
        if level == 1:
            print("BASIC MATH - NO EXPLANATION NEEDED")
            print(f"Answer: {answer}")
                
        elif level == 2:
            print("BASIC MATH - NO EXPLANATION NEEDED")
            print(f"Answer: {answer}")
                
        elif level == 3:
            if '^' in problem:
                print("EXPONENT EXPLANATION:")
                print("An exponent tells you how many times to multiply")
                print("a number by itself.")
                print()
                print("Step 1: Identify the base and exponent")
                print("Step 2: Multiply the base by itself exponent times")
                print(f"Step 3: {problem.split('=')[0].strip()} = {answer}")
                print()
                print("Example: 2³ means 2 × 2 × 2 = 8")
                print("The exponent 3 tells you to multiply 2 by itself 3 times")
            else:
                print("LOGARITHM EXPLANATION:")
                print("A logarithm asks: 'What power do I need to raise")
                print("the base to get this number?'")
                print()
                print("Step 1: Identify the base and the result")
                print("Step 2: Find what power gives that result")
                print(f"Step 3: {problem.split('=')[0].strip()} = {answer}")
                print()
                print("Example: log₂(8) asks 'What power of 2 equals 8?'")
                print("Since 2³ = 8, the answer is 3")
                
        elif level == 4:
            if 'radians' in problem:
                print("DEGREE TO RADIAN EXPLANATION:")
                print("Radians are another way to measure angles.")
                print("180° = π radians")
                print()
                print("Step 1: Use the conversion factor: π/180")
                print("Step 2: Multiply degrees by π/180")
                print(f"Step 3: {problem.split('=')[0].strip()} = {answer}")
                print()
                print("Formula: radians = degrees × (π/180)")
                print("This converts from degrees to radians")
            elif 'degrees' in problem:
                print("RADIAN TO DEGREE EXPLANATION:")
                print("Convert radians back to degrees.")
                print("π radians = 180°")
                print()
                print("Step 1: Use the conversion factor: 180/π")
                print("Step 2: Multiply radians by 180/π")
                print(f"Step 3: {problem.split('=')[0].strip()} = {answer}")
                print()
                print("Formula: degrees = radians × (180/π)")
                print("This converts from radians to degrees")
            else:
                print("TRIGONOMETRIC FUNCTION EXPLANATION:")
                print("Trig functions relate angles to ratios of triangle sides.")
                print()
                print("Step 1: Identify the angle and function")
                print("Step 2: Use unit circle or calculator")
                print(f"Step 3: {problem.split('=')[0].strip()} = {answer}")
                print()
                print("Common values to remember:")
                print("sin(30°) = 0.5, sin(45°) = 0.707, sin(90°) = 1")
                print("cos(0°) = 1, cos(60°) = 0.5, cos(90°) = 0")
                
        elif level == 5:
            print("WORD PROBLEM EXPLANATION:")
            print("Word problems require translating words to math.")
            print()
            print("Step 1: Read the problem carefully")
            print("Step 2: Identify what you're looking for")
            print("Step 3: Write an equation")
            print("Step 4: Solve the equation")
            print(f"Step 5: Answer: {answer}")
            print()
            if extra_info:
                print(f"Multiple choice options: {extra_info}")
            print("Tip: Look for keywords like 'of', 'is', 'equals'")
            print("'of' usually means multiplication")
            print("'is' or 'equals' means =")
                
        elif level == 6:
            print("QUADRATIC EQUATION EXPLANATION:")
            print("Quadratic equations have the form ax² + bx + c = 0")
            print("We can solve by factoring or guess-and-check.")
            print()
            print("Step 1: Write the equation in standard form")
            print("Step 2: Try to factor into (x + a)(x + b) = 0")
            print("Step 3: Set each factor equal to zero")
            print("Step 4: Solve for x")
            print(f"Step 5: Solutions: x = {answer}")
            print()
            print(f"Equation: {extra_info}")
            print("Tip: Look for numbers that multiply to c and add to b")
            
        print()
        print("Press ENTER to continue...")
        input()
        
    def run_level(self, level):
        """Run a complete level session"""
        self.correct_answers = 0
        self.wrong_answers = 0
        
        for question_num in range(1, self.num_questions + 1):
            self.clear_screen()
            
            if self.timed_mode:
                self.start_time = time.time()
                print(f"Time: {time.time() - self.start_time:.1f}s")
                print()
                
            print(f"Question {question_num}/{self.num_questions}")
            print("=" * 30)
            
            problem, correct_answer, extra_info = self.generate_problem(level)
            print(f"Problem: {problem}")
            
            if level == 5:  # AMC 8 problems show choices
                print(f"Choices: {extra_info}")
                
            print()
            print("Enter your answer:")
            print("(Press 'M' for math button/solution)")
            
            while True:
                try:
                    user_input = input().strip().upper()
                    
                    if user_input == 'M':
                        self.show_solution(level, problem, correct_answer, extra_info)
                        self.clear_screen()
                        print(f"Question {question_num}/{self.num_questions}")
                        print("=" * 30)
                        print(f"Problem: {problem}")
                        if level == 5:
                            print(f"Choices: {extra_info}")
                        print()
                        print("Enter your answer:")
                        continue
                        
                    # Handle different answer types
                    if level == 6:  # Quadratic has multiple answers
                        if ',' in user_input:
                            user_answers = [int(x.strip()) for x in user_input.split(',')]
                            user_answers.sort()
                            correct_answer.sort()
                            is_correct = user_answers == correct_answer
                        else:
                            is_correct = False
                    else:
                        user_answer = float(user_input)
                        is_correct = abs(user_answer - correct_answer) < 0.01
                        
                    if is_correct:
                        print("CORRECT! ✓")
                        self.correct_answers += 1
                    else:
                        print("WRONG! ✗")
                        print(f"Correct answer: {correct_answer}")
                        self.wrong_answers += 1
                        
                    break
                    
                except ValueError:
                    print("Please enter a valid number (or 'M' for solution):")
                    
            print()
            print("Press ENTER to continue...")
            input()
            
    def show_results(self):
        """Show final results"""
        self.clear_screen()
        print("=== SESSION RESULTS ===")
        print(f"Level: {self.levels[self.current_level]['name']}")
        print(f"Questions: {self.num_questions}")
        print(f"Correct: {self.correct_answers}")
        print(f"Wrong: {self.wrong_answers}")
        
        if self.num_questions > 0:
            percentage = (self.correct_answers / self.num_questions) * 100
            print(f"Accuracy: {percentage:.1f}%")
            
        if self.timed_mode:
            total_time = time.time() - self.start_time
            print(f"Total time: {total_time:.1f} seconds")
            
        print()
        print("Press ENTER to return to main menu...")
        input()
        
    def run(self):
        """Main program loop"""
        while True:
            self.display_menu()
            
            try:
                level_choice = int(input().strip())
                if level_choice not in self.levels:
                    print("Please enter a number between 1 and 6")
                    continue
                    
                self.current_level = level_choice
                self.show_level_info(level_choice)
                
                if input().strip() == "":
                    self.get_timed_preference()
                    self.get_question_count()
                    self.run_level(level_choice)
                    self.show_results()
                    
            except ValueError:
                print("Please enter a valid number")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break

# Start the program
if __name__ == "__main__":
    trainer = MathTrainer()
    trainer.run()
