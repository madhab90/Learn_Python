from sys import argv
script, user_name = argv
prompt = '>'
print ('Hi %s, I am the %s script.' % (user_name, script))
print'I would like to ask you some questions.'
print 'Do you like %s' % user_name
likes = raw_input(prompt)
print 'Where do you live %s' % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, you said %r about liking me.
You live in %r. Not usre where that is.
And you have %r computer. Nice.
""" % (likes, lives, computer)
