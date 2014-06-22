import CSEUWrapCSPlain
import CSEUWrapDD

#in progress
class CSEUContainer:
	hopt=dict()
	dopt=dict()

	def createFile(self,size,fill,loc):
		if fill=="rand":
			fill="/dev/urandom"
		elif fill=="zero":
			fill="/dev/zero"
		else:
			return "ERROR"

		ddWrap=CSEUWrapDD()
		ddWrap.dd(inf=fill,outf=loc,bs="1M",count=str(size))

	def setHopt():
		hopt['cipher']='aes'
		hopt['hash']='sha512'
		hopt['key-size']='512'
		hopt['mode']='xts-plain64'
		hopt['loc']='testfile'
		hopt['size']='32'

#Test
cs_container=CSEUContainer()
cs_container.createFile(20,"zero","dumpfile")

options=dict()
options['cipher']='aes'
options['hash']='sha512'
options['key-size']='512'
options['mode']='xts-plain64'
options['loc']="testfile"
options['mntloc']="mapper0"
options['size']=