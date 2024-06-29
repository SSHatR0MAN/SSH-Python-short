import paramiko
import subprocess
import logging
import os
import getpass

# logging
current_dir = os.path.dirname(__file__)
log_file = os.path.join(current_dir, "log.txt")
logging.basicConfig(filename=log_file,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
log = logging.getLogger()

def ssh_connect(hostname, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        log.info(f"Successfully connected to {hostname} as {username}")

        # Start an interactive shell session
        channel = ssh.invoke_shell()
        while True:
            command = input(f"{username}@{hostname}:~$ ")
            if command.lower() in ['exit', 'quit']:
                print("Closing connection.")
                break
            channel.send(command + '\n')
            while not channel.recv_ready():
                pass
            output = channel.recv(1024).decode('utf-8')
            print(output)

        ssh.close()
    except Exception as e:
        log.error(f"Error executing SSH command: {e}")
        print(f"Error executing SSH command: {e}")
        
print("a = roman, b = julius")
choice = input("What device would you like to connect to for SSH file transfer? "
               "\nType a for roman"
               "\nType b for julius"
               "\nType c for custom"
               "\n>")
log.info(f"User Input: {choice}")

if choice == "a":
    print(f"You have selected roman at roman@192.168.0.16")
    password = getpass.getpass(prompt="Enter your SSH password for roman: ")
    ssh_connect('192.168.0.16', 'roman', password)
elif choice == "b":
    print("You have selected julius at julius@192.168.0.17")
    password = getpass.getpass(prompt="Enter your SSH password for julius: ")
    ssh_connect('192.168.0.17', 'julius', password)
elif choice == "c":
    server_ip = input("What is the server IP?\n")
    custom_user = input("What is your user?\n")
    password = getpass.getpass(prompt=f"Enter your SSH password for {custom_user}: ")
    log.info(f"Attempt to SSH to: {custom_user}@{server_ip}")
    ssh_connect(server_ip, custom_user, password)
else:
    print("Incorrect selection. Please select one device from the list.")