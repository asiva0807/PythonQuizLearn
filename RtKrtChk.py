from pprint import pprint

RtTbl = [["1.1.1.1/32         *[Direct/0] 00:59:16","> via lo0.0"],
["1.21.0.0/24        *[Direct/0] 01:53:29","> via ge-0/0/3.0"],
["1.21.0.1/32        *[Local/0] 01:53:29","Local via ge-0/0/3.0"],
["1.22.0.0/24        *[Direct/0] 00:53:44","> via ge-0/0/4.0"],
["1.22.0.1/32        *[Local/0] 00:53:44","Local via ge-0/0/4.0"],
["2.2.2.2/32         *[OSPF/10] 00:16:36, metric 5",["> to 1.21.0.21 via ge-0/0/3.0","to 1.22.0.22 via ge-0/0/4.0"]],
["2.51.0.0/24        *[OSPF/10] 00:57:08, metric 5","> to 1.21.0.21 via ge-0/0/3.0"],
["2.52.0.0/24        *[OSPF/10] 00:51:22, metric 5","> to 1.22.0.22 via ge-0/0/4.0"],
["10.102.163.13/32   *[Local/0] 04:43:49","Local via fxp0.0"],
["21.21.21.21/32     *[OSPF/10] 01:01:48, metric 1","> to 1.21.0.21 via ge-0/0/3.0"],
["21.31.0.0/24       *[OSPF/10] 01:01:48, metric 2","> to 1.21.0.21 via ge-0/0/3.0"],
["22.22.22.22/32     *[OSPF/10] 00:53:44, metric 1","> to 1.22.0.22 via ge-0/0/4.0"],
["22.32.0.0/24       *[OSPF/10] 00:53:44, metric 2","> to 1.22.0.22 via ge-0/0/4.0"],
["31.31.31.31/32     *[OSPF/10] 00:58:18, metric 2","> to 1.21.0.21 via ge-0/0/3.0"],
["31.41.0.0/24       *[OSPF/10] 00:58:18, metric 3","> to 1.21.0.21 via ge-0/0/3.0"],
["32.32.32.32/32     *[OSPF/10] 00:51:22, metric 2","> to 1.22.0.22 via ge-0/0/4.0"],
["32.42.0.0/24       *[OSPF/10] 00:51:22, metric 3","> to 1.22.0.22 via ge-0/0/4.0"],
["41.41.41.41/32     *[OSPF/10] 00:58:07, metric 3","> to 1.21.0.21 via ge-0/0/3.0"],
["42.42.42.42/32     *[OSPF/10] 00:51:22, metric 3","> to 1.22.0.22 via ge-0/0/4.0"],
["51.41.0.0/24       *[OSPF/10] 00:58:07, metric 4","> to 1.21.0.21 via ge-0/0/3.0"],
["51.51.51.51/32     *[OSPF/10] 00:57:08, metric 4","> to 1.21.0.21 via ge-0/0/3.0"],
["52.42.0.0/24       *[OSPF/10] 00:51:22, metric 4","> to 1.22.0.22 via ge-0/0/4.0"],
["52.52.52.52/32     *[OSPF/10] 00:51:22, metric 4","> to 1.22.0.22 via ge-0/0/4.0"],
["66.129.255.62/32   *[Static/5] 04:43:49","> to 10.102.175.254 via fxp0.0"],
["101.1.0.0/24       *[Direct/0] 01:53:29","> via ge-0/0/2.0"],
["101.1.0.1/32       *[Local/0] 01:53:29","Local via ge-0/0/2.0"],
["101.101.101.101/32 *[OSPF/10] 01:53:19, metric 1","> to 101.1.0.101 via ge-0/0/2.0"],
["102.2.0.0/24       *[OSPF/10] 00:16:36, metric 6",["> to 1.21.0.21 via ge-0/0/3.0","to 1.22.0.22 via ge-0/0/4.0"]],
["102.102.102.102/32 *[OSPF/10] 00:16:36, metric 6",["to 1.21.0.21 via ge-0/0/3.0","> to 1.22.0.22 via ge-0/0/4.0"]]]

