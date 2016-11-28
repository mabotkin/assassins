import email.mime.text
import getpass
import smtplib
import random
from time import time

USERNAME = "2017awang"
print("Enter password for " + USERNAME)
PASSWORD = getpass.getpass()

VERBOSE = True

tic = time()
fin = open("names.txt").read().splitlines()
for i in range(len(fin)):
	fin[i] = fin[i].split("|")

for i in range(int(len(fin)**3)):
	j = random.randint(0,len(fin)-1)
	k = random.randint(0,len(fin)-1)
	fin[j], fin[k] = fin[k], fin[j]

fout = open("out.txt","w")
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
	message = ("Hello {},\n\nYour target for assassins is {}.  Good luck!\n\n-AutoModerator\n\nThis is an automated message.").format(fin[i][0],fin[target][0])
	msg = email.mime.text.MIMEText(message)
	msg['Subject'] = "Assassins Target"
	msg['From'] = addr
	msg['To'] = fin[i][1]
	s.send_message(msg)
	if VERBOSE:
		print("Message sent to", fin[i][0])

s.quit()		
toc = time()
if VERBOSE:
	print(str(toc-tic) + " seconds elapsed")
print("Done!")
