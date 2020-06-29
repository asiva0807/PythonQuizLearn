from pprint import pprint
TED_DB = ["1.21.0.1-1 Net 7104 2 2 OSPF(0.0.0.0) To: 1.1.1.1, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 21.21.21.21, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"1.1.1.1 Rtr 6613 3 3 OSPF(0.0.0.0) To: 101.1.0.101-1, Local: 101.1.0.1, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 1.21.0.1-1, Local: 1.21.0.1, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 1.22.0.22-1, Local: 1.22.0.1, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"2.51.0.2-1 Net 6811 2 2 OSPF(0.0.0.0) To: 51.51.51.51, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 2.2.2.2, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"2.2.2.2 Rtr 4385 3 3 OSPF(0.0.0.0) To: 102.2.0.102-1, Local: 102.2.0.2, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 2.51.0.2-1, Local: 2.51.0.2, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 2.52.0.52-1, Local: 2.52.0.2, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"21.31.0.21-1 Net 6891 2 2 OSPF(0.0.0.0) To: 21.21.21.21, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 31.31.31.31, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"21.21.21.21 Rtr 6891 2 2 OSPF(0.0.0.0) To: 1.21.0.1-1, Local: 1.21.0.21, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 21.31.0.21-1, Local: 21.31.0.21, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"1.22.0.22-1 Net 6613 2 2 OSPF(0.0.0.0) To: 1.1.1.1, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 22.22.22.22, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"22.22.22.22 Rtr 6471 2 1 OSPF(0.0.0.0) To: 1.22.0.22-1, Local: 1.22.0.22, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"31.31.31.31 Rtr 6881 2 2 OSPF(0.0.0.0) To: 21.31.0.21-1, Local: 21.31.0.31, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 31.41.0.41-1, Local: 31.41.0.31, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"22.32.0.32-1 Net 6471 1 2 OSPF(0.0.0.0) To: 22.22.22.22, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 32.32.32.32, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"32.32.32.32 Rtr 6471 2 2 OSPF(0.0.0.0) To: 32.42.0.42-1, Local: 32.42.0.32, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 22.32.0.32-1, Local: 22.32.0.32, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"31.41.0.41-1 Net 6879 1 2 OSPF(0.0.0.0) To: 31.31.31.31, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 41.41.41.41, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"51.41.0.41-1 Net 6822 1 2 OSPF(0.0.0.0) To: 41.41.41.41, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 51.51.51.51, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"41.41.41.41 --- 6822 2 0 ",
"32.42.0.42-1 Net 6510 2 2 OSPF(0.0.0.0) To: 42.42.42.42, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 32.32.32.32, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"52.42.0.42-1 Net 6510 2 2 OSPF(0.0.0.0) To: 42.42.42.42, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 52.52.52.52, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"42.42.42.42 Rtr 6510 2 2 OSPF(0.0.0.0) To: 32.42.0.42-1, Local: 32.42.0.42, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 52.42.0.42-1, Local: 52.42.0.42, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"51.51.51.51 Rtr 6811 2 2 OSPF(0.0.0.0) To: 51.41.0.41-1, Local: 51.41.0.51, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 2.51.0.2-1, Local: 2.51.0.51, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"2.52.0.52-1 Net 4385 2 2 OSPF(0.0.0.0) To: 2.2.2.2, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 52.52.52.52, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"52.52.52.52 Rtr 4385 2 2 OSPF(0.0.0.0) To: 52.42.0.42-1, Local: 52.42.0.52, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 2.52.0.52-1, Local: 2.52.0.52, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"101.1.0.101-1 Net 10195 2 2 OSPF(0.0.0.0) To: 1.1.1.1, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 101.101.101.101, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"101.101.101.101 Rtr 10195 1 1 OSPF(0.0.0.0) To: 101.1.0.101-1, Local: 101.1.0.101, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"102.2.0.102-1 Net 6811 2 2 OSPF(0.0.0.0) To: 102.102.102.102, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0 To: 2.2.2.2, Local: 0.0.0.0, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0",
"102.102.102.102 Rtr 6811 1 1 OSPF(0.0.0.0) To: 102.2.0.102-1, Local: 102.2.0.102, Remote: 0.0.0.0 Local interface index: 0, Remote interface index: 0"]



NstLstTEDDB = []
verifyRtrNode = []
verifyRtrDict = {}
for Node in TED_DB:
	nodeTmpLst = Node.split("To: ")
	nodeTmpLstLen = len(nodeTmpLst)
	nodeTmpLst[0]=nodeTmpLst[0].split(" ")[0]+" "+nodeTmpLst[0].split(" ")[1]+" "+nodeTmpLst[0].split(" ")[3]+" "+nodeTmpLst[0].split(" ")[4]
	for count in range(1,nodeTmpLstLen):
		nodeTmpLst[count]=nodeTmpLst[count].split(", Local: ")[0]
	NstLstTEDDB.append(nodeTmpLst)
noTEDNode = []
for Node in NstLstTEDDB:
	if "---" in Node[0]:
		noTEDNode.append(Node[0].split(" ")[0])
