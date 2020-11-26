""" Muhammad Khan
Create Grade class

a. There are two quizzes, each graded on the basis of 10 points.

b. There is one midterm exam and one final exam, each graded on the basis of 100 points.

c. The final exam counts for 50% of the grade, the midterm counts for 25%,and the two quizzes
together count for a total of 25%. (Do not forget to normalize the quiz scores. They should be converted
to a percentage before they are averaged in.).

Any grade of 90 or more is an A, any grade of 80 or more (but less than 90) is a B, any grade of 70 or
more (but less than 80) is a C, any grade of 60 or more (but less than 70) is a D, and any grade below 60 is an F.

The program will ask for the score in each exam and output the student’s record, which consists of two quiz and
two exam scores as well as the student’s average numeric score for the entire course and final letter grade.

Define and use a class for the student record.  Use setter and getter methods, do not manipulate the class
data directly.
"""

class Grade:
    def _init_(self, quiz1, quiz2, midterm, final):
        self.quiz1 = quiz1
        self.quiz2 = quiz2
        self.midterm = midterm
        self.final = final

    # getter method
    def get_quiz1(self):
        return self.quiz1
    def get_quiz2(self):
        return self.quiz2
    def get_midterm(self):
        return self.midterm
    def get_final(self):
        return self.final

    # setter method
    def set_quiz1(self, quiz1):
        self.quiz1 = quiz1
    def set_quiz2(self, quiz2):
        self.quiz2 = quiz2
    def set_midterm(self, midterm):
        self.midterm = midterm
    def set_final(self, final):
        self.final = final

class StudentRecord:
    # Input
    a = float(input("Enter quiz 1 grades in -/10: "))
    b = float(input("Enter quiz 2 grades in -/10: "))
    c = float(input("Enter midterm grades: "))
    d = float(input("Enter final grades: "))
    print()

    g=Grade();
    # setting the grades using setter
    g.set_quiz1(a)
    g.set_quiz2(b)
    g.set_midterm(c)
    g.set_final(d)
    #totalgrades = float((g.get_quiz1() + g.get_quiz2()) / 4 + g.get_midterm() / 4 + g.get_final() / 2)
    #percent = float(totalgrades/80)*100
    totalgrades = float(0.5 * g.get_final() + 0.25 * g.get_midterm() + 0.25 * (g.get_quiz1() + g.get_quiz2()) / 2 * 10)
    percent = float(totalgrades/100)*100

    if percent>=90:
        grade='A'
    elif percent>=80 and percent<90:
        grade='B'
    elif percent>=70 and percent<80:
        grade='C'
    elif percent>=60 and percent<70:
        grade='D'
    else:
        grade='F'

    print("Quiz 1 grades: " + str(g.get_quiz1()))
    print("Quiz 2 grades: " + str(g.get_quiz2()))
    print("Midterm grades: " + str(g.get_midterm()))
    print("Final grades: " + str(g.get_final()))
    print()
    print("Total percentage: "+str(percent))
    print("Letter grade: "+str(grade))

