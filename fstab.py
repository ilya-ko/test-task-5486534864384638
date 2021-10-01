#!/usr/bin/env python3

# pip3 install --user pyyaml

import sys

try:
    import yaml
except:
    print ('Fatal error:  Yaml library is not available')
    sys.exit(3)								# exit with code 3


def display_help():
	print("Usage: "+sys.argv[0]+" inputfile outputfile")		# display help

infile=sys.argv[1]
outfile=sys.argv[2]

try:
	newfile_object=open(outfile, "w")
except:
	print("Could not open the output file "+sys.argv[2]+" for writing, nothing to do else here..")
	sys.exit(2)							# exit with code 2

try:
	open(infile)
except FileNotFoundError:
	print("Input file not found")					# if input file was not found:
	display_help()							# display help and
	sys.exit(1)							# exit with code 1

with open(infile, "r") as f:
	data = yaml.safe_load(f)
	print(data)
list_of_resources=[]							# initializing list of resources to mount


#	print(((data['fstab'])['/dev/sda1'])['mount'])
for resource in (data['fstab']):
	list_of_resources.append(resource)				# add resources to list, one by one

for i in range(0,len(list_of_resources)):
	resource=list_of_resources[i]

	print("Processing resource "+resource)
	try:
		resource+=":"+data['fstab'][list_of_resources[i]]['export']
	except KeyError:
		print("export not found")

	mountpoint=data['fstab'][list_of_resources[i]]['mount']
	print("Mountpoint: "+mountpoint)
	fstype=data['fstab'][list_of_resources[i]]['type']
	print("Filesystem: "+fstype)
	options="defaults"
	try:
		mountopts=data['fstab'][list_of_resources[i]]['options']
		for mountopt in mountopts:
			print("Option "+mountopt)
			options+=mountopt+","
	except KeyError:
		print("Options not found")
	except TypeError:
		print("Many options, list of them")
	if (options!="defaults"):
		print("We need to remove symbols")
		options=options[:-1]							# remove last symbol
		options=options.replace("defaults", "")
	newline=str(resource+" "+mountpoint+" "+fstype+" "+options+" 0 0\n")
	print(newline)
	newfile_object.write(newline)

newfile_object.close()									# close the output file
