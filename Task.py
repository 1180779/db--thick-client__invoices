from db_connection import cnx_mssql
from Decimal import *
from AccountGen import *
from random import randint

class Task(object):
    def __init__(self):
        self.cursor = cnx_mssql.cursor()
    
    def Print(self):
        querry = "SELECT * FROM Invoice"
        self.cursor.execute(querry)
        result = self.cursor.fetchall()
        print("DATABASE: ")
        if len(result) == 0:
            print("{empty}")
        for row in result:
            print(row)

    def Task1(self):
        querry = "DELETE FROM Invoice"
        self.cursor.execute(querry)

        cnx_mssql.commit()
        print("\nlog: database cleared")
        self.Print()

    def Task2(self):
        netlist = {Decimal(100), Decimal(200), Decimal(300)}
        for i, net in zip(range(1, 4), netlist):
            gross = net * 1.23
            self.cursor.execute("INSERT INTO Invoice (invoice_id, net, gross) VALUES (" + str(i) + ", " + str(net) + ", " + str(gross) + ')')

        cnx_mssql.commit()
        print("\nlog: added 3 entries")
        self.Print()

    def Task3(self):
        update = self.__getupdatearrays()
        for row in update:
            querry = "UPDATE Invoice SET net = " + str(row[1]) + ", " "gross = " + str(row[2]) + " WHERE invoice_id = " + str(row[0])
            self.cursor.execute(querry)
        
        querry = "INSERT INTO Invoice (invoice_id, net, gross) VALUES (4, '1000.00', '1230.00')"
        self.cursor.execute(querry)
        
        cnx_mssql.commit()
        print("\nlog: doubled the amounts, added 1 entry")
        self.Print()

    def Task4(self):
        gen = AccountGen()
        for i in range(5, 14):
            net = Decimal(randint(0, 10000), randint(0, 99))
            gross = Decimal(randint(0, 10000), randint(0, 99))
            account = gen.Generate()
            querry = "INSERT INTO Invoice VALUES(" + str(i) + ", " +  str(net) + ", " + str(gross) + ", " + account + ")"
            self.cursor.execute(querry)

        cnx_mssql.commit()
        print("\nlog: added 10 entries")
        self.Print()

    def __getupdatearrays(self):
        querry = "SELECT * FROM Invoice"
        self.cursor.execute(querry)
        rows = self.cursor.fetchall()
        update = []
        for row in rows:
            rowstr = str(row)
            rowstr = rowstr[1:]
            rowstr = rowstr[:-1]
            rowstr = rowstr.replace(' ', '')
            fields = rowstr.split(',')

            updaterow = []
            updaterow.append(fields[0])
            updaterow.append(Decimal(fields[1]) * 2)
            updaterow.append(Decimal(fields[2]) * 2)
            update.append(updaterow)
        return update

