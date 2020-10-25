import os
import re
tijiao = []
fenge = (' ', '+', '-', ',')
with open('zuoyetijiao.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        temp = line.strip('\n')
        tijiao.append(re.split(r" |\+|-|,",temp))

    f.close()
newitems = []
for items in tijiao:
    newitem = list(range(3))
    for item in items:

        if item.isnumeric():
            newitem[0] = item
        elif item.endswith('次作业'):
            if item[1] == '一':
                t = list(item)
                t[1] = '1'
                item = ''.join(t)
            elif item[1] == '二':
                t = list(item)
                t[1] = '2'
                item = ''.join(t)
            elif item[1] == '三':
                t = list(item)
                t[1] = '3'
                item = ''.join(t)
            elif item[1] == '四':
                t = list(item)
                t[1] = '4'
                item = ''.join(t)
            elif item[1] == '五':
                t = list(item)
                t[1] = '5'
                item = ''.join(t)
            elif item[1] == '六':
                t = list(item)
                t[1] = '6'
                item = ''.join(t)
            elif item[1] == '七':
                t = list(item)
                t[1] = '7'
                item = ''.join(t)
            elif item[1] == '八':
                t = list(item)
                t[1] = '8'
                item = ''.join(t)
            elif item[1] == '九':
                t = list(item)
                t[1] = '9'
                item = ''.join(t)
            newitem[2] = item
        else:
            newitem[1] = item
    newitems.append(newitem)
with open('new_zuoyetijiao.txt','w+',encoding='utf-8') as ff:
    for item in newitems:
        ff.write(item[0]+'-'+item[1]+'-'+item[2]+'\n')
    ff.close()
count = {}
for item in newitems:
    count[item[1]] = []
for item in newitems:
    count[item[1]].append(item[2][1])
for k,v in count.items():
    c = []
    if len(v) < 8:
        c = set(['1','2','3','4','5','6','7','8']) - set(v)
        print(k+'缺交第'+str(c)+'次作业')