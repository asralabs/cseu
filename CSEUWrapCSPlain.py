#WrapCSPlain.py
#CS Wrapper for dm-crypt plain mode
#working
import subprocess
class CSEUWrapCSPlain:
	#options to check
	validOpt=dict()
	validOpt['hash']=		{"sha512"}
	validOpt['cipher']=		{"aes"}
	validOpt['key-size']=	{"512"}
	validOpt['mode']=		{"xts-plain64"}
	
	#dict options:
	#hash,				str
	#cipher, 			str
	#key-file,			str
	#key-size,			str
	#offset,			str
	#size,				str
	#loc,				str
	#mntloc,			str
	#readonly,			str (not supported)
	#shared,			str (not supported)
	#allow-discards,	str (not supported)
	#verify-passphrase,	str (not supported)
	#keyfile-offset,	str (not supported)

	#checkOpt, check a single option, return true if valid
	def checkOpt(self,in_k,in_o):
		try:
			for o in self.validOpt[in_k]:
				if in_o==o:
					return True
			return False
		except KeyError,e:
			print "CSPlain:Exception:KeyError:"+str(e)
			return False

	def copen(self,opt):
		if self.checkOpt('hash',opt['hash'])==False:
			return "ERROR"
		if self.checkOpt('cipher',opt['cipher'])==False:
			return "ERROR"
		if self.checkOpt('key-size',opt['key-size'])==False:
			return "ERROR"
		if self.checkOpt('mode',opt['mode'])==False:
			return "ERROR"

		#optional arguments
		optarg=""
		if opt['key-file']!="":
			optarg+="--key-file="+opt['key-file']
		if opt['offset']!="":
			optarg+="--offset="+opt['offset']
		if opt['size']!="":
			optarg+="--size="+opt['size']

		#options valid, open
		print "CSPlain:copen:[SUDO] opening plain..."
		if optarg!="":
			p=subprocess.Popen(["sudo","cryptsetup","open","--type=plain",
				"--hash="+opt['hash'],"--cipher="+opt['cipher']+"-"+opt['mode'],
				"--key-size="+opt['key-size'], optarg, opt['loc'],opt['mntloc']],
				stdout=subprocess.PIPE, universal_newlines=False)
		else:
			p=subprocess.Popen(["sudo","cryptsetup","open","--type=plain",
				"--hash="+opt['hash'],"--cipher="+opt['cipher']+"-"+opt['mode'],
				"--key-size="+opt['key-size'], opt['loc'],opt['mntloc']],
				stdout=subprocess.PIPE, universal_newlines=False)
		print p.communicate()

	def cclose(self,loc):
		print "CSPlain:copen:[SUDO] closing plain..."
		p=subprocess.Popen(["sudo","cryptsetup","close",loc])
		print p.communicate()
		
#TEST
#wrapPlain=WrapCSPlain()
#options=dict()
#req args
#options['cipher']='aes'
#options['hash']='sha512'
#options['key-size']='512'
#options['mode']='xts-plain64'
#options['loc']="testfile"
#options['mntloc']="mapper0"
#opt args
#options['offset']=""
#options['key-file']=""
#options['size']=""
#print wrapPlain.copen(options)
#print wrapPlain.cclose("mapper0")
		