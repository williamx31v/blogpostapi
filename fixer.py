#/usr/bin/python3

#Import modules
import gzip, time, os
from time import mktime
from datetime import datetime

#Get source directory
inlog = input('Enter source directory: ')

#Build list of files
inlog = os.path.abspath(inlog)
indir =  os.listdir(inlog)
outlog = indir

#Create a timestamp
struct_time = time.gmtime()
dt = datetime.fromtimestamp(mktime(struct_time))
dt = str(dt)

#Function to remove PII
def fixer(inlog, outlog):
	#Counters
	count = 0
	saved = 0
	#Preserve file metadata
	shutil.copy2(inlog, outlog)
	#Open files and write to new file only entries without PII
	infile = gzip.open(inlog, 'rt', encoding='utf-8')
	outfile = gzip.open(outlog, 'wt', encoding='utf-8')
	auditfile = open('fixer_audit.log', 'a')
	SSN = 'SSN=\"'
	CC = 'CC=\"'
	f = infile.readlines()
	for line in f[:]:
		if SSN in line:
			f.remove(line)
			count +=1
		elif CC in line:
			f.remove(line)
			count +=1
		else:
			outfile.write(line)
			saved +=1
	#Write audit log
	count = str(count)
	saved = str(saved)
	auditfile.write(dt)
	auditfile.write(' ')
	auditfile.write(count)
	auditfile.write(' ')
	auditfile.write(saved)
	auditfile.write(' ')
	auditfile.write(inlog)
	auditfile.write(' ')
	auditfile.write(outlog)
	auditfile.write(' ')
	auditfile.write('\n')
	
	#Close things up
	infile.close()
	outfile.close()
	auditfile.close()
	
#Pass source directory to function
for filename in indir:
	filepath = os.path.join(inlog, filename)
	if not filepath.endswith('gz'):
		filepath.strip(filename)
	elif filepath.endswith('gz'):
		outlog = (filepath) + ('_fixed')
		fixer(filename, outlog)


