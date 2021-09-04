print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "What is your weight?",
weight = raw_input()
print "So you are %r old, %r tall and %r heavy" % (age,height,weight)



a, b = 0,1
while b < 100:
    print(b)
    a,b = b, a+b




a= ['madhab', 'paudel','gount','ping','ting','ding','ring','king','fing']

for i in range(0,len(a)):
    print(i,a[i])
