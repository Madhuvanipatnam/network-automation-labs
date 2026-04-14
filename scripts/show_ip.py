from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.16.131",
    "username": "madhu",
    "password": "madhu",
}

print("Connecting to R1...")

net_connect = ConnectHandler(**router)

output = net_connect.send_command("show ip interface brief")

print("\n=== R1 OUTPUT ===\n")
print(output)

net_connect.disconnect()
