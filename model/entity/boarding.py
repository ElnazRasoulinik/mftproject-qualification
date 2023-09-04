from controller.utills.validator import *


class Boarding:
    def __init__(self, code, name, family, melli, grade, major, work_years, score=0):
        self.code = code
        self.name = name
        self.family = family
        self.melli = melli
        self.grade = grade
        self.major = major
        self.work_years = work_years
        self.score = score

    def __repr__(self):
        return str(self.__dict__)

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    @persian(length=30, message="نام باید فارسی باشد")
    def name(self, name):
        self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    @persian(length=30, message="نام خانوادگی باید فارسی باشد")
    def family(self, family):
        self._family = family

    @property
    def melli(self):
        return self._melli

    @melli.setter
    @national_code(message="کدملی اشتباه است")
    def melli(self, melli):
        self._melli = melli

    @property
    def grade(self):
        return self._grade

    @grade.setter
    @persian(length=20, message="مقطع تحصیلی باید فارسی باشد")
    def grade(self, grade):
        self._grade = grade

    @property
    def major(self):
        return self._major

    @major.setter
    @persian(length=20, message="رشته تحصیلی باید فارسی باشد")
    def major(self, major):
        self._major = major

    @property
    def work_years(self):
        return self._work_years

    @work_years.setter
    @number(positive=True, message="سابقه باید یک عدد مثبت باشد")
    def work_years(self, work_years):
        self._work_years = work_years
