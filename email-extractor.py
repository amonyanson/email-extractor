import re
import time

def textextractor(text):
	def extractedemails(text):
		regex = r'[a-zA-Z0-9\.\+-_]+@[a-zA-Z0-9\.\+-_]+\.[a-zA-Z]+'
		emaillist = re.findall(regex,text)
		return emaillist
	text = input("Paste text containing emails here:\n")
	emails = extractedemails(text)
	time.sleep(1)
	print("Extracted emails:\n")
	time.sleep(0.5)
	for key in emails:
		time.sleep(0.5)
		print(key)
		time.sleep(0.5)
		print("Successfully done!")
		time.sleep(0.5)
def url extractor():
	def extractedemails(url):
		import requests
		from bs4 import BeautifulSoup
		response = requests.get(url)
		soup = BeautifulSoup(response.text,'html.parser')
		regex = r'[a-zA-Z0-9\.\+-_]+@[a-zA-Z0-9\.\+-_]+\.[a-zA-Z]+'
		emaillist = re.findall(regex,str(soup))
		return emaillist
	url = input("Paste url containing emails here:\n")
	url = url.lower()
	emails = extractedemails(url)
	time.sleep(0.5)
	print("Extracted Emails:\n")
	time.sleep(0.5)
	for key in emails:
		time.sleep(0.5)
		print(key)
		time.sleep(0.5)
		print("Successfully done!")
		time.sleep(0.5)
def newgame():
	user_input = input("""Choose an option on how you'd want to extract target emails:
1: Through text
2: Through url
reply with [text or url]:
""")
	if user_input == "text":
		time.sleep(0.5)
		textextractor()
	elif user_input == "url":
		time.sleep(0.5)
		urlextractor()
	else:
		time.sleep(1)
		print("Invalid user input")
def again():
	respond = input("Scan again? [yes/no]:\n")
	respond = respond.lower()
	if respond == "yes":
		return True
	else:
		return False
newgame()
while again():
	newgame()
