from itertools import *

data = [1,2,3,'a','b','c']
second_data = ['x','y','z']
all_data = sorted(chain(data,second_data),reverse=True)
for i in all_data:
    print(i)