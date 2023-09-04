from model.da.utills.make_db import MakeDatabase
import os

class MakeDbController:

    @classmethod
    def make_db(self):
        try:
            md = MakeDatabase()
            md.make_db()
            return True
        except Exception as e:
            raise ValueError("problem in creating database", str(e))
