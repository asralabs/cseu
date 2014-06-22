#cseu-create.py
#initial all in one script, for reference, will be deleted

import sys
import subprocess
from getpass import getpass

version="0.1a"

bad_input=True
c_type=""
c_cipher=""
c_iterations=1
c_passphrase=""
c_hashcmd=""

def askuser(title,query,options,default):
	while (1==1):	
		print "\n"+title
		for i in options:
			print i
		sel=raw_input(query+"["+default+"]:")
		if sel=="":
			return default
		for i in options:
			if sel==i:
				return sel
		print sel+" was invalid. Please type one of the options."


print "cseu-create-standard "+version
c_typeoptions={"standard","hidden"}
c_type=askuser("CONTAINER TYPE","type",c_typeoptions,"standard")

c_cipheroptions={"aes"}
c_cipher=askuser("CIPHER","cipher",c_cipheroptions,"aes")

c_modeoptions={"xts","cbc"}
c_mode=askuser("MODE","mode",c_modeoptions,"xts")

c_keysizeoptions={"8192"}
c_keysize=askuser("KEYSIZE","keysize",c_keysizeoptions,"8192")

c_hashfoptions={"sha512sum","sha256sum"}
c_hashf=askuser("HASH FUNCTION (HEADER):","hash",c_hashfoptions,"sha512sum")

c_size=int(raw_input("\nContainer size in MB:"))

c_file=raw_input("\nFile location (ex:~/cryptfile):") #find some way to sanitize this

c_passphrase=""
ct_passphrase="NULL"
firstrun=True
while (c_passphrase!=ct_passphrase):
	if firstrun!=True:	
		print "Passphrase was blank or did not match."
	c_passphrase=getpass()
	ct_passphrase=getpass()
	firstrun=False

print "\nContainer Summary"
print "Type:		"+c_type
print "Cipher:		"+c_cipher
print "Mode:		"+c_mode
print "Key Length:	"+c_keysize
print "Hash:		"+c_hashf
print "Size:		"+str(c_size)+"MB"
print "File:		"+c_file
sel=raw_input("Create? [y]:")
if sel!="y":
	exit()


def hashstr(h_cmd,string):
	print "Hashing password using"+h_cmd+"..."
	p= subprocess.Popen([h_cmd], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=False)
	return p.communicate(string)[0]

#f_size in int MB only
def makerandfile(fsize,floc):
	print "Creating "+str(fsize)+"MB"+" file at "+floc+"with /dev/urandom..."
	print subprocess.check_output(["dd","if=/dev/urandom","bs=1M","count="+str(fsize),"of="+floc])

#masterkeysize is hardcoded
def makemaster():
	print "Generating h0master with length 8K from /dev/urandom..."
	p=subprocess.Popen(["dd","if=/dev/urandom","bs=1K","count=8"],universal_newlines=False,stdout=subprocess.PIPE)
	return p.communicate()[0]

#need to work out finding open mappers
def openh0(h0hash,h0_keysize,floc):
	print "[SUDO] Opening h0..." #this is ignoring the cipher, need to format to cryptsetup 
	p=subprocess.Popen(["sudo","cryptsetup","open","--type=plain","--cipher=aes-xts-plain64","--key-size=512","--offset=0","--size=128",floc,"mapper0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=False)
	print p.communicate(h0hash) 

def closeh0(): #should prob take mapper as an argument
	print "[SUDO] Closing h0..."
	print subprocess.check_output(["sudo","cryptsetup","close","mapper0"]) 

def insnewmaster(slot,h0hash,h_keysize,floc):
	print "[SUDO] Inserting new "+slot+" master key..."
	if slot=="h0":
		openh0(h0hash,h_keysize,floc)
		print subprocess.check_output(["sudo","dd","if=/dev/urandom","bs=1K","count=8","of=/dev/mapper/mapper0","conv=notrunc"])
		closeh0()

def opend0(d0_mkey,d0_cipher,d0_mode,d0_keysize,floc):
	print "[SUDO] Opening d0..." #this is ignoring the cipher, need to format to cryptsetup
	p=subprocess.Popen(["sudo","cryptsetup","open","--type=plain","--cipher="+c_cipher+"-"+c_mode+"-plain64","--key-size=512","--offset=128",floc,"mapper1"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=False)
	print p.communicate(d0_mkey) 

def closed0(): #prob take mapper as arg
	print "[SUDO] Closing d0..."
	print subprocess.check_output(["sudo","cryptsetup","close","mapper1"])

def filld0(h0hash,d0_cipher,d0_mode,d0_keysize,floc):
	#filld0 assumes d0 is already open
	#this throws an exception when dd fills the drive, catch it and ignore
	print "[SUDO] Filling data0 with /dev/urandom, this may take some time..."
	opend0(h0hash,d0_cipher,d0_mode,d0_keysize,floc)
	try:
		print subprocess.check_output(["sudo","dd","if=/dev/urandom","bs=1M","of=/dev/mapper/mapper1"])
	except subprocess.CalledProcessError,e:
		print "[SUDO] Fill complete"
	closed0()

def maked0fs(h0hash,d0_cipher,d0_mode,d0_keysize,floc):
	print "[SUDO] Creating filesystem on data0..."
	opend0(h0hash,d0_cipher,d0_mode,d0_keysize,floc)
	subprocess.check_output(["sudo","mke2fs","-L volumed0","/dev/mapper/mapper1"])
	closed0()

def cleanup():
	print "Cleaning up..."
	subprocess.check_output(["sudo","cryptsetup","close","/dev/mapper/mapper1"])
	subprocess.check_output(["sudo","cryptsetup","close","/dev/mapper/mapper0"])

c_h0hash=hashstr(c_hashf,c_passphrase)
makerandfile(c_size,c_file)
c_h0master=makemaster()
insnewmaster("h0",c_h0hash, c_keysize, c_file)
maked0fs(c_h0hash,c_cipher,c_mode,c_keysize,c_file)
#cleanup()
print "Container Created!"










