class Person:
    def __init__(self, full_name='', year=None):
        self.full_name = full_name
        self.year = year

    def name(self):
        name = self.full_name.split(" ", 1)
        return name

    def surname(self):
        surname = self.full_name.split(" ", 2)
        return surname

    def age(self):
        return 2018 - self.year


class Employee(Person):
    def __init__(self, position="", experience=None, salary=None):
        self.position = position
        self.experience = experience
        self.salary = salary

    def what_position(self, experience):
        if experience > 6:
            return self.position + "Senior"
        elif 3 > experience > 6:
            return self.position + "Middle"
        elif experience < 3:
            return self.position + "Junior"

    def add_salary(self, money):
        return self.salary + money


class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        Employee.__init__(self, *args, **kwargs)
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

    def add_skills(self, *args):
