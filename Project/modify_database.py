# from .connect_db import Connect_db as conn

# query = """ ALTER TABLE employees
# ADD COLUMN hiredate timestamp;
# ADD COLUMN salerepresentative VARCHAR;

# """
# # """ INSERT INTO item (item_Id, item_name, purchase_time, price) VALUES (%s, %s, %s, %s)"""

# query2 = """ INSERT INTO employees (hiredate,salerepresentative) (%s, %s),(%s, %s),(%s, %s),(%s, %s),(%s, %s),(%s, %s),(%s, %s)
# """


# def Modify(query,query2):
#     cursor = conn().cursor()
#     cursor.executemany(query,query)
#     conn.commit()
#     record = cursor.
#     print("record",record)