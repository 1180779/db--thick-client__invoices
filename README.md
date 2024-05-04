# Solution to db thick client task

## Task 
1. Create table in MS SQL Server database with the following columns (use SQL 'CREATE TABLE' command) 
of chosen types: 
   * invoice_id (primary key)
   * net value (in zlotys)
   * gross value (in zlotys)
   * account number (text value)
2. Create a project which will do the following in the subsequent transactions
   * remove existing entries from table
   * create three records with net values 100, 200, 300 and gross values equal to 1.23 * net 
   (values can be hard coded)
   * modifies all existing transactions by doubling the gross value and adds a new entry with gross value equal 1000
   * in loop creates 10 records with subsequent primary key values and random values in other columns, then modifies three random entries 
  (applies random values)
3. After each transcation the contents of database have to be displayed 