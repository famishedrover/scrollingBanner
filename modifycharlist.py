from sys import argv
characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "E" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    ",
                       "*****" ],
               
               "H" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ], 

               "O" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],

               "L" : [ "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],

               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ],
               "M" : [ "*   *",
                       "** **",
                       "* * *",
                       "* * *",
                       "*   *",
                       "*   *",
                       "*   *",],

               "U" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****",],

               "D" : [ "**   ",
                       "*  * ",
                       "*   *",
                       "*   *",
                       "*   *",
                       "* *  ",
                       "**   ",],
                       
               "I" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "*****",],

               "T" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",]
 
               } 






if __name__ == "__main__"
  try :
  	import json
  	if argv[1] == 'create' :
  		json.dump(characters, open('mycharlist.txt' , 'wb'))
  		print 'Done Creating mycharlist.txt'
  	elif argv[1] == 'print' :
  		from printdict import show
  		show()
  	else :
  		print 'No argv supplied , expected create or print command'
  except :
  	print 'No argv supplied , expected create or print command'