print("The following nodes have issue with their TED and has been observed with no link connection to Psudonode:")
print(noTEDNode)
print("==============")
for Node in NstLstTEDDB:
	if "Net" in Node[0] and int(Node[0].split(" ")[2]) != int(Node[0].split(" ")[3]):
		tempLst = []
		RtrNodeCheck = True
		for count1 in range(len(Node)-1):
			n = Node[count1+1]
			if n in noTEDNode:
				RtrNodeCheck = False
			else:
				tempLst.append(n)
		if RtrNodeCheck:
			verifyRtrNode.append(tempLst)
			verifyRtrDict[Node[0].split(" ")[0]] = verifyRtrNode[0]

# Gathering those ID from Node alone

RtrNodeLst = []
for nodeEntry in NstLstTEDDB:
	if "Rtr" in nodeEntry[0]:
		addNodeRec = nodeEntry[0].split(" ")[0]
		for count2 in range(len(nodeEntry)-1):
			addNodeRec += " "+nodeEntry[count2+1]
		RtrNodeLst.append(addNodeRec)

'''
(RtrNodeLst)
-------------
 ['1.1.1.1 101.1.0.101-1 1.21.0.1-1 1.22.0.22-1', ---------> RtrIDRec
 '2.2.2.2 102.2.0.102-1 2.51.0.2-1 2.52.0.52-1',
 '21.21.21.21 1.21.0.1-1 21.31.0.21-1',
 '22.22.22.22 1.22.0.22-1',
 '31.31.31.31 21.31.0.21-1 31.41.0.41-1',
 '32.32.32.32 32.42.0.42-1 22.32.0.32-1',
 '42.42.42.42 32.42.0.42-1 52.42.0.42-1',
 '51.51.51.51 51.41.0.41-1 2.51.0.2-1',
 '52.52.52.52 52.42.0.42-1 2.52.0.52-1',
 '101.101.101.101 101.1.0.101-1',
 '102.102.102.102 102.2.0.102-1']

'''

# verifyRtrDict - {'22.32.0.32-1': ['22.22.22.22', '32.32.32.32']} ---------> LinkID: [NodesList]

#Check for Psudonode (NET) if it's link is missing in the Rtr IDs records.

for LinkID,NodesList in verifyRtrDict.items():
	for count3 in range(len(NodesList)):
		for RtrIDRec in  RtrNodeLst:
				if NodesList[count3] in RtrIDRec.split(" ")[0]:
					if LinkID not in RtrIDRec:
						print("The node %s is not having the link %s in its TED" % (NodesList[count3],LinkID))
						break



'''
Task here is to validate if the TED DB is proper.
1. If we have an Node entry where the "Type" is missing, then we have a missing config on that router. 
2. If there is a Psudo node entry (Type = Net) with LinkIn count less than LinkOut, Check out for the Node Type entry (Type = Rtr) to see if any one of them is showing LnkOut less than LnkIn.

Print the Node ID which has an issue.

pprint(NstLstTEDDB)
-------------------
[['1.21.0.1-1 Net 2 2', '1.1.1.1', '21.21.21.21'],
 ['1.1.1.1 Rtr 3 3', '101.1.0.101-1', '1.21.0.1-1', '1.22.0.22-1'],
 ['2.51.0.2-1 Net 2 2', '51.51.51.51', '2.2.2.2'],
 ['2.2.2.2 Rtr 3 3', '102.2.0.102-1', '2.51.0.2-1', '2.52.0.52-1'],
 ['21.31.0.21-1 Net 2 2', '21.21.21.21', '31.31.31.31'],
 ['21.21.21.21 Rtr 2 2', '1.21.0.1-1', '21.31.0.21-1'],
 ['1.22.0.22-1 Net 2 2', '1.1.1.1', '22.22.22.22'],
 ['22.22.22.22 Rtr 2 1', '1.22.0.22-1'],
 ['31.31.31.31 Rtr 2 2', '21.31.0.21-1', '31.41.0.41-1'],
 ['22.32.0.32-1 Net 1 2', '22.22.22.22', '32.32.32.32'],
 ['32.32.32.32 Rtr 2 2', '32.42.0.42-1', '22.32.0.32-1'],
 ['31.41.0.41-1 Net 1 2', '31.31.31.31', '41.41.41.41'],
 ['51.41.0.41-1 Net 1 2', '41.41.41.41', '51.51.51.51'],
 ['41.41.41.41 --- 2 0'],
 ['32.42.0.42-1 Net 2 2', '42.42.42.42', '32.32.32.32'],
 ['52.42.0.42-1 Net 2 2', '42.42.42.42', '52.52.52.52'],
 ['42.42.42.42 Rtr 2 2', '32.42.0.42-1', '52.42.0.42-1'],
 ['51.51.51.51 Rtr 2 2', '51.41.0.41-1', '2.51.0.2-1'],
 ['2.52.0.52-1 Net 2 2', '2.2.2.2', '52.52.52.52'],
 ['52.52.52.52 Rtr 2 2', '52.42.0.42-1', '2.52.0.52-1'],
 ['101.1.0.101-1 Net 2 2', '1.1.1.1', '101.101.101.101'],
 ['101.101.101.101 Rtr 1 1', '101.1.0.101-1'],
 ['102.2.0.102-1 Net 2 2', '102.102.102.102', '2.2.2.2'],
 ['102.102.102.102 Rtr 1 1', '102.2.0.102-1']]



sivaa@sivaa-mbp Module 2 % python3 OSPF_TED_Validation.py
The following nodes have issue with their TED and has been observed with no link connection to Psudonode:
['41.41.41.41']
==============
The node 22.22.22.22 is not having the link 22.32.0.32-1 in its TED




'''