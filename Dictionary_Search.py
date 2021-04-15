def get_key(val):
    for key, value in my_Dict.items():
        if val == value:
            return "success"
    return "key doesn't exist"
my_Dict = {'abc':'Java','xyz':'python','c':300, 15:20, 52:64}

print(get_key('java'))
print(get_key(64))
print(get_key(92))
