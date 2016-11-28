import email.mime.text
import getpass
import smtplib
import random
from time import time

USERNAME = "2017awang"
print("Enter password for " + USERNAME)
PASSWORD = getpass.getpass()

VERBOSE = True
EMAIL = False #safety switch

WEAPON = open("config/weapon.txt").read()
IMMUNITY = open("config/immunity.txt").read()

tic = time()
fin = open("config/names.txt").read().splitlines()
for i in range(len(fin)):
	fin[i] = fin[i].split("|")

random.shuffle(fin)

fout = open("config/out.txt","w")
for i in fin:
	i[0] = i[0].strip()
	i[1] = i[1].strip()
	fout.write(i[0] + "\n")
fout.close()

s = smtplib.SMTP_SSL('smtp.tjhsst.edu')
s.login(USERNAME, PASSWORD)

for i in range(len(fin)):
	target = i+1
	if i == len(fin)-1:
		target = 0
	addr = USERNAME + '@tjhsst.edu'
	message = ("Hello {},\n\nYour target for assassins is {}.\n{}\n{}\nGood luck!\n\n-AutoModerator\n\nThis is an automated message.").format(fin[i][0],fin[target][0],WEAPON,IMMUNITY)
	msg = email.mime.text.MIMEText(message)
	msg['Subject'] = "Assassins Target"
	msg['From'] = addr
	msg['To'] = fin[i][1]
	if EMAIL:
		try:
			s.send_message(msg)
			if VERBOSE:
				print("Message sent to", fin[i][0])
		except:
			print("Error sending message to", fin[i][0])
mods = open("config/mod.txt").read().splitlines()
for i in mods:
	addr = USERNAME + '@tjhsst.edu'
	message = "Hello Moderator,\n\nHere is the assassins targeting list:\n\n"
	message += ("Total Participants: " + str(len(fin)) + "\n")
	for j in fin:
		message += (j[0] + "\n")
	message += "\n-AutoModerator\n\nThis is an automated message."
	msg = email.mime.text.MIMEText(message)
	msg['Subject'] = "Assassins List"
	msg['From'] = addr
	msg['To'] = i
	if EMAIL:
		try:
			s.send_message(msg)
		except:
			print("Error sending moderator message to", i)
	if VERBOSE:
		print("Moderator Message sent to", i)

s.quit()		
toc = time()
if VERBOSE:
	print(str(toc-tic) + " seconds elapsed")
print("Done!")
