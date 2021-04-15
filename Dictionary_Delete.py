def delete(key):
    my_Dict.pop(key)
    print(my_Dict)
my_Dict = {'abc':'Java','xyz':'python','c':300, 15:20, 52:64}
delete('abc')
delete('xyz')