inc = 0
FwTbl = ["Destination        Type RtRef Next hop           Type Index    NhRef Netif",
"default            perm     0                    rjct       36     1",
"0.0.0.0/32         perm     0                    dscd       34     1",
"1.1.1.1/32         intf     0 1.1.1.1            locl      591     1",
"1.21.0.0/24        intf     0                    rslv      580     1 ge-0/0/3.0",
"1.21.0.0/32        dest     0 1.21.0.0           recv      578     1 ge-0/0/3.0",
"1.21.0.1/32        intf     0 1.21.0.1           locl      579     2",
"1.21.0.1/32        dest     0 1.21.0.1           locl      579     2",
"1.21.0.21/32       dest     0 0:5:86:1b:4b:3     ucst      590    18 ge-0/0/3.0",
"1.21.0.255/32      dest     0 1.21.0.255         bcst      577     1 ge-0/0/3.0",
"1.22.0.0/24        intf     0                    rslv      593     1 ge-0/0/4.0",
"1.22.0.0/32        dest     0 1.22.0.0           recv      586     1 ge-0/0/4.0",
"1.22.0.1/32        intf     0 1.22.0.1           locl      592     2",
"1.22.0.1/32        dest     0 1.22.0.1           locl      592     2",
"1.22.0.22/32       dest     0 0:5:86:2b:28:4     ucst      594    15 ge-0/0/4.0",
"1.22.0.255/32      dest     0 1.22.0.255         bcst      585     1 ge-0/0/4.0",
#"2.2.2.2/32         user     0 1.21.0.21          ucst      590    18 ge-0/0/4.0",
"2.51.0.0/24        user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"2.52.0.0/24        user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"10.0.0.0/8         user     2 0:0:5e:0:1:c9      ucst      341     8 fxp0.0",
"10.102.160.0/20    intf     0                    rslv      340     1 fxp0.0",
"10.102.160.0/32    dest     0 10.102.160.0       recv      338     1 fxp0.0",
"10.102.160.37/32   dest     0 0:50:56:b2:5c:46   ucst      346     1 fxp0.0",
"10.102.163.13/32   intf     0 10.102.163.13      locl      339     2",
"10.102.163.13/32   dest     0 10.102.163.13      locl      339     2",
"10.102.175.252/32  dest     0 10:e:7e:b1:f4:0    ucst      351     1 fxp0.0",
"10.102.175.253/32  dest     0 10:e:7e:b1:b0:80   ucst      350     1 fxp0.0",
"10.102.175.254/32  dest     0 0:0:5e:0:1:c9      ucst      341     8 fxp0.0",
"10.102.175.255/32  dest     0 10.102.175.255     bcst      337     1 fxp0.0",
"21.21.21.21/32     user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"22.22.22.22/32     user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"22.32.0.0/24       user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"31.31.31.31/32     user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"31.41.0.0/24       user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"32.32.32.32/32     user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"41.41.41.41/32     user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"42.42.42.42/32     user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"51.41.0.0/24       user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"51.51.51.51/32     user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"52.42.0.0/24       user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"52.52.52.52/32     user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"66.129.255.62/32   user     0 10.102.175.254     ucst      341     8 fxp0.0",
"101.1.0.0/24       intf     0                    rslv      576     1 ge-0/0/2.0",
"101.1.0.0/32       dest     0 101.1.0.0          recv      574     1 ge-0/0/2.0",
"101.1.0.1/32       intf     0 101.1.0.1          locl      575     2",
"101.1.0.1/32       dest     0 101.1.0.1          locl      575     2",
"101.1.0.101/32     dest     0 0:5:86:8a:85:2     ucst      589     4 ge-0/0/2.0",
"101.1.0.255/32     dest     0 101.1.0.255        bcst      573     1 ge-0/0/2.0",
"101.101.101.101/32 user     0 101.1.0.101        ucst      589     4 ge-0/0/2.0",
"102.2.0.0/24       user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"102.102.102.102/32 user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"128.102.161.75/32  user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"128.102.161.80/32  user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"128.102.161.87/32  user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"128.102.161.99/32  user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"128.102.162.66/32  user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"128.102.162.81/32  user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"128.102.162.93/32  user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"128.102.162.112/32 user     0 1.22.0.22          ucst      594    15 ge-0/0/4.0",
"128.102.163.1/32   user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"128.102.163.13/32  intf     0 128.102.163.13     locl      513     1",
"128.102.163.102/32 user     0 1.21.0.21          ucst      590    18 ge-0/0/3.0",
"128.102.163.138/32 user     0 101.1.0.101        ucst      589     4 ge-0/0/2.0",
"172.16.0.0/12      user     0 10.102.175.254     ucst      341     8 fxp0.0",
"192.168.0.0/16     user     0 10.102.175.254     ucst      341     8 fxp0.0",
"224.0.0.0/4        perm     1                    mdsc       35     1",
"224.0.0.1/32       perm     0 224.0.0.1          mcst       31     3",
"224.0.0.5/32       user     1 224.0.0.5          mcst       31     3",
"255.255.255.255/32 perm     0                    bcst       32     1"]


