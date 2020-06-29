from pprint import pprint

SysProc = [["   10 root        4 155 ki31     0K    64K CPU3    3    ??? 325.54% idle",
"   11 root       25 -60    -     0K   400K WAIT   255 3409.0  71.68% intr",
"13538 root        2 -26  r26   892M 31576K nanslp  1 552.3H   5.47% chassisd",
"13586 root        1  21    0   715M  5296K select  3 213:30   1.46% eventd"],
["   10 root        4 155 ki31     0K    64K CPU3    3    ??? 325.54% idle",
"   11 root       25 -60    -     0K   400K WAIT   255 3409.0  56.69% intr",
"13538 root        2 -26  r26   892M 31576K nanslp  1 552.3H   5.47% chassisd",
"13586 root        1  21    0   715M  5296K select  3 213:30   1.46% eventd"],
["   10 root        4 155 ki31     0K    64K CPU3    3    ??? 325.54% idle",
"   11 root       25 -60    -     0K   400K WAIT   255 3409.0  61.38% intr",
"13538 root        2 -26  r26   892M 31576K nanslp  1 552.3H   5.47% chassisd",
"13586 root        1  21    0   715M  5296K select  3 213:30   1.46% eventd"],
["   10 root        4 155 ki31     0K    64K CPU3    3    ??? 325.54% idle",
"   11 root       25 -60    -     0K   400K WAIT   255 3409.0  71.64% intr",
"13538 root        2 -26  r26   892M 31576K nanslp  1 552.3H   5.47% chassisd",
"13586 root        1  21    0   715M  5296K select  3 213:30   1.46% eventd"],
["   10 root        4 155 ki31     0K    64K CPU3    3    ??? 325.54% idle",
"   11 root       25 -60    -     0K   400K WAIT   255 3409.0  74.61% intr",
"13538 root        2 -26  r26   892M 31576K nanslp  1 552.3H   5.47% chassisd",
"13586 root        1  21    0   715M  5296K select  3 213:30   1.46% eventd"]]


VMStatI = [["interrupt                          total       rate",
"irq4: uart0                         5687          0",
"irq5: uart2                            8          0",
"irq14: ata0                     14915620        100",
"irq15: ata1                            1          0",
"irq18: ichsmb0             5344101346867     145045",
"irq23: ehci0                    55269622          1",
"irq39: acb0                            1          0",
"cpu0:timer                   34533005999        937",
"irq256: em0                  13119211319        356",
"irq257: em1                    930213042         25",
"irq258: em2                     36843750          0",
"cpu2:timer                   21487792492        583",
"cpu3:timer                   21368494440        579",
"cpu1:timer                   21774635040        590",
"Total                      5457421733888     148120"],
["interrupt                          total       rate",
"irq4: uart0                         5687          0",
"irq5: uart2                            8          0",
"irq14: ata0                     24915620        200",
"irq15: ata1                            1          0",
"irq18: ichsmb0             5344101346867     145045",
"irq23: ehci0                    55269622          1",
"irq39: acb0                            1          0",
"cpu0:timer                   34533005999        937",
"irq256: em0                  13119211319        356",
"irq257: em1                    930213042         25",
"irq258: em2                     36843750          0",
"cpu2:timer                   21487792492        583",
"cpu3:timer                   21368494440        579",
"cpu1:timer                   21774635040        590",
"Total                      5457421733888     148120"],
["interrupt                          total       rate",
"irq4: uart0                         5687          0",
"irq5: uart2                            8          0",
"irq14: ata0                     34915620        300",
"irq15: ata1                            1          0",
"irq18: ichsmb0             5344101346867     145045", 
"irq23: ehci0                    55269622          1",
"irq39: acb0                            1          0",
"cpu0:timer                   34533005999        937",
"irq256: em0                  13119211319        356",
"irq257: em1                    930213042         25",
"irq258: em2                     36843750          0",
"cpu2:timer                   21487792492        583",
"cpu3:timer                   21368494440        579",
"cpu1:timer                   21774635040        590",
"Total                      5457421733888     148120"], 
["interrupt                          total       rate",
"irq4: uart0                         5687          0",
"irq5: uart2                            8          0",
"irq14: ata0                     44915620        400",
"irq15: ata1                            1          0",
"irq18: ichsmb0             5344101346867     145045",
"irq23: ehci0                   555269622         51", 
"irq39: acb0                            1          0",
"cpu0:timer                   34533005999        937",
"irq256: em0                  13119211319        356",
"irq257: em1                    930213042         25",
"irq258: em2                     36843750          0",
"cpu2:timer                   21487792492        583",
"cpu3:timer                   21368494440        579",
"cpu1:timer                   21774635040        590",
"Total                      5457421733888     148120"],
["interrupt                          total       rate",
"irq4: uart0                         5687          0",
"irq5: uart2                            8          0",
"irq14: ata0                     54915620        500", 
"irq15: ata1                            1          0",
"irq18: ichsmb0             5344101346867     145045",
"irq23: ehci0                    55269622          1",
"irq39: acb0                            1          0",
"cpu0:timer                   34533005999        937",
"irq256: em0                  13119211319        356",
"irq257: em1                    930213042         25",
"irq258: em2                     36843750          0",
"cpu2:timer                   21487792492        583",
"cpu3:timer                   21368494440        579",
"cpu1:timer                   21774635040        590",
"Total                      5457421733888     148120"]]

