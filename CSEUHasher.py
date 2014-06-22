import subprocess
from getpass import getpass

#this is all broken
oldh=getpass()
newh=""
iter=10
count=0
while count<iter:
	newh=subprocess.check_output(["echo","\""+oldh+"\"","sha512sum"], universal_newlines=False)
	oldh=newh
	count+=1

print "sha512sum after "+str(count)+" iterations:"
print newh
