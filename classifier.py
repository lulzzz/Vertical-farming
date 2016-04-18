import re 				# importing regular expression

if __name__ == '__main__': 		# Defining weights for keywords
	dict = {"good":1.0, 
		"great":1.2,
		"awesome":1.7,
		"bad": -1.0,
		"terrible": -2.1,
		"awful":-3.3,
		"dangerous": -3.5
		}	
	
	ls =[]	
	temp = float(0)
	x = raw_input("Enter the text....  \n")
	ls =x.split()
	for i in ls:
		if i in dict:
			temp = temp + dict[i]
			
	if temp > 0:
		print "The sentence is positive with total weight ", temp
	elif(temp==0):
		print "The sentence is unpredicatble", temp
	else:
		print "The sentence is negative with toatl weight", temp
