# 
# template script
# 

from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.inet6 import *
from GetConfig import *

setting = getconfig()
IFACE = setting.iface

packet = Ether(dst="ff:ff:ff:ff:ff:ff")/Dot1Q(vlan=int(setting.vlan_id))/IP(src=setting.ip_source, dst=setting.ip_destination)/TCP(sport=13400,dport=13400,flags='A' + 'S' + 'U')/"payload_default"

def print_infor(pk):
    try:
        print("\n----------Packet-information-------------")
        pk.show()
    except Exception as ex:
        print("Error:"+ex)

def print_menu():
    cloop=True
    while cloop:
        print (22 * "-" , "MENU" , 22 * "-")
        print ("\t1. [Infor]     {:<24} ".format("Packet information"))
        print ("\t2. [Send]      {:<24} ".format("Packet Send"))
        print ("\t0. [Exit]      {:<24} ".format("Exit"))
        
        print (50 * "-")
        try:
            choice =input("Enter your choice [0-2]: ")
            if (int(choice) >=0 and int(choice) <=2):
                cloop = False
        except ValueError:
            print('')
    return choice

def send_packet(pk):
    try:
        # invalid source MAC
        pk.show()
        sendp(pk, iface=IFACE)
    except Exception as ex:
        print("Error:"+ str(ex))


def main():    
	try:
		choice = 2
		if int(choice)      ==1:                
			print_infor(packet)
		elif int(choice)    ==2:
			send_packet(packet)
		elif int(choice)    ==0:
			cloop=False
	except KeyboardInterrupt:
		print ('\nThanks! See you later!\n\n')

if __name__ == '__main__':
    main()
