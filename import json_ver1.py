import json
import telnetlib

# read the JSON configuration file
with open('config.json', 'r') as f:
    config = json.load(f)

# extract the configuration parameters
host = config['router']['host']
username = config['router']['username']
password = config['router']['password']
enable_password = config['router']['enable_password']
interface = config['router']['interface']
ip_address = config['router']['ip_address']
subnet_mask = config['router']['subnet_mask']

# connect to the router using telnetlib
tn = telnetlib.Telnet(host)
tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"enable\n")
tn.read_until(b"Password: ")
tn.write(enable_password.encode('ascii') + b"\n")

# enter configuration mode and configure the interface
tn.write(b"conf t\n")
tn.write(("interface " + interface + "\n").encode('ascii'))
tn.write(("ip address " + ip_address + " " + subnet_mask + "\n").encode('ascii'))
tn.write(b"no shutdown\n")
tn.write(b"exit\n")

# exit configuration mode and exit telnet session
tn.write(b"exit\n")
tn.read_all().decode('ascii')
tn.close()
