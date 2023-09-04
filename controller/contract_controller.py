from model.da.utills.contract_da import ContractDa
from model.entity.contract import Contract
from controller.utills.validator import *


class ContractController:

    @classmethod
    def save(self, name, subject, start_year, end_year, price):
        try:
            if 1386 < start_year < 1403 and 1386 < end_year < 1403:
                con = Contract(0, name, subject, start_year, end_year, price)
                c_da = ContractDa()
                c_da.save(con)
                return True, "قرارداد ذخیره شد"
            else:
                return False, "سال شروع و پایان قرارداد باید بین 1350 تا 1402 باشد"

        except Exception as e:
            return False, str(e)


    @classmethod
    def edit(self, code, name, subject, start_year, end_year, price):
        try:
            if 1386 < start_year < 1403 and 1386 < end_year < 1403:
                con = Contract(code, name, subject, start_year, end_year, price)
                c_da = ContractDa()
                c_da.edit(con)
                return True, con
            else:
                raise ValueError("سال شروع و پایان قرارداد باید بین 1350 تا 1402 باشد")

        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(self, code):
        try:
            if isinstance(code, int) and code > 0:
                c_da = ContractDa()
                c_da.remove(code)
                return True, code
            else:
                raise ValueError("کد باید یک عدد و مثبت باشد")


        except Exception as e:
            return False, str(e)


    @classmethod
    def find_all(self):
        try:
            c_da = ContractDa()
            contract_list = c_da.find_all()
            return True, contract_list

        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_name(self, name):
        try:
            if isinstance(name, str) and re.match("^[آ-ی]{1,60}$", name):
                c_da = ContractDa()
                contract_list = c_da.find_by_name(name)
                return True, contract_list
            else:
                raise ValueError("نام مورد نظر درست نیست")

        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_subject(self, subject):
        try:
            if isinstance(subject, str) and re.match("^[آ-ی]{1,30}$", subject):
                c_da = ContractDa()
                contract_list = c_da.find_by_subject(subject)
                return True, contract_list
            else:
                raise ValueError("موضوع مورد نظر درست نیست")

        except Exception as e:
            return False, str(e)


    @classmethod
    def find_by_start_year(self, start_year, end_year):
        try:
            if 1386 < start_year < 1403 and 1386 < end_year < 1403:
                c_da = ContractDa()
                contract_list = c_da.find_by_start_year(start_year, end_year)
                return True, contract_list
            else:
                raise ValueError("سال شروع قرارداد باید بین 1387 تا 1402 باشد")

        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_end_year(self, start_year, end_year):
        try:
            if (1386 < start_year < 1403) and (1386 < end_year < 1403):
                c_da = ContractDa()
                contract_list = c_da.find_by_end_year(start_year, end_year)
                return True, contract_list
            else:
                raise ValueError("سال پایان قرارداد باید بین 1387 تا 1402 باشد")

        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_price(self, price):
        try:
            if isinstance(price, int) and price > 0:
                c_da = ContractDa()
                contract_list = c_da.find_by_price(price)
                return True, contract_list
            else:
                raise ValueError("مبلغ باید یک عدد و بزرگتر از صفر باشد")

        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_price_range(self, first_price, end_price):
        try:
            if isinstance(first_price, int) and isinstance(end_price, int) and first_price > 0 and end_price > 0:
                c_da = ContractDa()
                contract_list = c_da.find_by_price_range(first_price, end_price)
                return True, contract_list
            else:
                raise ValueError("رقم قرارداد معتبر نیست")

        except Exception as e:
            return False, str(e)

    @classmethod
    def check_contract_exist(self, contract):
        try:
            cu_da = ContractDa()
            result = cu_da.check_contract_exists(contract)
            return True, result[0]

        except Exception as e:
            return False, str(e)

    @classmethod
    def check_code_exists(self, code):
        try:
            if isinstance(code, int) and code > 0:
                cu_da = ContractDa()
                result = cu_da.check_code_exists(code)
                return result
            else:
                raise ValueError("مقدار کد به درستی وارد نشده است")

        except Exception as e:
            return False, str(e)

    @classmethod
    def calc_cont_score(self, contract):
        try:
            cu_da = ContractDa()
            score = cu_da.calc_cont_score(contract)
            return True, score

        except Exception as e:
            return False, str(e)

    @classmethod
    def calc_sum_score(self):
        try:
            cu_da = ContractDa()
            result = cu_da.calc_sum_score()
            return True, result

        except Exception as e:
            return False, str(e)