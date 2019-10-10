import pymysql

# create table
##----------------------------------------
# s1 = 'create table if not exists students (id varchar(255) not null, name varchar(255) not null, age int not null, primary key (id))'
# table = 'students'
# keys=','.join(data.keys())
# values=','.join(['%s']*len(data))
# # generate sql dynamically 
# s2 = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)

# try:
#     if cursor.execute(s2, tuple(data.values())):
#     # if cursor.execute(s1):
#         print('successful')
#         db.commit()
# except Exception as e:
#     print(e)
#     # cancle previous executions
#     db.rollback()
# db.close()
##------------------------------------------------------------------------------------



# update function
##------------------------------------------------------------------------------------
# def update():
#     sql = 'update students set age = %s where name = %s'
#     try:
#         cursor.execute(sql,(25,'bob'))
#         db.commit()
#     except Exception as e:
#         print(e)
#         db.rollback()
#     db.close()
##------------------------------------------------------------------------------------


# insert data if value exit then update 
##------------------------------------------------------------------------------------
def insert_update(table, data):
    t = table
    d = data
    keys = ','.join(d.keys())
    values = ','.join(['%s']*len(d))

    sql = 'insert into {table}({keys}) values ({values}) on duplicate key update'.format(
        table=t, keys=keys, values=values)
    update = ','.join([" {key}=%s".format(key=key) for key in d])
    sql += update
    # try:
    #     #INSERT INTO students(id, name, age) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE id = %s, name = %s, age = %s  there is 6 %s so we need *2
    #     if cursor.execute(sql, tuple(d.values()) * 2):
    #         print('successful')    
    #         db.commit()
    # except Exception as e:
    #     print('failed')
    #     print(e)
    #     db.rollback()
    # db.close()
    excution(sql, t=tuple(d.values()) * 2)
##------------------------------------------------------------------------------------

# delete function 
##------------------------------------------------------------------------------------
def delete(table, conditon):
    table = table
    condition = condition 
    sql = 'delete from {table} where {condition}'. format(table = table, condition = condition)
    excution(sql)
##------------------------------------------------------------------------------------    


def read():
    sql = 'select * from students where age >=20'
    try:
        cursor.execute(sql)
        print('count', cursor.rowcount)
        row = cursor.fetchone()
        while row:
            print('row:', row)
            row = cursor.fetchone()
    except Exception as e:
        print('failed')
        print(e)









# execute the CURD
def excution(sql,t=None):
    try:
        exe_(sql, t)
        db.commit()
        print('successful')
    except Exception as e:
        print('failed')
        print(e)
        db.rollback()
    db.close()

# construct a sql execution 
def exe_(sql, t=None):
    if t == None:
        return cursor.execute(sql)
    else:
        return cursor.execute(sql,t)

    
  





db = pymysql.connect(host='localhost', user='root',
                     password='19941205', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id': '20120001',
    'name': 'bob',
    'age': 21
}

table = 'students'

insert_update(table, data)
