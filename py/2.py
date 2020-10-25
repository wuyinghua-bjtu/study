import os
import re
def find_filepath(path, kw, pos):
    items = os.listdir(path)
    if pos == None:
        for item in items:
            pt = os.path.join(path, item)
            if os.path.isdir(pt):
                find_filepath(pt,kw,pos)
            elif kw.lower() in pt.split('\\')[-1].lower():
                print(pt)

    elif pos == 'end':
        for item in items:
            pt = os.path.join(path, item)
            if os.path.isdir(pt):

                find_filepath(pt, kw, pos)
            elif os.path.splitext(pt)[0].lower().endswith(kw.lower()):
                print(pt)
    elif pos == 'start':
        for item in items:
            pt = os.path.join(path, item)
            if os.path.isdir(pt):

                find_filepath(pt,kw,pos)
            elif pt.split('\\')[-1].lower().startswith(kw.lower()):
                print(pt)



#find_filepath('d:\\a','test',None)
#find_filepath('d:\\a','test','start')
find_filepath('d:\\a', 'test', 'end')