RtDerDict = {}
for rt in RtTbl:
	RtEntry = (" ".join(rt[0].split())).split(" *")[0]
	if type(rt[1]) is not list:
		if "lo0" not in rt[1]:
			if "Local" not in rt[1]:
				RtNH = rt[1].split("via")[1]
				RtDerDict[RtEntry]=RtNH
	else:
		if any(">" in string for string in rt[1]):
			for countA in range(len(rt[1])):
				if ">" in rt[1][countA]:
					RtNHPos = countA
					break
			RtNH = rt[1][RtNHPos].split("via")[1]
			RtDerDict[RtEntry]=RtNH

'''
pprint(RtDerDict)
{'1.21.0.0/24': ' ge-0/0/3.0',
 '1.22.0.0/24': ' ge-0/0/4.0',
 '101.1.0.0/24': ' ge-0/0/2.0',
 '101.101.101.101/32': ' ge-0/0/2.0',
 '102.102.102.102/32': ' ge-0/0/4.0',
 '102.2.0.0/24': ' ge-0/0/3.0',
 '2.2.2.2/32': ' ge-0/0/3.0',
 '2.51.0.0/24': ' ge-0/0/3.0',
 '2.52.0.0/24': ' ge-0/0/4.0',
 '21.21.21.21/32': ' ge-0/0/3.0',
 '21.31.0.0/24': ' ge-0/0/3.0',
 '22.22.22.22/32': ' ge-0/0/4.0',
 '22.32.0.0/24': ' ge-0/0/4.0',
 '31.31.31.31/32': ' ge-0/0/3.0',
 '31.41.0.0/24': ' ge-0/0/3.0',
 '32.32.32.32/32': ' ge-0/0/4.0',
 '32.42.0.0/24': ' ge-0/0/4.0',
 '41.41.41.41/32': ' ge-0/0/3.0',
 '42.42.42.42/32': ' ge-0/0/4.0',
 '51.41.0.0/24': ' ge-0/0/3.0',
 '51.51.51.51/32': ' ge-0/0/3.0',
 '52.42.0.0/24': ' ge-0/0/4.0',
 '52.52.52.52/32': ' ge-0/0/4.0',
 '66.129.255.62/32': ' fxp0.0'}
'''

FwTbl.pop(0)
for rtE,nhE in RtDerDict.items():
	RtFibPresent = False
	for fibE in FwTbl:
		if rtE in fibE:
			RtFibPresent = True
			break
	if not RtFibPresent:
		print(rtE," is not present in Fib Table")



'''
2.2.2.2/32  is not present in Fib Table
21.31.0.0/24  is not present in Fib Table
32.42.0.0/24  is not present in Fib Table
'''

'''
TO CHECK IF A LIST CONTAIN CHARACHTER
-------------------------------------
>>> a
['1', 'a', 'b', 'c d', 'n:s']
>>> any(":" in string for string in a)
True
>>> any("@" in string for string in a)
False
>>> '''


'''
Look out for each entry of RPD i.e. the RtTbl in the Kernel FIB Table i.e. the FwTbl list.
Look out for mismatch between the 2 tables.
	If the entry is present in RPD but not in KRT 
	If the NH info / outgoing info of these tables are not the same 
Then we have a situation of RPD out of sync with KRT.
Create a dict with structure as {Rt:Mismatch_Reason}
Mismatch_Reason like "Missing Kernel entry" or "NH info mismatch".

KEY1: Some routes are learnt over 2 path and only 1 path is active (Represented by ">" symbol) That next hop interface needs to be in the FW.
E.g:
["102.2.0.0/24       *[OSPF/10] 00:16:36, metric 6",["> to 1.21.0.21 via ge-0/0/3.0","to 1.22.0.22 via ge-0/0/4.0"]]

'''
