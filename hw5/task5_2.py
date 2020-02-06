# -*- coding: utf8 -*-

"""
Разработать класс Student для представления сведений об успешности
слушателя некого курса. Объект класса должен содержать поля для сохранения
имени студента и баллов, полученных им за выполнение практических заданий
и финального экзамена.
Обеспечить следующие методы класса:
- конструктор, принимающий строку - имя студента - и словарь,
 содержащий настройки курса в следующем формате:
```
conf = {
    "exam_max": 30
    "lab_max": 7,  #
    "lab_num": 10
    "k": 0.61,
}
```
- метод `make_lab(m, n)`,
- метод `make_exam(m)`,
- метод `is_certified()`,
"""

import random


class Course:
    def __init__(self, conf):
        self.conf = conf
        self.labs = {}
        self.exam = []

    def add_lab(self, mark, lab_id=None):
        if lab_id is None:
            lab_id = 0
        tries = self.labs.setdefault(lab_id, [])
        if len(tries) > 5:
            raise Exception("Can't pass the task anymore, limit is reached")
        tries.append(mark)

    def add_exam(self, mark):
        self.exam.append(mark)

    def total_points(self):
        points = sum(self._labs_points())
        points += self._exam_points()
        return points

    def maximum_points(self):
        return (self.conf['lab_max']
                * self.conf['lab_num']
                + self.conf['exam_max'])

    def is_certified(self):
        maximum_points = self.maximum_points()
        total_points = self.total_points()
        is_pass = (total_points / maximum_points) > self.conf.get('k')
        return total_points, is_pass

    def _labs_points(self):
        for lab_id, marks in self.labs.items():
            if 0 <= lab_id <= self.conf['lab_num']:
                mark = marks[-1]
                yield mark if self._is_valid_lab_mark(mark) else 0

    def _is_valid_lab_mark(self, mark):
        if mark is None:
            return False
        elif 0 > mark or mark > self.conf.get('lab_max'):
            return False
        else:
            return True

    def _exam_points(self):
        if len(self.exam) == 0:
            return 0
        mark = self.exam[-1]
        return mark if self._is_valid_exam_mark(mark) else 0

    def _is_valid_exam_mark(self, mark):
        if mark is None:
            return False
        if mark < 0 or mark > self.conf['exam_max']:
            return False
        return True


class Student:
    def __init__(self, name, course_conf):
        self.name = name
        self.course = Course(course_conf)

    def make_lab(self, mark, lab_id=None):
        self.course.add_lab(mark, lab_id)
        return self

    def make_exam(self, mark):
        self.course.add_exam(mark)
        return self

    def is_certified(self):
        return self.course.is_certified()


course_conf = {
    "exam_max": 30,
    "lab_max": 7,
    "lab_num": 10,
    "k": 0.61,
}
a = Student("Vasya", course_conf)
for lab_id in range(0, 40):
    a.make_lab(random.randint(1, 7), random.randint(1, 20))
else:
    a.make_lab(1)
    a.make_exam(30)

print(a.is_certified())
