'''
Created on 2015/4/5

@author: fmir33
'''
for i in range(1,10):
    for j in range(1,10):
        text='%2d x %2d = %.2d    ' % (j,i,j*i)
        print (text),
    print "\n",