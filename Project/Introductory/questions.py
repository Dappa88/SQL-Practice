from ..connect_db import Connect_db as conn


class Query():
    @classmethod
    def execute(cls,query):
        cursor = conn().cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        print("record",record)
        

# Query.execute(query19)
query1 = "SELECT * FROM shippers"

query2 = "SELECT CategoryName, Description from Categories"

    
query3 = """ SELECT FirstName, LastName, hiredate from employees WHERE Title = sales representative
"""

query4 = """ SELECT FirstName, LastName, hiredate from employees WHERE Title = sales
representative and Country = United states
"""
     
query5 = """ SELECT orderid,orderdate from orders where employeeid = 5
"""
query6 = """ SELECT SupplierID,ContactName,ContactTitle from suppliers where ContactTitle <> Marketing Manager """

    
query7 = """ SELECT productid,productname FROM products WHERE productname ILIKE '%queso%' """


query8 = """ SELECT orderid, customerid,shipcountry FROM orders WHERE shipcountry = france OR shipcountry = germany"""

    
query9 = """ SELECT orderid, customerid,shipcountry FROM orders where shipcountry in  ('Brazil',
'Mexico',
'Argentina',
'Venezuela'
) """

query10 = """ SELECT employeeid, firstname , lastname ,title, birthdate from employees ORDER BY cast(birthdate as DATE) ASC"""

    
# query11 = """ SELECT firstname ,lastname ,title,EXTRACT(YEAR From cast(birthdate as DATE)) || '-'|| EXTRACT(MONTH From cast(birthdate as DATE)) || '-' || EXTRACT(DAY From cast(birthdate as DATE))AS DATEONLY from employees """
query11 =  """ SELECT employeeid, firstname , lastname ,title, cast(birthdate as DATE) from employees """


query12 = """ SELECT  firstname , lastname ,firstname||' '||lastname as fullname  from employees """
   
query13 = """ SELECT productid, quantity, productid * quantity as totalprice from orderdetails

"""


query14 = """ SELECT COUNT(customerid) from customers """

# query15 = """ SELECT date from orders order by date desc limit 1 """
query15 = """ SELECT MIN(orderid) AS Firstorder,date from orders"""


# query16 = """ SELECT DISTINCT country as country from customers"""
query16 = """ SELECT country from customers group by country"""

query17 = """SELECT ContactTitles,count(ContactTitles) from customers group by ContactTitles """

query18 = """ SELECT ProductID, ProductName,ContactName FROM products INNER JOIN suppliers on products.supplierid = suppliers.supplierid ORDER BY ProductID """
  
query19 = """ SELECT  OrderID, CAST(OrderDate AS DATE),Shippername FROM orders AS o INNER JOIN shippers AS s on o.shipperid = s.shipperid WHERE CAST(OrderID AS INTEGER) < 10300  ORDER BY OrderID """

    

    


    
