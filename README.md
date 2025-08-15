# math trainer for ti-84 plus ce

a comprehensive mental math training program designed specifically for ti-84 plus ce calculators using ti's micropython subset. this program helps students develop and practice mental math skills across 6 different difficulty levels.

## 🎯 features

### **interactive learning system**
- **6 progressive levels** from basic arithmetic to advanced algebra
- **customizable practice sessions** with 1-20 questions per session
- **timed mode option** with real-time timer display
- **immediate feedback** with correct/incorrect answer responses
- **step-by-step solutions** available via math button (press 'm')

### **comprehensive problem types**
- **level 1**: basic addition and subtraction (2-digit numbers)
- **level 2**: multiplication, division, and mixed operations
- **level 3**: logarithms and exponents
- **level 4**: trigonometry (angles, conversions, trig functions)
- **level 5**: amc 8-style word problems (multiple choice)
- **level 6**: quadratic equations (factoring and guess-and-check)

### **smart problem generation**
- **adaptive difficulty** within each level
- **realistic amc 8 problems** covering percentages, algebra, geometry, fractions, number theory, and word problems
- **clean division problems** with whole number results
- **mixed operations** combining multiple mathematical concepts

## 📚 level details

### **level 1: basic math skills**
- **skills**: addition and subtraction
- **problem types**: simple addition (10-99 + 1-99), simple subtraction (20-99 - 1-99)
- **examples**: 25 + 7, 35 - 12
- **math button**: shows answer only (no explanation needed for basic operations)

### **level 2: basic math part 2**
- **skills**: multiplication, division, mixed operations
- **problem types**: 
  - larger multiplication (10-25 × 2-9)
  - division with clean results
  - division with remainders (whole number part)
  - mixed operations (e.g., 3 × 4 + 2)
- **examples**: 15 × 6, 48 ÷ 6, 3 × 4 + 5
- **math button**: shows answer only

### **level 3: logarithms & exponents**
- **skills**: basic exponentiation and logarithmic functions
- **problem types**: 
  - exponents (base 2-5, power 2-4)
  - logarithms (simple cases like log₂(8))
- **examples**: 2³, log₂(8)
- **math button**: full step-by-step explanations

### **level 4: basic trigonometry**
- **skills**: angle conversions, trigonometric functions
- **problem types**:
  - degree to radian conversion
  - radian to degree conversion
  - trigonometric function values (sin, cos, tan)
- **examples**: convert 180° to radians, sin(30°)
- **math button**: full explanations with formulas and common values

### **level 5: amc 8 questions**
- **skills**: word problems, multiple choice reasoning
- **problem types**:
  - percentage problems
  - algebra equations
  - geometry (area, perimeter)
  - fractions
  - number theory
  - real-world word problems
- **examples**: "if 15% of a number is 45, what is the number?"
- **math button**: problem-solving strategies and keyword identification

### **level 6: quadratics**
- **skills**: quadratic equation solving
- **problem types**: factorable quadratic equations
- **examples**: x² - 5x + 6 = 0
- **math button**: factoring techniques and solution methods

## 🎮 how to use

### **getting started**
1. **select level**: choose from 6 difficulty levels (1-6)
2. **view level info**: see skills tested and example problems
3. **choose timing**: opt for timed or untimed practice
4. **set question count**: select 1-20 questions for your session
5. **solve problems**: answer each question using the number pad
6. **get help**: press 'm' for step-by-step solutions
7. **review results**: see your accuracy and time at the end

### **controls**
- **number pad**: enter answers
- **enter key**: confirm selections and continue
- **'m' key**: show math button solution/explanation
- **any other key**: go back to previous menu

### **session flow**
```
main menu → level selection → level info → timing option → 
question count → problem solving → results → return to menu
```

## 🔧 technical requirements

### **hardware**
- ti-84 plus ce calculator
- micropython support enabled

### **software**
- ti's micropython subset
- no external dependencies required
- uses only standard libraries: `random`, `math`, `time`

### **installation**
1. transfer `main.py` to your ti-84 plus ce calculator
2. run the program from the calculator's python environment
3. follow the on-screen prompts to begin training

## 📊 features in detail

### **timed mode**
- real-time timer display during problems
- total session time tracking
- performance metrics in results

### **math button system**
- **levels 1-2**: quick answer display (basic operations)
- **levels 3-6**: comprehensive step-by-step explanations
- educational content with examples and formulas
- problem-solving strategies for complex topics

### **problem generation**
- **random selection**: each session provides different problems
- **difficulty scaling**: problems get more challenging within levels
- **realistic content**: amc 8 problems match actual competition format
- **clean results**: division problems designed for whole number answers

### **results tracking**
- correct/incorrect answer counts
- accuracy percentage calculation
- session time (if timed mode enabled)
- level and question count summary

## 🎓 educational benefits

### **skill development**
- **mental math**: improves calculation speed and accuracy
- **problem solving**: develops logical thinking and strategy
- **test preparation**: amc 8 level prepares for math competitions
- **concept understanding**: explanations reinforce mathematical concepts

### **progressive learning**
- **scaffolded difficulty**: each level builds on previous skills
- **varied problem types**: exposes students to different mathematical concepts
- **immediate feedback**: helps identify areas for improvement
- **self-paced learning**: students can practice at their own speed

## 🔄 recent updates

### **version 2.0 features**
- ✅ **enhanced amc 8 problems**: expanded from 5 to 18 problems across 6 categories
- ✅ **simplified basic levels**: removed overly complex problem types for cleaner practice
- ✅ **improved explanations**: more detailed step-by-step solutions for advanced levels
- ✅ **better problem variety**: more realistic and educational problem types
- ✅ **streamlined interface**: cleaner user experience with better navigation

### **problem type refinements**
- **level 1**: focused on simple addition/subtraction without carrying/borrowing
- **level 2**: removed basic times tables, added more challenging operations
- **level 5**: comprehensive amc 8 coverage with realistic multiple choice options

## 🚀 future enhancements

### **planned features**
- [ ] **progress tracking**: save scores across sessions
- [ ] **difficulty adjustment**: adaptive difficulty based on performance
- [ ] **more problem types**: additional mathematical concepts
- [ ] **statistics dashboard**: detailed performance analytics
- [ ] **custom problem sets**: user-defined problem categories

### **potential additions**
- [ ] **geometry problems**: more complex geometric calculations
- [ ] **statistics**: mean, median, mode problems
- [ ] **probability**: basic probability calculations
- [ ] **number theory**: prime numbers, factors, multiples

## 📝 usage tips

### **for students**
- start with level 1 to build confidence
- use the math button when stuck to learn solution methods
- practice regularly with timed sessions to improve speed
- review explanations even for correct answers to reinforce concepts

### **for teachers**
- assign specific levels based on student skill level
- use timed sessions to assess calculation speed
- review math button explanations to understand student thinking
- track progress across multiple sessions

## 🤝 contributing

this project is designed for educational use. suggestions for improvements, additional problem types, or bug reports are welcome.

## 📄 license

this project is open source and available under the mit license.

---

**happy math training! 🧮✨**