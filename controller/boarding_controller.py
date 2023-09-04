from model.da.utills.boarding_da import BoardingDa
from model.entity.boarding import Boarding
import re


class BoardingController:

    @classmethod
    def save(self, name, family, melli, grade, major, work_years):
        try:
            if 0 < work_years < 16:
                br = Boarding(0, name, family, melli, grade, major, work_years)
                bd = BoardingDa()
                bd.save(br)
                return True, "شخص اضافه شد"
            else:
                return False, "سابقه فقط بین 1 تا 15 سال باشد"

        except Exception as e:
            return False, str(e)


    @classmethod
    def edit(self, code, name, family, melli, grade, major, work_years):
        try:
            if 0 < work_years < 16:
                br = Boarding(code, name, family, melli, grade, major, work_years)
                bd = BoardingDa()
                bd.edit(br)
                return True, br
            else:
                raise ValueError("سابقه فقط بین 1 تا 15 سال باشد")

        except Exception as e:

            return False, str(e)

    @classmethod
    def remove(self, code):
        try:
            if isinstance(code, int) and code > 0:
                bd = BoardingDa()
                bd.remove(code)
                return True, code
            else:
                raise ValueError("کد باید یک عدد و مثبت باشد")

        except Exception as e:
            return False, str(e)


    @classmethod
    def find_all(self):
        try:
            bd = BoardingDa()
            boarding_list = bd.find_all()
            return True, boarding_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_name(self, name):
        try:
            if isinstance(name, str) and re.match("^[آ-ی]{1,30}$", name):
                bd = BoardingDa()
                boarding_list = bd.find_by_name(name)
                return True, boarding_list
            else:
                raise ValueError("نام مورد نظر درست نیست")

        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_family(self, family):
        try:
            if isinstance(family, str) and re.match("^[آ-ی]{1,30}$", family):
                bd = BoardingDa()
                boarding_list = bd.find_by_family(family)
                return True, boarding_list
            else:
                raise ValueError("نام خانوادگی مورد نظر درست نیست")

        except Exception as e:
            return False, str(e)


    @classmethod
    def find_by_grade(self, garde):
        try:
            if isinstance(garde, str) and re.match("^[آ-ی]{1,30}$", garde):
                bd = BoardingDa()
                boarding_list = bd.find_by_grade(garde)
                return True, boarding_list
            else:
                raise ValueError("مقطع تحصیلی مورد نظر درست نیست")

        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_major(self, major):
        try:
            if isinstance(major, str) and re.match("^[آ-ی]{1,30}$", major):
                bd = BoardingDa()
                boarding_list = bd.find_by_major(major)
                return True, boarding_list
            else:
                raise ValueError("رشته تحصیلی مورد نظر درست نیست")

        except Exception as e:
            return False, str(e)

    @classmethod
    def calc_score(self, boarding):
        try:
            bd = BoardingDa()
            total_score = bd.calc_score(boarding)
            return True, total_score

        except Exception as e:
            return False, str(e)

    @classmethod
    def check_boarding_exists(self, boarding):
        try:
            bd = BoardingDa()
            result = bd.check_boarding_exists(boarding)
            return True, result

        except Exception as e:
            return False, str(e)

    @classmethod
    def check_code_exists(self, code):
        try:
            bd = BoardingDa()
            result = bd.check_code_exists(code)
            return True, result

        except Exception as e:
            return False, str(e)

    @classmethod
    def calc_sum_score(self):
        try:
            bd = BoardingDa()
            result = bd.calc_sum_score()
            return True, result
        except Exception as e:
            return False, str(e)