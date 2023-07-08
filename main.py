
def func_gen():
    n = open('text.txt', encoding='utf-8')
    for line in n:
        d = {}
        key, *value = line.split()
        d[key] = value
        korteg = tuple([d])
        for i in [korteg]:
            yield i

    n.close()

a = func_gen()
for el in a:
   print(el)














































