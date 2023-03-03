# class Student:
#     print("Hello")
#     def __init__(self):  #КОНСТРУКТОР ЯКИЙ МІСТИТЬ В СОБІ ВЛАСТИВОСТІ КЛАСУ
#         self.height = 160
#         print("I'm German")
#
# first_student = Student() #ПОСИЛАННЯ НА КЛАС
# print(first_student.height) #ПОСИЛАННЯ НА ВЛАСТИВІСТЬ ВСЕРЕДИНІ КЛАСУ

# class Student:
#     amount_of_students = 0 #ВНУТРІШНЯ ЗМІННА КЛАСУ
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students += 1 #РАХУВАННЯ ПРИ ДОДАВАННІ НОВОГО ЕКЗЕМПЛЯРУ КЛАСУ
#
# german = Student()
# sasha = Student(height = 158) #ЗАПИС У КЛАС ЧЕРЕЗ КОНСТРУКТОР
# print(german.height)
# print(sasha.height)
# print(german.amount_of_students)

# class Student:
#     def __init__(self, name = None):
#         self.name = name
#     def __str__(self):
#         return f"Ya student. Moye imya {self.name}." #ПЕРЕТВОРЕННЯ НАЗВИ КЛАСУ ПРИМУСОВО
#
# kate = Student(name = "Kate") #ЗАДАННЯ ЗНАЧЕННЯ ПАРАМЕТРУ ПРИ ВИКЛИКУ КЛАСУ
# print(kate)
# print(kate.name)

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("Time to go rest")
        self.gladness += 3
    def to_chill(self):
        print("Time to play")
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed extern")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()

nick = Student(name = "Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)