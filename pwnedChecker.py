#!/usr/bin/python3
# Author: Jose Angel Loarces
# Contact: https://goo.gl/zfGmre
# Last Update: 14/03/2019 (DD/MM/YY)

import time
import requests
import argparse


def main():
	# Arguments parse
	parser = argparse.ArgumentParser(description="Pwned Checker - v1.0")
	parser.add_argument('-e', '--email', dest="email", help="Checks a single email", type=str)
	parser.add_argument('-f', '--filename', dest="filename", help="Checks a list of emails given in a file (one per line)", type=str)
	parser.add_argument('-o', '--output', dest="output", help="Changes the default output file name (pwned_log.txt)", type=str, default="pwned_log.txt")
	parser.add_argument('-u', '--unverified', dest="unverified", help="Include unverified breaches too (boolean)", type=bool, default=False)
	
	args = parser.parse_args()

	email = args.email
	filename = args.filename
	output = args.output
	unverified = args.unverified

	rate = 1.5	# Change it if needed, but this is the lowest secure value for working (https://haveibeenpwned.com/API/v2#RateLimiting)

	log = open(output, 'w')

	if email != None:
		print(checkMail(email, unverified))
	elif filename != None:
		try:
			for email in open(filename):
				email = email.replace('\n', '')
				result = checkMail(email, unverified)
				print(result)
				log.write(result + '\n')	# Writes in the log file
				time.sleep(rate)			# Sleeps the rate limit
		except IOError:
			print("[ERROR] The file " + filename + " has not been found.")
	else:
		parser.print_help()

def siteParser(request):
	sites = []
	for site in request.split(','):
		sites.append(site[9:-2])		# Initially, it has the format: {"Name": "site"}, so we parse that
	return sites

def showResults(email, sites):
	# Format and returns the results
	s = 'Mail: {} - ({} sites)\n'.format(email, str(len(sites)))
	for site in sites:
		s += '\t* {}\n'.format(site)
	return s[:-1]

def checkMail(email, unverified):
	headers = {'User-Agent': 'Pwn-Checker-v1.0'}	# It must have an user agent (https://haveibeenpwned.com/API/v2#UserAgent)"
	url = 'https://haveibeenpwned.com/api/v2/breachedaccount/{}?truncateResponse=true&includeUnverified={}'.format(email, str(unverified))

	r = requests.get(url, headers=headers)
	# Request status codes (https://haveibeenpwned.com/API/v2#ResponseCodes)
	if r.status_code == 200:
		sites = siteParser(r.text[1:-1])
		return showResults(email, sites)
	elif r.status_code == 403:
		return "[ERROR 403] No user agent has been specified!"
	elif r.status_code == 404:
		return 'Mail: {} has not been pwned!'.format(email)
	elif r.status_code == 429:
		return '[WARNING] Rate limit has been exceeded! Sleeping 2 seconds...'
		time.sleep(2)

if __name__ == "__main__":
	main()
