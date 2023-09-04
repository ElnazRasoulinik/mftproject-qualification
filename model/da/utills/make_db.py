import mysql.connector


class MakeDatabase:
    def make_db(self):
        schema = mysql.connector.connect(host="localhost", user="root",password="10203040")
        cursor = schema.cursor()

        cursor.execute("DROP DATABASE IF EXISTS MFT")
        cursor.execute("CREATE DATABASE MFT")

        cursor.execute(
            "CREATE TABLE MFT.CUSTOMER_TBL (CODE INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(50), NATION_CODE VARCHAR(11), REGISTRATION_CODE VARCHAR(5), SUBJECT VARCHAR(20), GRADE INT, CONTRACT_INDICATOR BIGINT, BOARDING_INDICATOR MEDIUMINT, REWARDING_INDICATOR MEDIUMINT)")
        cursor.execute(
                "CREATE TABLE MFT.BOARDING_TBL (CODE INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30), FAMILY VARCHAR(30), MELLI VARCHAR(13), GRADE VARCHAR(30), MAJOR VARCHAR(20), WORK_YEARS INT, SCORE MEDIUMINT)")
        cursor.execute(
                "CREATE TABLE MFT.REWARDING_TBL (CODE INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(30), FAMILY VARCHAR(30), MELLI VARCHAR(13), GRADE VARCHAR(30), MAJOR VARCHAR(20), WORK_YEARS INT, SCORE MEDIUMINT)")
        cursor.execute(
                "CREATE TABLE MFT.CONTRACT_TBL (CODE INT PRIMARY KEY AUTO_INCREMENT, NAME VARCHAR(30), SUBJECT VARCHAR(30), START_YEAR MEDIUMINT, END_YEAR MEDIUMINT, PRICE bigint, SCORE MEDIUMINT)")
        cursor.execute(
                "CREATE TABLE MFT.INDICATOR (CODE INT PRIMARY KEY AUTO_INCREMENT, SUBJECT VARCHAR(30), ONE VARCHAR(10), TWO VARCHAR(10), THREE VARCHAR(10), FOUR VARCHAR(10), FIVE VARCHAR(10))")
        cursor.execute(
                "INSERT INTO MFT.INDICATOR (SUBJECT, ONE, TWO, THREE, FOUR, FIVE) VALUES ('ساختمان', '255542', '127771', '64026', '28081', '0'), ('راه و ترابری', '383312', '191656', '96039', '42122', '0'), ('نفت و گاز', '511083', '25542', '128052', '56163', '0'), ('تاسیسات', '229987', '114994', '57623', '25273', '0'), ('آب و فاضلاب', '434421', '217210', '108844', '47739', '0'), ('صنعت', '459975', '229987', '115246', '50547', '0'), ('کشاورزی', '178879', '89440','44818', '19657', '0')")

        schema.commit()
        print("Database Created")

        cursor.close()
        schema.close()
