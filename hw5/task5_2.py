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
from collections import namedtuple


class Student:
    Lab = namedtuple("Lab", "id mark")

    def __init__(self, name, course_conf):
        self.name = name
        self.course_progress = {}
        self.course_conf = course_conf

    def make_lab(self, mark, lab_id):
        self.course_progress.setdefault('labs', []).append(self.Lab(lab_id, mark))
        return self

    def make_exam(self, mark):
        if (mark is not None) and (0 < mark <= self.course_conf.get('exam_max')):
            self.course_progress['exam'] = mark
        return self

    def is_certified(self):
        maximum_points = self._maximum_points()
        total_points = self._total_points()
        is_pass = (total_points / maximum_points) > self.course_conf.get('k')
        return total_points, is_pass

    def _total_points(self):
        labs = self.course_progress.get('labs')
        total_points = sum((lab.mark for lab in self._lab_filter(labs)))
        total_points += self.course_progress.get('exam', 0)
        return total_points

    def _lab_filter(self, labs):
        lab_ids = set()
        latest = []
        for lab in reversed(labs):
            if not lab.id in lab_ids:
                latest.append(lab)
            lab_ids.add(lab.id)
        for lab in latest:
            if 0 > lab.id or lab.id > self.course_conf.get('lab_num'):
                yield self.Lab(lab.id, 0)
            elif lab.mark is None:
                yield self.Lab(lab.id, 0)
            elif 0 > lab.mark or lab.mark > self.course_conf.get('lab_max'):
                yield self.Lab(lab.id, 0)
            else:
                yield lab

    def _exam_filter(self, mark):
        if 0 > mark > self.course_conf.get('exam_max'):
            return 0
        return mark

    def _maximum_points(self):
        return (self.course_conf['lab_max']
                * self.course_conf['lab_num']
                + self.course_conf['exam_max'])


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
    a.make_lab(None, 1)
    a.make_exam(30)

print(a.is_certified())
