import  threading
# import library threading to allow various tasks happen at the same time
import socket
# import library socket to allow network connection

host = '192.168.56.115'
# server static IPv4 address
port = 55555
# free, unreserved connection  port

nickname = input("Choose a nickname: ")
# request a nickname from client

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# configure client socket AF_INET to use internet socket and SOCK_STREAM to use TCP protocol
client.connect(('192.168.56.114', 55555))
# connect client to said IP and port

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'NICK':
				client.send(nickname.encode('ascii'))
			else:
				print(message)
		except:
			print("An error occured!")
			client.close()
			break
# receive function to receive messages
# if message asks for nickname, send nickname
# else print messages
# if the is error in receiving message, an error message is sent

def write():
	while True:
		message = f'{nickname}: {input("")}'
		client.send(message.encode('ascii'))
# write function to write message
# while messsage is written, nickname will be included at the output 
# to let other clients see the nickname of the message sender

receive_thread = threading.Thread(target=receive)
receive_thread.start()
# a thread that run receive function start running

write_thread = threading.Thread(target=write)
write_thread.start()
# a thread that run write function start running
