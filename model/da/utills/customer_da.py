import mysql.connector


class CustomerDa:

    def save(self, customer):
        cu_da = CustomerDa()
        if not cu_da.show_customer():
            contract_indicator, boarding_indicator, rewarding_indicator = cu_da.check_score(customer.subject, customer.grade)
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
            cursor = db.cursor()
            cursor.execute("insert into customer_tbl (NAME, NATION_CODE, REGISTRATION_CODE, SUBJECT, GRADE, contract_indicator, boarding_indicator, rewarding_indicator) values (%s, %s, %s, %s, %s, %s, %s, %s)",
                           [customer.name, customer.nation_code, customer.registration_code, customer.subject, customer.grade, contract_indicator, boarding_indicator, rewarding_indicator])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("قبلا اطلاعات شرکت را اضافه کرده اید")

    def edit(self, customer):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("update customer_tbl set NATION_CODE=%s, NATION_CODE=%s, REGISTRATION_CODE=%s, SUBJECT=%s, GRADE=%s where code=%s",
                       [customer.name, customer.nation_code, customer.registration_code, customer.subject, customer.grade, customer.code])
        db.commit()
        cursor.close()
        db.close()

    def remove(self, code):
        if self.check_code_exists(code):
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
            cursor = db.cursor()
            cursor.execute("delete from customer_tbl where code=%s", [code])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("کد مورد نظر شما وجود ندارد")

    def show_customer(self):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from customer_tbl")
        customer_list = cursor.fetchall()
        cursor.close()
        db.close()
        return customer_list

    def check_code_exists(self, code):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("SELECT code FROM customer_tbl WHERE code = %s", [code])
        result = cursor.fetchone()
        cursor.close()
        return result

    def check_score(self, subject, grade):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM indicator WHERE subject = %s", [subject])
        result = cursor.fetchall()
        contract_indicator = result[0][grade+1]
        db.commit()
        cursor.close()
        db.close()


        match grade:
            case 1:
                boarding_indicator =1200
                rewarding_indicator = 1800
            case 2:
                boarding_indicator = 1000
                rewarding_indicator = 800
            case 3:
                boarding_indicator = 800
                rewarding_indicator = 400
            case 4:
                boarding_indicator = 600
                rewarding_indicator = 200
            case 5:
                boarding_indicator = 600
                rewarding_indicator = 0

        return contract_indicator, boarding_indicator, rewarding_indicator

    def show_indicator(self):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from customer_tbl")
        customer_list = cursor.fetchall()
        cursor.close()
        db.close()
        return customer_list[0][6], customer_list[0][7], customer_list[0][8]


