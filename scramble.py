import random
fin = open("names.txt").read().splitlines()

for i in range(int(len(fin)**3)):
	j = random.randint(0,len(fin)-1)
	k = random.randint(0,len(fin)-1)
	fin[j], fin[k] = fin[k], fin[j]

fout = open("out.txt","wb")
for i in fin:
	fout.write(i + "\n")
fout.close()
print "Done!"
