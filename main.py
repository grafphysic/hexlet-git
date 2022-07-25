def make_user(name, age):
    return {'name': name, 'age': age}

def format_user(user):
    return str(user.get('name')) + ',' + str(user.get('age'))