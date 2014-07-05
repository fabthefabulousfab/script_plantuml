##################################################
#
#	IMpot
#
#################################################

import subprocess
import shlex
import packet


##################################################
#
#	Constants
#
#################################################

# Genrals imports
HEADER = "tshark -r"
PROTOCOL = '''  -nn -T fields -R  'http || sip || msrp' ''' 

FILTRE = """ -e frame.protocols""" 					#0
FILTRE = FILTRE + """ -e frame.number""" 			#1
FILTRE = FILTRE + """ -e frame.time_delta""" 		#2
FILTRE = FILTRE + """ -e ip.src """					#3
FILTRE = FILTRE + """ -e ip.dst  """				#4

FILTRE = FILTRE + """ -e sip.Method """				#5
FILTRE = FILTRE + """ -e sip.Status-Code""" 		#6

FILTRE = FILTRE + """ -e msrp.method """			#7
FILTRE = FILTRE + """ -e msrp.data """				#8
FILTRE = FILTRE + """ -e msrp.status.code"""		#9

FILTRE = FILTRE + """ -e diameter.cmd.code  """		#10


array_color_http=['blue','orange']
array_color_msrp=['blue','orange']
array_color_diameter=['blue','orange']
array_color_sip=['blue','orange']

all_packets = []

##################################################
#
#	Functions
#
#################################################


def extract(file):
	output = subprocess.check_output(shlex.split(HEADER+ file+PROTOCOL+FILTRE))
	lines = output.splitlines()
	for i in lines:
		attr_list = i.split('\t')
		if ('sip' in attr_list[0] ):
			print (attr_list[0])
			newpacket = packet.Sip_packet(attr_list[0],attr_list[1],attr_list[2],attr_list[3],attr_list[4],attr_list[5],attr_list[6])
  			print(newpacket.ip_src)
  			print(newpacket.method)
  			print(newpacket.request_name)

##################################################
#
#	Main
#
#################################################

print ('begin')


file ='/tmp/capture.cap'

extract(file)

print ('end')