IntrLvlLst = []
iterIntrPresent = "FALSE"
# Even if one iteration of the System process had no Interrupt CPU usage, then the script will stop execution
for Iter in SysProc:
	for Proc in Iter:
		if "intr" in Proc:
			iterIntrPresent = "TRUE"
			IntrLvlLst.append((Proc.strip("% intr")).split(" ")[-1])
	if not iterIntrPresent:
		exit()
	else:
		iterIntrPresent = "FALSE"
HighIntr = "TRUE"
for itr in range(5):
	if float(IntrLvlLst[itr]) < 50.00:
		HighIntr = "FALSE"
print("Interrupt constant high is : ",HighIntr)

#Q2
IRQList = {}
for Iterlst in VMStatI:
	Iterlst.pop(0)
	lengt = len(Iterlst)
	for irqno in Iterlst:
		if "Total" in irqno:
			t = irqno.split(" ")
			a = [":"]
			irqno = " ".join(t[:1]+a+t[2:])
			#irqno.replace("Total ","Total0")
		if irqno.split(":")[0] in IRQList:
			TmpLst = []
			existingVal = IRQList[irqno.split(":")[0]]
			if type(existingVal) is list:
				existingVal = ' '.join(existingVal)
			TmpLst.append(existingVal)
			tempV = [' '.join(irqno.split())][0].split(" ")[-2]
			TmpLst.append(tempV)
			IRQList[irqno.split(":")[0]] = TmpLst
		else:
			temp = [' '.join(irqno.split())][0].split(" ")[-2]
			IRQList[irqno.split(":")[0]] = temp
TmpLst = []
ConstantRaise = False
for keyK, ValueV in IRQList.items():
	ValueV = ' '.join(ValueV)
	TmpLst = ValueV.split(" ")
	IRQList[keyK] = TmpLst
for keyK, ValueV in IRQList.items():
	for i in range(5):
		if "Total" in keyK:
			break
		else:
			if int(IRQList[keyK][i]) > 0.6 * int(IRQList["Total "][i]):
				print("The interrupt %s is observed with more than 60 % of Total CPU interrupt:",keyK,".")
				break
for keyK, ValueV in IRQList.items():
	for i in range(4):
		if "Total" in keyK:
			break
		else:
			if int(IRQList[keyK][i]) > 1.1 * int(IRQList[keyK][i+1]):
				print("The interrupt %s is observed with more than 10 % spike:",keyK,".")
				break
