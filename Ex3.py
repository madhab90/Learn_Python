def Formulate(x):
    if x <= 15 :
        print x*x

    else:
        print ("This is a jokeeeeeeeeeee!!!!!!!!")


Formulate(16)
Formulate(12)
Formulate(13)
Formulate(10000000000)
Formulate(15.0)



formater = "{} {} {} {}"

print (formater.format(1,2,3,4))
print (formater.format(True, False, True, False))
print (formater.format('one', 'two', 'three', 'four'))
print (formater.format(formater, formater,formater, formater))
print (formater.format(
    "This is My name",
    "How are you doing",
    "Big Bang Boong",
    "Love Python most!!!!!!!!!!!"
))
