'''Two tasks here.
1. Convert those string to hex with arthematic operators. Represent the entries in the list in hex strings - like: ['0xc0a80101','0x80000001',...]
2. Convert the above string list to an integer list (Performing IP to Int conversion - known method of using multiplication with 256 factor at respective octets)  
	and then perform bit wise operation on that integer to identify the class of IP address involved and rewrite it in a dictionary'''


IP_Hex_Dict = {}
ClassNm = "NA"
IP_Address_List=["192.168.100.1",
"233.10.0.1",
"10.100.100.100",
"155.100.100.100",
"239.132.108.165",
"172.108.10.10",
"128.0.0.1",
"87.60.50.50",
"125.10.77.77",
"223.76.65.32",
"12.68.10.43",
"126.12.12.1",
"60.10.10.10",
"125.120.100.197",
"235.100.100.101",
"192.168.100.1",
"228.108.97.100",
"109.120.210.112",
"55.70.99.88",
"235.23.86.92",
"95.148.153.142",
"239.245.245.1",
"34.43.23.22",
"75.40.19.10",
"223.0.0.1"]

for eachIP in IP_Address_List:
	IPInt = (int(eachIP.split(".")[3]))+(int(eachIP.split(".")[2])*256)+(int(eachIP.split(".")[1])*(256**2))+(int(eachIP.split(".")[0])*(256**3))
	IPHex = hex(IPInt)
	IPbin = '{:04b}'.format(IPInt >> 28)
	if IPbin[0] == '0':
		ClassNm = "A"
	elif IPbin[1] == '0':
		ClassNm = "B"
	elif IPbin[2] == '0':
		ClassNm = "C"
	elif IPbin[3] == '0':
		ClassNm = "D"
	IP_Hex_Dict[eachIP]="     Class Name: "+ClassNm
print(IP_Hex_Dict)

'''sivaa@sivaa-mbp Module 2 % python3 IPAddClass.py
{'192.168.100.1': '     Class Name: C', '233.10.0.1': '     Class Name: D', '10.100.100.100': '     Class Name: A', '155.100.100.100': '     Class Name: B', '239.132.108.165': '     Class Name: D', '172.108.10.10': '     Class Name: B', '128.0.0.1': '     Class Name: B', '87.60.50.50': '     Class Name: A', '125.10.77.77': '     Class Name: A', '223.76.65.32': '     Class Name: C', '12.68.10.43': '     Class Name: A', '126.12.12.1': '     Class Name: A', '60.10.10.10': '     Class Name: A', '125.120.100.197': '     Class Name: A', '235.100.100.101': '     Class Name: D', '228.108.97.100': '     Class Name: D', '109.120.210.112': '     Class Name: A', '55.70.99.88': '     Class Name: A', '235.23.86.92': '     Class Name: D', '95.148.153.142': '     Class Name: A', '239.245.245.1': '     Class Name: D', '34.43.23.22': '     Class Name: A', '75.40.19.10': '     Class Name: A', '223.0.0.1': '     Class Name: C'}'''
