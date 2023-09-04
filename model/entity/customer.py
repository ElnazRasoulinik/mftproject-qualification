from controller.utills.validator import *


class Customer:
    def __init__(self, code, name, nation_code, registration_code, subject, grade):
        self.code = code
        self.name = name
        self.nation_code = nation_code
        self.registration_code = registration_code
        self.subject = subject
        self.grade = grade

    def __repr__(self):
        return str(self.__dict__)

    @property
    def code(self):
        return self._code

    @code.setter
    @number(positive=True, message="کد باید یک عدد مثبت باشد")
    def code(self, code):
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    @persian(length=50, message="نام شرکت معتبر نمی باشد")
    def name(self, name):
        self._name = name

    @property
    def nation_code(self):
        return self._nation_code

    @nation_code.setter
    def nation_code(self, nation_code):
        self._nation_code = nation_code

    @property
    def registration_code(self):
        return self._registration_code

    @registration_code.setter
    def registration_code(self, registration_code):
        self._registration_code = registration_code

    @property
    def subject(self):
        return self._subject

    @subject.setter
    @persian(length=20, message="رشته درخواستی باید فارسی نوشته شود")
    def subject(self, subject):
        self._subject = subject

    @property
    def grade(self):
        return self._grade

    @grade.setter
    @number(positive=True, message="پایه درخواستی باید عدد باشد")
    def grade(self, grade):
        self._grade = grade