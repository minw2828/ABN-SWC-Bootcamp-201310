file_name = 'test.csv'
default_file = '/home/swc_trainee/bootcamp2013/day1/classes_objects/rodents.csv'

try:
	file = open(file_name)
except IOError as e:
	'''
	Only raise the exception if there is an IO error
	'''
	file = open(default_file)
except:
	'''
	Catch other errors other than IO errors
	'''
	print 'There was some other problem'
	raise

print file.readline()
