import mysql.connector


class BoardingDa():

    def save(self, boarding):
        if not self.check_boarding_exists(boarding):
            score = self.calc_score(boarding)
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
            cursor = db.cursor()
            cursor.execute("insert into boarding_tbl (NAME, FAMILY, MELLI, GRADE, MAJOR, WORK_YEARS, SCORE) values (%s, %s, %s, %s, %s, %s, %s)",
                           [boarding.name, boarding.family, boarding.melli, boarding.grade, boarding.major, boarding.work_years, score])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("این شخص در جدول وجود دارد")

    def edit(self, boarding):
        if self.check_code_exists(boarding.code):
            score = self.calc_score(boarding)
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
            cursor = db.cursor()
            cursor.execute("update boarding_tbl set name=%s, family=%s, melli=%s, grade=%s, major=%s, work_years=%s , SCORE=%s where code=%s",
                           [boarding.name, boarding.family, boarding.melli, boarding.grade, boarding.major, boarding.work_years, score, boarding.code])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("شخص موجود نمی باشد")

    def remove(self, code):
        if self.check_code_exists(code):
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
            cursor = db.cursor()
            cursor.execute("delete from boarding_tbl where code=%s", [code])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("کد موردنظر موجود نیست")

    def find_all(self):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from boarding_tbl")
        boarding_list = cursor.fetchall()
        cursor.close()
        db.close()
        return boarding_list

    def find_by_name(self, name):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from boarding_tbl where name=%s", [name])
        boarding_list = cursor.fetchall()
        cursor.close()
        db.close()
        return boarding_list

    def find_by_family(self, family):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from boarding_tbl where FAMILY=%s", [family])
        boarding_list = cursor.fetchall()
        cursor.close()
        db.close()
        return boarding_list


    def find_by_grade(self, grade):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from boarding_tbl where GRADE=%s", [grade])
        boarding_list = cursor.fetchall()
        cursor.close()
        db.close()
        return boarding_list

    def find_by_major(self, major):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from boarding_tbl where MAJOR=%s", [major])
        boarding_list = cursor.fetchall()
        cursor.close()
        db.close()
        return boarding_list

    def calc_score(self, boarding):
        f_score = 0
        match boarding.grade:
            case "دیپلم":
                f_score = 0
            case "فوق دیپلم":
                f_score = 125
            case "کارشناسی":
                f_score = 250
            case "کارشناسی ارشد":
                f_score = 275
            case "دکتری":
                f_score = 300

        s_score = boarding.work_years * 20

        total_score = f_score + s_score
        return total_score

    def check_boarding_exists(self, boarding):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute(
                 "SELECT COUNT(*) FROM boarding_tbl WHERE NAME = %s AND FAMILY = %s AND MELLI = %s AND GRADE = %s AND MAJOR = %s AND WORK_YEARS = %s",
                [boarding.name, boarding.family, boarding.melli, boarding.grade, boarding.major, boarding.work_years])
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    def check_code_exists(self, code):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM boarding_tbl WHERE code=%s", [code])
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    def calc_sum_score(self):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("SELECT SUM(score) FROM boarding_tbl")
        result = cursor.fetchone()
        cursor.close()
        return result

