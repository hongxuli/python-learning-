data = {
    'id': '20120001',
    'name': 'bob',
    'age': 20
}
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s']*len(data))
# sql = 'insrt into {table}({keys}) values ({values}) on duplicate key update'.format(
#     table=table, keys=keys, values=values)
# update = ','.join(["{key}=%s".format(key=key) for key in data])
print('ssss', tuple(data.values()) * 2)
