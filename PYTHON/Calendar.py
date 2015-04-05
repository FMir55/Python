'''
Created on 2015/4/5

@author: fmir33
'''
ca=set()
user={'jan','feb','may','june','july'}
user.add('aug')
user.add('sep')
user.add('oct')
ca={'sep','oct','nov','dec'}

print ca&user
print ca|user
print ca^user
print ca-user
print user-ca