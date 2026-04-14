from netmiko import ConnectHandler

username = input("Enter username: ")
password = input("Enter password: ")

router = {
    "device_type": "cisco_ios",
    "host": "192.168.16.131",
    "username": username,
    "password": password,
    "secret": password,
}

net_connect = ConnectHandler(**router)
net_connect.enable()

output = net_connect.send_command("show run")
print(output)

net_connect.disconnect()