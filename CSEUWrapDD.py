import subprocess

#working
class CSEUWrapDD:
	def dd(self,inf,outf,bs,count,conv):
		if conv=="":
			p=subprocess.Popen(["dd","if="+inf,"of="+outf,"bs="+bs,"count="+count])
		else:
			p=subprocess.Popen(["dd","if="+inf,"of="+outf,"bs="+bs,"count="+count,"conv="+conv])
		p.communicate()

#test
#ddWrap=CSEUWrapDD()
#print "Dumping File...."
#ddWrap.dd(inf="/dev/urandom",outf="testdump",bs="1M",count="20",conv="")
