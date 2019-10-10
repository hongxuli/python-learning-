start_user = [1111, 2222]
user_info = [{'id': 1111, 'values': {'name': 'hongxu', 'age': 24}}, {
    'id': 2222, 'values': {'name': 'yujia', 'age': 25}}]
relations = [{'id': 1111, 'follower': [1234, 2341, 2134], 'fans':[9821, 7632, 8463]}, {
    'id': 2222, 'follower': [7255, 2847, 9473], 'fans':[7206, 7323, 1232]}]


# def request(uid, callback=None):
#     return uid


def start_request():
    for uid in start_user:
        yield parse_user(uid)


def parse_user(uid):
    yield out_put_value(uid)

    if uid in start_user:

        yield parse_follower(uid)

        yield parse_fans(uid)


def parse_follower(uid):
    for relation in relations:
        if uid == relation.get('id'):
            follows = relation.get('follower')
            for follow in follows:
                yield parse_user(follow)


def parse_fans(uid):
    for relation in relations:
        if uid == relation.get('id'):
            fans = relation.get('fans')
            for fan in fans:
                yield parse_user(fan)


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
    while True:
        b=next(a)
        while True:
            next(b)
