# 1 Student
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # 2
    def show_info(self):
        print(f"Студент: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Курс: {self.course}")
        print("-" * 20)

    # 3 стан
    def change_course(self, new_course):
        self.course = new_course



student1 = Student("Ло", 19, 2)
student2 = Student("Тайлер", 21, 3)

student1.show_info()
student2.show_info()

student1.change_course(3)
print("Після зміни курсу:")
student1.show_info()


# 4 Task
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.title}"


# 5 Кілька об
tasks = [
    Task("Вивчити класи в Python"),
    Task("Зробити домашнє завдання"),
    Task("Написати планувальник"),
]

tasks[1].mark_done()

print("\nСписок завдань:")
for task in tasks:
    print(task)


# 6 Event
class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def show(self):
        print(f"Подія: {self.title}")
        print(f"Дата: {self.date}")


# 7 М-Ч
class Event:
    def __init__(self, title, date, description=""):
        self.title = title
        self.date = date
        self.description = description

    def show(self):
        print(f"Подія: {self.title}")
        print(f"Дата: {self.date}")
        print(f"Опис: {self.description}")

    def update_description(self, new_description):
        self.description = new_description


event = Event("Захист проєкту", "2026-12-01", "Презентація RPG-гри")
event.update_description("Презентація RPG-гри та демонстрація класів")
print("\nПодія після зміни опису:")
event.show()