start_user = [1111, 2222]
user_info = [{'id': 1111, 'values':{'name': 'hongxu', 'age': 24}},{'id':2222, 'values':{'name': 'yujia', 'age': 25}}]
relations = [{'id': 1111, 'follower': [1234,2341,2134],'fans':[9821,7632,8463]},{'id':2222, 'follower':[7255,2847,9473],'fans':[7206,7323,1232]}]


def request(uid, callback=None):
    if callback is None:
        return uid
    else:    
        return callback(uid) 


def start_request():
    for uid in start_user:
        print(uid)
        yield request(uid, callback=parse_user)


def parse_user(uid):
    yield  out_put_value(uid)

    if uid in start_user:

        yield request(uid, callback=parse_follower)

        yield request(uid, callback=parse_fans)


def parse_follower(uid):
    for relation in relations:
        if uid == relation.get('id'):
            follows = relation.get('follower')
            for follow in follows:
                yield request(follow, callback=parse_user)


def parse_fans(uid):
    for relation in relations:
        if uid == relation.get('id'):
            fans = relation.get('fans')
            for fan in fans:
                yield request(fan, callback=parse_user)


def out_put_value(uid):
    try:
        if uid in start_user:
            for user in user_info:
                if uid == user.get('id'):
                    print(str(uid) + str(user.get('values')))
        else:
            print(str(uid))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    a = start_request()
    for i in a:   
        for j in i:
            try:
                d=next(i)
            
            except Exception as e:
                # if isinstance(e,StopIteration):
                #     print('True')
                pass
           
       
        
