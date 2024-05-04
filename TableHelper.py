from db_connection import cnx_mssql
import pymssql

class TableHelper(object):
    def __init__(self, table: str, fields, cursor: pymssql.Connection):
        if not isinstance(table, str):
            raise TypeError
        for item in fields:
            if not isinstance(item, str):
                raise TypeError
        if not isinstance(cursor, pymssql.Connection):
            raise TypeError
        self.fields = fields
        self.table = table
        self.cursor = cursor
    
    def Select(self):
        self.cursor.execute("SELECT " + self.__fieldcommalist() + " FROM " + self.table)
        return self.cursor.fetchall()
    
    def Insert(self, values):
        querry = "INSERT INTO " + self.table + '(' + self.__fieldcommalist() + ") VALUES (" +  self.__commalist(values) + ')'
        print("querry = " + querry)
        self.cursor.execute(querry)

    def Delete(self):
        cursor = cnx_mssql.cursor()
        cursor.execute("DELETE FROM " + self.table)

    def Update(self):
        querry = "UPDATE " + self.table + " SET " + self.__namevaluelist() + " WHERE "

    def Commit(self):
        cnx_mssql.commit()

    def Close(self):
        self.cursor.close()

    def __namevaluelist(self, values) -> str:
        res = "("
        if len(self.fields) != len(values):
            raise ValueError
        for field, value in zip(self.fields, values):
            res = res + field + '=' + str(value) + ','
        res = res[:-1]
        return res + ')'

    def __commalist(self, values) -> str:
        res = ""
        for value in values:
            res = res + str(value) + ','
        return res[:-1]

    def __fieldcommalist(self) -> str:
        res = ""
        for field in self.fields:
            res = res + field + ','
        return res[:-1]
