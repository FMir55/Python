'''
Created on 2015/4/5

@author: fmir33
'''
array =[]
array.append(20)
array.append(30)

array2=[55,"dicc",13,13]
array2[0]=112

print len( array), sum(array),array2.count(13)
print array2[0], array2[-1],array2[1:3],array2[1:]