import re
from model.da.utills.customer_da import CustomerDa
from model.entity.customer import Customer


class CustomerController:

    @classmethod
    def save(self, name, nation_code, registration_code, subject, grade):
        try:
            if isinstance(nation_code, str) and re.match("^[0-9]{11}$", nation_code) and isinstance(registration_code, str) and re.match("^[0-9]{4,5}$", registration_code):
                cu = Customer(0, name, nation_code, registration_code, subject, grade)
                cu_da = CustomerDa()
                cu_da.save(cu)
                return True, "saved"
            else:
                return False, "شناسه ملی 11رقمی و شماره ثبت 4 یا 5رقمی می باشد"
        except Exception as e:
            return False, str(e)


    @classmethod
    def edit(self, code, name, nation_code, registration_code, subject, grade):
        try:
            cu = Customer(code, name, nation_code, registration_code, subject, grade)
            cu_da = CustomerDa()
            cu_da.edit(cu)
            return True, cu

        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(self, code):
        try:
            if isinstance(code, int) and code > 0:
                cu_da = CustomerDa()
                cu_da.remove(code)

            else:
                return False, "کد باید یک عدد مثبت باشد"

        except Exception as e:
            return False, str(e)


    @classmethod
    def show_customer(self):
        try:
            cu_da = CustomerDa()
            customer_list = cu_da.show_customer()
            return customer_list

        except Exception as e:
            return False, str(e)

    @classmethod
    def check_code_exist(self, code):
        try:
            if isinstance(code, int) and code>0:
                cu_da = CustomerDa()
                result = cu_da.check_code_exists(code)
                if result:
                    return True, result
                else:
                    return False, "کد در جدول نیست"
            else:
                return False, "کد باید یک عدد مثبت باشد"

        except Exception as e:
            return False, str(e)

    @classmethod
    def check_score(self, subject, grade):
        try:
            cu_da = CustomerDa()
            contract_indicator, boarding_indicator, rewarding_indicator = cu_da.check_score(subject, grade)
            return True, contract_indicator, boarding_indicator, rewarding_indicator

        except Exception as e:
            return False, str(e)

    @classmethod
    def show_indicator(self):
        try:
            cu_da = CustomerDa()
            contract_indicator, boarding_indicator, rewarding_indicator = cu_da.show_indicator()
            return contract_indicator, boarding_indicator, rewarding_indicator

        except Exception as e:
            return False, str(e)

