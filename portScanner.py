import nmap
import sys

nm=nmap.PortScanner()
nm_scanner=nm.scan(sys.argv[1],'80',args='-A -p -sS ')

for h in nm_scanner.all_hosts():
	print('--------------------------------')
	print('Host: %s (%s)'% (h,nm_scanner[h].hostname()))
	print('State: %s' % nm_scanner[h].state())
	for prot in nm_scanner[h].all_protocols():
		print('---------------')
		print('Protocol: ',prot)

		list_ports=nm_scanner[h][prot].keys()
		for x in list_port:
			print('port: %s \tstate: %s'% x,nm_scanner[h][prot]['state'])



