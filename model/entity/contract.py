from controller.utills.validator import *


class Contract:
    def __init__(self, code, name, subject, start_year, end_year, price, score=0):
        self.code = code
        self.name = name
        self.subject = subject
        self.start_year = start_year
        self.end_year = end_year
        self.price = price
        self.score = score

    def __repr__(self):
        return str(self.__dict__)

    @property
    def code(self):
        return self._code

    @code.setter
    @number(positive=True, message="کد معتبر نیست")
    def code(self, code):
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    @persian(length=60, message="نام معتبر نیست")
    def name(self, name):
        self._name = name

    @property
    def subject(self):
        return self._subject

    @subject.setter
    @persian(length=30, message="موضوع معتبر نیست")
    def subject(self, subject):
        self._subject = subject

    @property
    def start_year(self):
        return self._start_year

    @start_year.setter
    @number(positive=True, message="سال شروع باید عدد باشد")
    def start_year(self, start_year):
            self._start_year = start_year

    @property
    def end_year(self):
        return self._end_year

    @end_year.setter
    @number(positive=True, message="سال پایان باید عدد باشد")
    def end_year(self, end_year):
            self._end_year = end_year


    @property
    def price(self):
        return self._price

    @price.setter
    @number(positive=True, message="مبلغ قرارداد باید عدد باشد")
    def price(self, price):
        self._price = price

