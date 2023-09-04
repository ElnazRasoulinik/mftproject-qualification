import mysql.connector


class RewardingDa():

    def save(self, rewarding):
        if not self.check_rewarding_exists(rewarding):
            score = self.calc_score(rewarding)
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password= "10203040")
            cursor = db.cursor()
            cursor.execute("insert into rewarding_tbl (name, family, melli, grade, major, work_years, score) values (%s, %s, %s, %s,%s, %s, %s)",
                           [rewarding.name, rewarding.family, rewarding.melli, rewarding.grade, rewarding.major, rewarding.work_years, score])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("این شخص در جدول وجود دارد")

    def edit(self, rewarding):
        if self.check_code_exists(rewarding.code):
            score = self.calc_score(rewarding)
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
            cursor = db.cursor()
            cursor.execute("update rewarding_tbl set name=%s, family=%s, melli=%s, grade=%s, major=%s, work_years=%s, score=%s  where code=%s",
                           [rewarding.name, rewarding.family, rewarding.melli, rewarding.grade, rewarding.major, rewarding.work_years, score, rewarding.code])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("شخص موجود نمی باشد")

    def remove(self, code):
        if self.check_code_exists(code):
            db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
            cursor = db.cursor()
            cursor.execute("delete from rewarding_tbl where code=%s", [code])
            db.commit()
            cursor.close()
            db.close()
        else:
            raise ValueError("کد موردنظر موجود نیست")

    def find_all(self):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from rewarding_tbl")
        rewarding_list = cursor.fetchall()
        cursor.close()
        db.close()
        return rewarding_list

    def find_by_name(self, name):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from rewarding_tbl where name=%s", [name])
        rewarding_list = cursor.fetchall()
        cursor.close()
        db.close()
        return rewarding_list

    def find_by_family(self, family):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from rewarding_tbl where FAMILY=%s", [family])
        rewarding_list = cursor.fetchall()
        cursor.close()
        db.close()
        return rewarding_list


    def find_by_grade(self, grade):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from rewarding_tbl where GRADE=%s", [grade])
        rewarding_list = cursor.fetchall()
        cursor.close()
        db.close()
        return rewarding_list

    def find_by_major(self, major):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("select * from rewarding_tbl where MAJOR=%s", [major])
        rewarding_list = cursor.fetchall()
        cursor.close()
        db.close()
        return rewarding_list
    
    def calc_score(self, rewarding):
        f_score = 0
        match rewarding.grade:
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

        s_score = rewarding.work_years * 10

        total_score = f_score + s_score
        return total_score

    def check_rewarding_exists(self, rewarding):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute(
                 "SELECT COUNT(*) FROM rewarding_tbl WHERE NAME = %s AND FAMILY = %s AND MELLI = %s AND GRADE = %s AND MAJOR = %s AND WORK_YEARS = %s",
                [rewarding.name, rewarding.family, rewarding.melli, rewarding.grade, rewarding.major, rewarding.work_years])
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    def check_code_exists(self, code):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM rewarding_tbl WHERE code=%s", [code])
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    def calc_sum_score(self):
        db = mysql.connector.connect(host="localhost", database="mft", user="root", password="10203040")
        cursor = db.cursor()
        cursor.execute("SELECT SUM(score) FROM rewarding_tbl")
        result = cursor.fetchone()
        cursor.close()
        return result

