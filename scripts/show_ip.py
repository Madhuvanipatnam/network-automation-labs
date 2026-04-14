from netmiko import ConnectHandler

username = input("Enter username: ")
password = input("Enter password: ")

router = {
    "device_type": "cisco_ios",
    "host": "192.168.16.131",
    "username": username,
    "password": password,

}

print("Connecting to R1...")

net_connect = ConnectHandler(**router)

output = net_connect.send_command("show ip interface brief")

print("\n=== R1 OUTPUT ===\n")
print(output)

net_connect.disconnect()
