import sys
sys.path.append('./')
import module_1

class Rt:
  l = 'OK ye bas ek test he'




if __name__ == '__main__':
  from module_1 import Example
  sa = Example("rahul",90)
  print(sa.l)