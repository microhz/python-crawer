#!/bin/python
print "hello world!"
print "中文字符"
if True : 
    print "true..."
else :
    print "false..."

name = "micro"
print name
i = 10
print i

a = b = c = 1
print a
print b

d,e,f = 1,2,"haha"
print d
print e
print f

i1 = 1
i2 = 2
i3 = 4
print i1

del i1

s = "abcd"
print s[1:2]
print s[1:3]
s = s + "efg"
print s
print s[2:11]
print s[2:]

t = (1,2,3,4,"a")
print t[0]
print t[3:]

list = [1,2,3,4]
print list
print list[2:]

print list[2:] * 3

print t[4] * 5

d = {1:"a",2:"b"}
print d[1]
print d.keys()

print d.values()

l2 = [1,2,3,5]
if (1 in l2) :
    print "1 is in"
else :
    print "not in"

if (4 not in l2) : 
    print "4 not in"
else :
    print "is in"

i2 = "abc"
i3 = "abc"
if (i2 is not i3) :
    print "i2 not is i3"
else :
    print "is "

i5 = 0
sum = 0
while i5 <= 100 :
    sum += i5
    i5 += 1
print sum 

s2 = "abcdefg"
print len(s2)
for i in range(len(s2)) : 
    j = len(s2) - i - 1
    if (i >= j) : 
        break
    print "exchange " + str(i) + " and " + str(j)
    s2 = s2[:i] + s2[j] + s2[i + 1:j] + s2[i] + s2[j + 1:]
    print s2
print s2

s = "str..."
print "a" + s
print "a",s

for i in range(0,8) :
    if (i == 4 or i == 5) :
        continue
    if (i == 2) :
        pass
    print i


s2 = "micro.."
print "hello ...",s2 + " python.."

class User : 
    '注释'
    id
    name

    def __init__(self, name, id) :
        self.name = name
        self.id = id
    def say(self) :
        print "this is my name " + self.name + ", and my id is " + str(self.id)

u = User("micro", 2)
u.say()

print u.id
print User.__name__
print User.__doc__

print User.__dict__
dis = User.__dict__
for d in dis :
    print d

class Parent :
    id = 0
    name = "micro"
    def __init__(self, id, name) :
        self.id = id
        self.name = name
    def parentSay(self,s) :
        print "parent call " + s
class Son(Parent) :
    age = 0
    def __init__(self, age) :
        self.age = age
    def sonSay(self,s) :
        print "age",str(self.age),"son say..",s

    def callParent(self,s) :
        self.parentSay(s)

    ## override
    def parentSay(self, s) :
        print "this call is override.."
s = Son(24)
s.sonSay("hello")
s.callParent("parent...")