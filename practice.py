import mysql.connector as msql
mysql=msql.connect(host="localhost",database="mysql",user="root",password="1234")
if(mysql.is_connected()):
    print("connection established")
else:
    print("failed connection")
cur=mysql.cursor()
cur.execute("insert into detail values ('piyu','2000-02-9','87','07:32','A',24)")
mysql.commit()

def update():
    rno=int(input("enter the number"))
    sname=input("enter the name")
    query="update student set '%s' where %s"%(sname,rno)
    cur.execute(query)
    mysql.commit()
    update()