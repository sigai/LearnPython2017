#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "sigai"
import sys
import getopt
import socket

#TODO: finish server_loop

def usage():
	print("BHP Net Toll\n")
	print("Usage: bhpnet.py -t target_host -p port")
	print("-l --listen                 - listen on [host]:[port] for incoming conections")
	print("-e --execute=file_to_run    - execute the given file upon receiving a connection")
	print("-c --command                - initialize a command shell")
	print("-u --upload=destination     - upon receiving connection upload a file and write to [destination]\n\n")
	print("Examples: ")
	print("bhhpnet.py -t 192.168.0.1 -p 5555 -l -c")
	print("bhhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
	print("bhhpnet.py -t 192.168.0.1 -p 5555 -l -e='cat /etc/passwd'")
	print("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.0.1 -p 135")
	sys.exit()

def client_sender(target, port, buffer):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client.connect((target, port))
		if len(buffer):
			client.send(buffer)
		
		while True:
			recv_len = 1
			response = ""
			
			while recv_len:
				data = client.recv(4096)
				recv_len = len(data)
				response += data
				if recv_len < 4096:
					break
			print(response)
			buffer = input("")
			buffer += "\n"
			client.send(buffer)
	except:
		print("[*] Exception!, Exiting.")
		client.close()

def server_loop():
	pass

def main():
	listen = False
	command = False
	upload = False
	execute = ""
	target = ""
	upload_destination = ""
	port = 0
	
	if not len(sys.argv[1:]):
		usage()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",
		["help", "listen", "execute", "target", "port", "command", "upload"])
	except getopt.GetoptError as err:
		print(err)
		usage()
	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
		elif: o in ("-l", "--listen"):
			listen = True
		elif: o in ("-e", "--execute"):
			execute = a
		elif: o in ("-c", "--commandshell"):
			command = True
		elif: o in ("-u", "--upload"):
			upload_destination = a
		elif: o in ("-t", "--target"):
			target = a
		elif: o in ("-p", "--port"):
			port = int(a)
		else:
			assert False, "Unhandled Option"
	if not listen and len(target) and port > 0:
		buffer = sys.stdin.read()
		client_sender(target, port, buffer)
	if listen:
		server_loop()

if __name__ == "__main__":
	main()