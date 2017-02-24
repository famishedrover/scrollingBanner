import json 

def show() :	
	f = json.load(open('mycharlist.txt'))

	for i,j in f.iteritems() :
		if i == ' ' :
			i = 'Blank'
		print 'char :',i
		for x in j :
			print x
		print '\n'