for keyK, ValueV in IRQList.items():
	for i in range(4):
		if int(IRQList[keyK][i+1]) > int(IRQList[keyK][i]):
			ConstantRaise = "TRUE"
		else:
			ConstantRaise = "FALSE"
	if ConstantRaise == "TRUE":
		print("The interrupt %s is observed with constant raise",keyK,".")
#pprint(IRQList)


'''
sivaa@sivaa-mbp Module 2 % python3 IntrChk.py
Interrupt constant high is :  TRUE
The interrupt %s is observed with more than 60 % of Total CPU interrupt: irq18 .
The interrupt %s is observed with more than 10 % spike: irq23 .
The interrupt %s is observed with constant raise irq14 .
sivaa@sivaa-mbp Module 2 % 
'''

'''
Interrupt constant high is :  TRUE
{'Total ': ['5457421733888',
            '5457421733888',
            '5457421733888',
            '5457421733888',
            '5457421733888'],
 'cpu0': ['34533005999',
          '34533005999',
          '34533005999',
          '34533005999',
          '34533005999'],
 'cpu1': ['21774635040',
          '21774635040',
          '21774635040',
          '21774635040',
          '21774635040'],
 'cpu2': ['21487792492',
          '21487792492',
          '21487792492',
          '21487792492',
          '21487792492'],
 'cpu3': ['21368494440',
          '21368494440',
          '21368494440',
          '21368494440',
          '21368494440'],
 'irq14': ['14915620', '24915620', '34915620', '44915620', '54915620'],
 'irq15': ['1', '1', '1', '1', '1'],
 'irq18': ['5344101346867',
           '5344101346867',
           '5344101346867',
           '5344101346867',
           '5344101346867'],
 'irq23': ['55269622', '55269622', '55269622', '555269622', '55269622'],
 'irq256': ['13119211319',
            '13119211319',
            '13119211319',
            '13119211319',
            '13119211319'],
 'irq257': ['930213042', '930213042', '930213042', '930213042', '930213042'],
 'irq258': ['36843750', '36843750', '36843750', '36843750', '36843750'],
 'irq39': ['1', '1', '1', '1', '1'],
 'irq4': ['5687', '5687', '5687', '5687', '5687'],
 'irq5': ['8', '8', '8', '8', '8']}

'''



'''
JARGANDS:
-------------
MULTI SPACED STRING TO SINGLE SPACED STRING:
=============================================
>>> i = "This    is    a     way      to    have      a     single    space     in        multi       space     string"
>>> ' '.join(i.split())
'This is a way to have a single space in multi space string'

>>> [' '.join(i.split())]
['This is a way to have a single space in multi space string']
>>> [' '.join(i.split())][0].split(" ")
['This', 'is', 'a', 'way', 'to', 'have', 'a', 'single', 'space', 'in', 'multi', 'space', 'string']
>>> [' '.join(i.split())][0].split(" ")[0]
'This'
>>> [' '.join(i.split())][0].split(" ")[-1]
'string'



>>> [' '.join(i.split())][0].split(" ")[0]
'This'
>>> 

>>> [' '.join(i.split())][0].split(" ")[-1]
'string'
>>> 


LIST TO STRING:
===============
>>> i = ['This', 'is', 'a', 'multi', 'space', 'string']
>>> ''.join(i)
'Thisisamultispacestring'
>>> ' '.join(i)
'This is a multi space string'
>>> 


'''	

'''Find if overall interrupt in the 1st list Sys_Proc has been high at 50% of the RE CPU consistently in the 5 iterations. If observed then perform the below.
a) at any instance, does any interrupt is at large above 60% of overall. 
b) at any instance, does any any interrupt shows a spikes by 10% high than the previous one. 
c) Among the instances, a particular interrupt is at a raise constantly.

ANS:
"irq18: ichsmb0             5344101346867     145045", .................(a)
"irq23: ehci0                   555269622         51", .................(b)
"irq14: ata0                     54915620        500", .................(c)
'''

