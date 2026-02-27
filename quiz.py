import csv
import random
import tkinter as tk

results = []

filepath = "business_unit_names.csv"

class Person:
    def __init__(self, domain, name, role):
        self.domain = domain
        self.name = name
        self.role = role

    def __repr__(self):
        return "Person(" + self.domain + ", " + self.name + ", " + self.role + ")"

#CSV

def read_csv(filepath):
    people = []
    try:
        file = open(filepath, "r")
        lines = file.readlines()
        file.close()
        for i in range(1, len(lines)):
            row = lines[i].strip().split(",")
            p = Person(row[0], row[1], row[2])
            people.append(p)
    except:
        print("Error, could not read the file")
    return people

def check_role(role):
    if role == 'SME' or role == 'Seller' or role == 'Tech Seller':
        return True
    else:
        return False

def check_name(text):
    if text.strip() == "":
        return False
    else:
        return True

#Quiz

def pick_random_person(people):
    number = random.randint(0, len(people) - 1)
    return people[number]

def make_question(person):
    question = "Who is the " + person.role + " for " + person.domain + "?"
    return question

def check_answer(person, answer):
    if answer.strip().lower() == person.name.lower():
        return True
    else:
        return False

#Saving the Results

def save_results(filepath, results):
    try:
        file = open(filepath, "w")
        for line in results:
            file.write(line + "\n")
        file.close()
    except:
        print("Could not save results.")

#GUI

class QuizGUI:
    def __init__(self, people):
        self.people = people
        self.current = None
        self.window = tk.Tk()
        self.window.title("Quiz Programme")
        self.label_question = tk.Label(self.window, text="Press Start to begin")
        self.label_question.pack()
        self.entry_answer = tk.Entry(self.window)
        self.entry_answer.pack()
        self.button_start = tk.Button(self.window, text="Start Quiz", command=self.start_quiz)
        self.button_start.pack()
        self.button_submit = tk.Button(self.window, text="Submit Answer", command=self.submit_answer)
        self.button_submit.pack()
        self.button_save = tk.Button(self.window, text="Save Results", command=self.save_results_to_file)
        self.button_save.pack()
        self.label_result = tk.Label(self.window, text="")
        self.label_result.pack()
        self.window.mainloop()
        self.score = 0
        self.question_number = 0
        self.current = None

    def start_quiz(self):
        self.score = 0
        self.question_number = 0
        self.ask_new_question()
        self.current = pick_random_person(self.people)
        question = make_question(self.current)
        self.label_question.config(text=question)
        self.entry_answer.delete(0, tk.END)
        self.label_result.config(text="")

    def submit_answer(self):
        user_answer = self.entry_answer.get()
        if check_answer(self.current, user_answer):
            self.label_result.config(text="Correct")
            self.score += 1
        else:
            self.label_result.config(text="Wrong, the correct answer was " + self.current.name)

        result_line = "Question: " + make_question(self.current)
        result_line += " | Your answer: " + user_answer

        if check_answer(self.current, user_answer):
            result_line += " | Correct"
        else:
            result_line += " | Wrong (Correct was " + self.current.name + ")"

        results.append(result_line)
        self.question_number += 1
        self.ask_new_question()

    def ask_new_question(self):
        if self.question_number == 5:
            self.label_question.config(text="Quiz finished! Your score: " + str(self.score) + "/5")
            return

        self.current = pick_random_person(self.people)
        question = make_question(self.current)
        self.label_question.config(text=question)
        self.entry_answer.delete(0, tk.END)
        self.label_result.config(text="")

    def save_results_to_file(self):
        save_results("results.txt", results)
        self.label_result.config(text="Results saved!")

#Run

people = read_csv(filepath)
QuizGUI(people)