from xml.etree import ElementTree
import sys
import os, errno
import array
from subprocess import call

#This function lists the files within a given directory dir
def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]
	
	
	
def main(argv=None):

	print "Parsing arguments..."
	if argv is None:
		argv = sys.argv

	filenamesX3D = filter(lambda x: ".x3d" in x, listdir_fullpath(argv[1]))

	if len(filenamesX3D) > 0:
	 for fi in filenamesX3D :
		print fi
		newfi = fi.split('.')
		basename = str(newfi[0])+str(newfi[1])
		outp = './'+ basename+'_aopt.x3d'
		print outp	 

		try:
			#r1 = call("mkdir "+ argv[1] +"/"+ str(newfi[0]) , shell=True)
			#print (r1)
			retcode = call("aopt" + " -i "+str(fi)+" -F Scene -G "+ str(newfi[0]) +"/:sacp -x "+str(outp), shell=True) 
			#
				#call(["ls", "-l"])
			if retcode < 0:
				print >>sys.stderr, "Child was terminated by signal", -retcode
			else:
				print >>sys.stderr, "Child returned", retcode
		except OSError as e:
			print >>sys.stderr, "Execution failed:", e
			

	 
	#if len(argv):
	#	print "Usage: command <InputFolder> <OutputFilename>"
	#	print "	<InputFolder> must contain only one set of X3D files to be processed"
	#	print "	<OutputFilename> must contain the path and base name of the desired output, extension will be added automatically"
	#	print "Note: this version does not process several folders recursively. "
	#	print "You typed:", argv
	#	return 2
		
	print "done file loop"
	
if __name__ == "__main__":
    main()
			