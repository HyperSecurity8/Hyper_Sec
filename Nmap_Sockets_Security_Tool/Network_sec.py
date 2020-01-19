import os
import subprocess
import socket


def mainMenu():
	print("_" * 80)
	print("\t\t\t HYPER SECURITY")
	print("_" * 80)
	print()
	print("\t\t\t0---> My Ip ?")
	print("\t\t\t1---> Host Scan")
	print("\t\t\t2---> OS Scan")
	print("\t\t\t3---> Port Scan")
	print("\t\t\t4---> Port Mode Scan")
	print("\t\t\t5---> Os Bet")
	print("\t\t\t6---> Clear The Screen")
	print("\t\t\t7---> Quit")
	print()
	choice = int(input("Select Your Option : "))
	if choice == 0:
		IP_Scan()
		mainMenu()
	elif choice == 1:
		Host_Scan()
		mainMenu()
	elif choice == 2:
		OS_Scan()
		mainMenu()
	elif choice == 3:
		Port_Scan()
		mainMenu()
	elif choice == 4:
		Port_Mod()
		mainMenu()
	elif choice == 5:
		OS_Bet()
		mainMenu()
	elif choice == 6:
		clear()
		mainMenu()
	elif choice == 7:
		clear()
		quit_Program()
	else:
		print("What ? :(")
		mainMenu()


def IP_Scan():
	scan = subprocess.run(['ipconfig'], capture_output=True)
	scan = scan.stdout.decode()
	scan = scan.split('\n')
	scan = scan[-2]
	Host = open('MyHost.txt', 'w')
	Host.write(scan)
	print(scan)
	Host.close()


def Host_Scan():
	host = input("[*]Please Enter The Host Address To Scan : ")
	print('_' * 80)
	subprocess.check_call(['nmap', '-sn', host + '/24', '-oN', 'Hosts.txt'])
	print("_" * 80)


def OS_Scan():
	OS_in = input("[*]Please Enter The Host Address To Scan : ")
	print('_' * 80)
	subprocess.check_call(['nmap', '-n', '-F', '-A', '-v', '-Pn', '-sS', '-O', '-oN', 'OS_discovery.txt', OS_in])
	print('_' * 80)


def Port_Scan():
	port = input("[*]Please Enter Host Address To Scan : ")
	print('_' * 80)
	subprocess.check_call(['nmap', '-n', '-v', '-Pn', '-sV', '-oN', 'Scanned_Ports.txt', port])
	print('_' * 80)


def Port_Mod():
	host = input("[*]Please Enter The Host Address To Scan : ")
	port = int(input("[*]Please Enter The Port To Scan : "))
	print('_' * 80)
	print('starting ... ')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5)

	if s.connect_ex((host, port)):
		mod1 = "the port is closed"
	else:
		mod1 = "the port is open"

	s.close()

	s = socket.socket()
	try:
		s.connect((host, int(port)))
		s.settimeout(5)
		mod = s.recv(1024)
		s.close()


	except socket.error as err:
		mod = 'cannot connect to ' + str(host) + ' by port ' + str(port) + '\n' + 'error = ' + str(err)
	s.close()

	scan = open('port_mode.txt', 'w')
	scan.write('port mod : \n ' + str(mod1 + '\n') + 'banner results : \n' + str(mod))
	scan.close()
	print('port mod : \n ' + str(mod1) + '\n' + 'banner results : \n' + str(mod))
	print('_' * 80)


def OS_Bet():
	OS_in = input("[*]Please Enter The Host Address To Scan : ")
	print('_' * 80)
	subprocess.check_call(['nmap', '-O', '--osscan-guess', OS_in, '-oN', 'OS_Bet.txt'])
	print('_' * 80)


def clear():
	os.system('cls||clear')


def quit_Program():
	quit()


if __name__ == '__main__':
	mainMenu()
