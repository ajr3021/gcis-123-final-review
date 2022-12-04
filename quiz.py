import csv

class Question:
    __slots__ = ['__question', '__options', '__answer', '__difficulty']

    def __init__(self, question, options, answer, difficulty):
        self.__question = question
        self.__options = options
        self.__answer = answer
        self.__difficulty = difficulty

    def is_correct(self, answer:str):
        return answer == self.__answer

    def __str__(self) -> str:
        option_string = ""
        for i in range(len(self.__options)):
            option_string += chr(97 + i) + '. ' + self.__options[i] + '\n'
        return f"{self.__question}\n{option_string}"

    def __lt__(self, other:object):
        if type(self) == type(other):
            return self.__difficulty < other.__difficulty
        return False

class Quiz:
    __slots__ = ['__questions']

    def __init__(self, filename):
        self.__questions = []
        try:
            with open(filename) as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)
                for line in csv_reader:
                    q = Question(line[0], line[1:5], line[5], line[6])
                    self.__questions.append(q)
        except FileExistsError:
            print("File not found")

        self.__questions.sort()


    def start(self):
        for question in self.__questions:
            print(question)
            answer = input(">> ")
            if question.is_correct(answer):
                print("Correct")
            else:
                print("Incorrect")

quiz = Quiz('quiz.csv')
quiz.start()