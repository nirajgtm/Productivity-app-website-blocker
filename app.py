from sys import platform
import re
import time
from datetime import datetime as dt

if platform == "linux" or platform == "linux2" or platform=="darwin":
	hosts_path = "/etc/hosts"
	print("Your System is UNIX")
elif platform == "win32":
	hosts_path = "C:\\Windows\\System32\\drivers\\etc"
	print("Your System is Windows")
else:
	a= input ("Coudn't determine Operating system \n Enter 1 for Windows \n Enter 2 For Linux or OSX")
	if a==1:
		hosts_path = "C:\\Windows\\System32\\drivers\\etc"
	elif a==2:
		hosts_path = "/etc/hosts"
	else:
		print("Wrong Input, Please Try Again")

redirect = "127.0.0.1"
sites = []

while True:
	site = input("What site do you want to block?\n Enter in format \"abc.com\"\n input anything else to skip  ")
	if re.search(r'[a-z0-9-]+\.(?:com)(?:\.[a-z]{2,3})?', site):
		print(site + " added to block list")
		sites.append(site)
		sites.append("www." + site)
	else:
		print("skipping")
		break
print(sites)
host_temp = "hosts"

while True: 
	if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17):
		print("\ncurrent time is under working hours... \n Sites are blocked. \n")
		with open(host_temp, 'r+') as file:
			content = file.read()
			for site in sites:
				if site in content:
					pass
				else:
					file.write(redirect + " " + site + "\n")
	else:
		print("Sites are not blocked, current time is")
		print(dt.now())
	time.sleep(10)








# websites_list = ["www.facebook.com", "facebook.com", "web.whatsapp.com"]