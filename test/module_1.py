import sys
sys.path.append('./')

from main import Rt


class Example(Rt):
    def __init__(self, name,roll ):


        self.name = name
        self.roll =roll
 

if __name__ =='__main__':
    a = Example('nazrul',21)
    print(a.name)
    print(a.roll)
    print(a.l)