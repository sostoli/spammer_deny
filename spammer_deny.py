# Spammer deny by sosto


import argparse
import subprocess
import re


# # Add in argument options
parser = argparse.ArgumentParser(description='Use this script to parse mail.log (for postfix and dovecot)\n to catch Spammer ip adresses and deny them with ufw automatically')
parser.add_argument('-f', action='store', dest='file',
                    help='The log file to parse')

results = parser.parse_args()

# 
if results.file == None:
	print ("Please enter the log file from which you will retrieve the IP adresses")
	exit()
else:
	file = results.file

regex = r"(\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?)(?=]: SASL LOGIN authentication failed)"



with open(file, 'rb') as logs:
	logfile = logs.read()
	logs.close()

subprocess.call("ufw enable",shell=True)
matches = re.findall(regex, logfile)
for match in matches:

    print("IP: %s" % (match))
    subprocess.call("ufw deny from "+match+" to any",shell=True)

