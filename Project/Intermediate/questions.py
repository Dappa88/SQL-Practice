from ..connect_db import Connect_db as conn


class Query():
    @classmethod
    def execute(cls,query):
        cursor = conn().cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        print("record",record)
# SELECT cat.categoryname, count(productname) as totalproduct FROM public.categories 
# AS cat INNER JOIN products as prod ON cat.categoryid = prod.categoryid
# group by cat.categoryname order by totalproduct desc



# SELECT count(customerid) as totalcustomer,city,country
# FROM public.customers group by city,country order by totalcustomer desc


# SELECT productname from product where unitprice < reorderlevel order by productid 


# SELECT productname,(unitprice+unitinorder) as Total from product where Total <= reorderlevel  and Discontinued = NO order by productid 


# SELECT * FROM public.customers
# ORDER BY country nulls last,customerid
# OFFSET 82 ROWS
# FETCH FIRST 10 ROWS ONLY 