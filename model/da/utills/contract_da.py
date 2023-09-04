import mysql.connector


class ContractDa():

    def save(self, contract):
        if not self.check_contract_exists(contract):
            score = self.calc_cont_score(contract)
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password= "10203040")
            cursor = db.cursor()
            cursor.execute("insert into contract_tbl (NAME, SUBJECT, START_YEAR, END_YEAR, PRICE, SCORE) values (%s, %s, %s, %s,%s, %s)",
                           [contract.name, contract.subject, contract.start_year, contract.end_year, contract.price, score])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("این قرارداد در جدول وجود دارد")

    def edit(self, contract):
        if self.check_code_exists(contract.code):
            score = self.calc_cont_score(contract)
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
            cursor = db.cursor()
            cursor.execute("update contract_tbl set NAME=%s, SUBJECT=%s, START_YEAR=%s, END_YEAR=%s, PRICE=%s, SCORE=%s where code=%s",
                [contract.name, contract.subject, contract.start_year, contract.end_year, contract.price, score, contract.code])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("قرارداد موجود نیست")

    def remove(self, code):
        if self.check_code_exists(code):
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
            cursor = db.cursor()
            cursor.execute("delete from contract_tbl where code=%s", [code])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("کد موردنظر موجود نیست")

    def find_all(self):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from contract_tbl")
        contract_list = cursor.fetchall()
        cursor.close()
        db.close()
        return contract_list

    def find_by_code(self, code):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from contract_tbl where code=%s", [code])
        contract_list = cursor.fetchall()
        cursor.close()
        db.close()
        return contract_list

    def find_by_name(self, name):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from contract_tbl where name=%s", [name])
        contract_list = cursor.fetchall()
        cursor.close()
        db.close()
        return contract_list

    def find_by_subject(self, subject):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from contract_tbl where SUBJECT=%s", [subject])
        contract_list = cursor.fetchall()
        cursor.close()
        db.close()
        return contract_list


    def find_by_start_year(self, start_year, end_year):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from contract_tbl where START_YEAR between %s and %s", [start_year, end_year])
        contract_list = cursor.fetchall()
        cursor.close()
        db.close()
        return contract_list

    def find_by_end_year(self, start_year, end_year):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from contract_tbl where END_YEAR between %s and %s", [start_year, end_year])
        contract_list = cursor.fetchall()
        cursor.close()
        db.close()
        return contract_list

    def find_by_price(self, price):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from contract_tbl where PRICE=%s", [price])
        contract_list = cursor.fetchall()
        cursor.close()
        db.close()
        return contract_list

    def find_by_price_range(self, first_price, end_price):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from contract_tbl where PRICE between %s and %s", [first_price, end_price])
        contract_list = cursor.fetchall()
        cursor.close()
        db.close()
        return contract_list

    def check_contract_exists(self, contract):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM contract_tbl WHERE NAME = %s AND SUBJECT = %s AND START_YEAR = %s AND END_YEAR = %s AND PRICE = %s",
                        [contract.name, contract.subject, contract.start_year, contract.end_year, contract.price])
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    def check_code_exists(self, code):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM contract_tbl WHERE code=%s", [code])
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    def calc_cont_score(self, contract):
        h3 = 1402
        start_year = contract.start_year
        end_year = contract.end_year
        price = contract.price

        score = 0.03 * ((1.2) ** (h3 - (start_year + end_year) / 2)) * price
        return score

    def calc_sum_score(self):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("SELECT SUM(score) FROM contract_tbl")
        result = cursor.fetchone()
        cursor.close()
        return result