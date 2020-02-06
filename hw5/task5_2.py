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
    """
    Course representation
    """
    MAX_LAB_ATTEMPTS = 5

    def __init__(self, conf):
        self.conf = conf
        self.labs = {}
        self.exam = []

    def add_lab(self, mark, lab_id=None):
        """
        Добавляет оценку за лабораторную работу.
        Если lab_id == None - ищется первое невыполненное
        задание по возрастанию

        :param mark: mark for lab
        :param lab_id: lab work id
        """
        if lab_id is None:
            lab_id = self._get_unfulfilled_lab()
        tries = self.labs.setdefault(lab_id, [])
        # ограниченное число попыток сдачи
        if len(tries) > self.MAX_LAB_ATTEMPTS:
            raise Exception("Can't pass the task anymore, limit is reached")
        tries.append(mark)

    def _get_unfulfilled_lab(self):
        """
        Находит первую невыполненную задачу

        :raises: LookupError
        :return: lab id
        """
        for lab_id in range(self.conf["lab_num"]):
            if lab_id not in self.labs:
                return lab_id
        raise LookupError("Can't find unfulfilled task. All tasks done")

    def add_exam(self, mark):
        """
        :param mark: mark for exam
        """
        self.exam.append(mark)

    @property
    def total_points(self):
        """
        Сумма набранных баллов\n
        :return: int
        """
        points = sum(self._labs_points())
        points += self._exam_points()
        return points

    @property
    def maximum_points(self):
        """
        Максимальное кол-во баллов

        :return: int
        """
        return (self.conf['lab_max']
                * self.conf['lab_num']
                + self.conf['exam_max'])

    def is_certified(self):
        """
        Подсчитывает кол-во набранных баллов и
        определяет пройден ли курс

        :return: int, bool
        """
        is_pass = (self.total_points / self.maximum_points) > self.conf.get('k')
        return self.total_points, is_pass

    def _labs_points(self):
        """
        Выбирает оценки по основным лабораторным работам

        :return: int
        """
        for lab_id, marks in self.labs.items():
            if 0 <= lab_id <= self.conf['lab_num']:
                mark = marks[-1]
                yield mark if self._is_valid_lab_mark(mark) else 0

    def _is_valid_lab_mark(self, mark):
        """
        Проверяет корректность оценки за лабораторную работу

        :param mark:
        :return: None
        """
        rules = [lambda x: x is None,
                 lambda x: x < 0 or x > self.conf.get('lab_max')]
        if any(check(mark) for check in rules):
            return False
        return True

    def _exam_points(self):
        """
        Выбирает последнюю оценку за экзамен из всех попыток

        :return: int
        """
        if len(self.exam) == 0:
            return 0
        mark = self.exam[-1]
        return mark if self._is_valid_exam_mark(mark) else 0

    def _is_valid_exam_mark(self, mark):
        """
        Проверяет корректность оценки за экзамен

        :param: mark
        :return: bool
        """
        rules = [lambda x: x is None,
                 lambda x: x < 0 or x > self.conf['exam_max']]
        if any(check(mark) for check in rules):
            return False
        return True


class Student:
    """
    Student representation
    """
    def __init__(self, name, course_conf):
        """
        :param name: Имя студента
        :param course_conf: Конфигурация курса
        """
        self.name = name
        self.course = Course(course_conf)

    def make_lab(self, mark, lab_id=None):
        """
        Получить оценку за лабораторную работу\n
        :param mark: Оценка
        :param lab_id: Номер лабораторной работы
        :return: self
        """
        self.course.add_lab(mark, lab_id)
        return self

    def make_exam(self, mark):
        """
        Получить оценка за экзамен

        :param mark: Оценка дза экзамен
        :return: self
        """
        self.course.add_exam(mark)
        return self

    def is_certified(self):
        """
        Проверяет пройден ли курс

        :return: int, bool
        """
        return self.course.is_certified()


def main():
    """
    Class Student at work
    """
    course_conf = {
        "exam_max": 30,
        "lab_max": 7,
        "lab_num": 10,
        "k": 0.61,
    }

    student = Student("Vasya", course_conf)
    for _ in range(0, 8):
        student.make_lab(random.randint(1, 7))
    student.make_lab(1)
    student.make_exam(30)

    print(student.is_certified())


if __name__ == '__main__':
    main()
