import random
list= list()
def crypto(out):
####
	if out==1073: list.append(9)
	if out==1261: list.append(0)
	if out==1138: list.append(12)
	if out==1855: list.append(15)
	if out==1920: list.append(22)
	if out==1368: list.append(5)
	if out==1318: list.append(0)
	if out==1986: list.append(25)
	if out==1624: list.append(15)
	if out==1253: list.append(21)
	if out==1988: list.append(0)
	if out==1680: list.append(19)
	if out==1928: list.append(8)
	if out==1602: list.append(9)
	if out==1012: list.append(6)
	if out==1555: list.append(1)
	if out==1682: list.append(9)
	if out==1076: list.append(0)
	if out==1999: list.append(12)
	if out==1690: list.append(15)
	if out==1281: list.append(22)
	if out==1672: list.append(5)
	if out==1754: list.append(0)
	if out==1391: list.append(25)
	if out==1469: list.append(15)
	if out==1157: list.append(21)
	if out==1506: list.append(0)
	if out==1060: list.append(19)
	if out==1683: list.append(8)
	if out==1537: list.append(9)
	if out==1682: list.append(6)
	if out==1587: list.append(1)
	if out==1398: list.append(9)
	if out==1795: list.append(0)
	if out==1799: list.append(12)
	if out==1627: list.append(15)
	if out==1052: list.append(22)
	if out==1817: list.append(5)
	if out==1396: list.append(0)
       # if out==3333: list.append(9)
	if out==1798: list.append(25)
	if out==1307: list.append(15)
	if out==1390: list.append(21)
	if out==1607: list.append(0)
	if out==1120: list.append(19)
	if out==1429: list.append(8)
	if out==1856: list.append(6)
	if out==1418: list.append(1)
	if out==1073: list.append(9)
	if out==1261: list.append(0)
	if out==1138: list.append(12)
	if out==1855: list.append(15)
	if out==1920: list.append(22)
	if out==1368: list.append(5)
	if out==1318: list.append(0)
	if out==1986: list.append(25)
	if out==1624: list.append(15)
	if out==1253: list.append(21)
	if out==1988: list.append(0)
	if out==1680: list.append(19)
	if out==1928: list.append(8)
	if out==1602: list.append(9)
	if out==1012: list.append(6)
	if out==1555: list.append(1)
	if out==1398: list.append(9)
	if out==1795: list.append(0)
	if out==1799: list.append(12)
	if out==1627: list.append(15)
	if out==1052: list.append(22)
	if out==1817: list.append(5)
	if out==1396: list.append(0)
	if out==1798: list.append(25)
	if out==1307: list.append(15)
	if out==1390: list.append(21)
	if out==1607: list.append(0)
	if out==1120: list.append(19)
	if out==1429: list.append(8)
	if out==1635: list.append(9)
	if out==1856: list.append(6)
	if out==1418: list.append(1)

	
	
alpha=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n', 'o','p','q','r','s','t','u','v','w','x','y','z']
n=0
sed=input("Please Enter the day arean love most but you hate:(DDMMYYYY):")
random.seed(sed)
while n<16:
	out1=random.randint(1000,2000)
	crypto(out1)
	n+=1

if len(list)>14:
    del list[1]
    del list[14]
    



line=[]
for item in list:
	line.append(alpha[item])
for word in line:
	print(word,end="")
