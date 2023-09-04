from model.da.utills.rewarding_da import RewardingDa
from model.entity.rewarding import Rewarding
import re


class RewardingController:
    # static
    @classmethod
    def save(self, name, family, melli, grade, major, work_years):
        try:
            if 0 < work_years < 16:
                rw = Rewarding(0, name, family, melli, grade, major, work_years)
                rd = RewardingDa()
                rd.save(rw)
                return True, "شخص اضافه شد"
            else:
                return False, "سابقه فقط بین 1 تا 15 سال باشد"

        except Exception as e:
            return False, str(e)


    @classmethod
    def edit(self, code, name, family, melli, grade, major, work_years):
        try:
            if 0 < work_years < 16:
                rw = Rewarding(code, name, family, melli, grade, major, work_years)
                rd = RewardingDa()
                rd.edit(rw)
                return True, rw
            else:
                raise ValueError("سابقه فقط بین 1 تا 15 سال باشد")

        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(self, code):
        try:
            if isinstance(code, int) and code > 0:
                rd = RewardingDa()
                rd.remove(code)
                return True, code
            else:
                raise ValueError("کد باید یک عدد و مثبت باشد")

        except Exception as e:
            return False, str(e)


    @classmethod
    def find_all(self):
        try:
            rd = RewardingDa()
            rewarding_list = rd.find_all()
            return True, rewarding_list

        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_name(self, name):
        try:
            if isinstance(name, str) and re.match("^[آ-ی]{1,30}$", name):
                rd = RewardingDa()
                rewarding_list = rd.find_by_name(name)
                return True, rewarding_list
            else:
                raise ValueError("نام مورد نظر درست نیست")

        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_family(self, family):
        try:
            if isinstance(family, str) and re.match("^[آ-ی]{1,30}$", family):
                rd = RewardingDa()
                rewarding_list = rd.find_by_family(family)
                return True, rewarding_list
            else:
                raise ValueError("نام خانوادگی مورد نظر درست نیست")

        except Exception as e:
            return False, str(e)


    @classmethod
    def find_by_grade(self, garde):
        try:
            if isinstance(garde, str) and re.match("^[آ-ی]{1,30}$", garde):
                rd = RewardingDa()
                rewarding_list = rd.find_by_grade(garde)
                return True, rewarding_list
            else:
                raise ValueError("مقطع تحصیلی مورد نظر درست نیست")

        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_major(self, major):
        try:
            if isinstance(major, str) and re.match("^[آ-ی]{1,30}$", major):
                rd = RewardingDa()
                rewarding_list = rd.find_by_major(major)
                return True, rewarding_list
            else:
                raise ValueError("رشته تحصیلی مورد نظر درست نیست")

        except Exception as e:
            return False, str(e)

    @classmethod
    def calc_score(rewarding):
        try:
            rd = RewardingDa()
            total_score = rd.calc_score(rewarding)
            return True, total_score

        except Exception as e:
            return False, str(e)

    @classmethod
    def check_rewarding_exists(self, rewarding):
        try:
            rd = RewardingDa()
            result = rd.check_rewarding_exists(rewarding)
            return True, result

        except Exception as e:
            return False, str(e)

    @classmethod
    def check_code_exists(self, code):
        try:
            rd = RewardingDa()
            result = rd.check_code_exists(code)
            return True, result
        except Exception as e:
            return False, str(e)

    @classmethod
    def calc_sum_score(self):
        try:
            rd = RewardingDa()
            result = rd.calc_sum_score()
            return True, result

        except Exception as e:
            return False, str(e)

