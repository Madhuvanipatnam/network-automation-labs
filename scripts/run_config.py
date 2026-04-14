from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.16.131",
    "username": "madhu",
    "password": "madhu",
    "secret": "madhu",   # VERY IMPORTANT
}

print("Connecting to R1...")

net_connect = ConnectHandler(**router)

net_connect.enable()   # VERY IMPORTANT

output = net_connect.send_command("show run")

print("\n=== RUNNING CONFIG ===\n")
print(output)

net_connect.disconnect()