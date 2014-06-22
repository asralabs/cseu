#askuser_sel:	get selection from a user, sanitize input
#str title,str query,list opt {str}, str default
#return str
def askuser_sel(title,query,options,default):
	while (1==1):	
		print "\n"+title
		for i in options:
			print i
		sel=raw_input(query+"["+default+"]:")
		if sel=="":
			sel=default
		for i in options:
			if sel==i:
				return sel
		print sel+" was invalid. Please type one of the options."

#askuser_num:	get number from a user, sanitize input
#str title, str query, int default,int numMin,int numMax
#numMax/numMin can also = "", for no max or nomin
#return int
def askuser_int(title,query,default,numMin,numMax):	
	#make sure numMin/numMax is int
	while (1==1):
		print "\n"+title
		sel=raw_input(query+"["+str(default)+"]:")
		try:
			sel=int(sel)
		
			if numMin=="":	#no min
				if numMax=="":	#no max
					return sel
				else:			#max
					if sel<=int(noMax):
						return sel
			else:			#min
				if sel>=int(numMin):
					if numMax=="":			#no max
						return sel
					elif sel<=int(numMax):	#sel less then max
						return sel
		except ValueError,e:
			#print "ValueError Exception:"+str(e)
			pass
		print str(sel)+" was invalid. min="+str(numMin)+", max="+str(numMax)
			



		