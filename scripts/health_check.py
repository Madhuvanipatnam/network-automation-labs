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

print("\n🔌 Connecting to R1...")

try:
    connection = ConnectHandler(**router)
    connection.enable()
    print("✅ Connected successfully!\n")

    # Run command
    output = connection.send_command("show ip interface brief")

    print("📊 Interface Status:\n")
    print(output)

    print("\n🔍 Health Check Results:\n")

    lines = output.splitlines()

    issues_found = False

    for line in lines[1:]:  # skip header
        if "down" in line.lower():
            print(f"⚠️ Issue detected: {line}")
            issues_found = True

    if not issues_found:
        print("✅ All interfaces are UP")

    # Save report
    with open("health_report.txt", "w") as file:
        file.write(output)

    connection.disconnect()

except Exception as e:
    print(f"❌ Connection failed: {e}")

print("\n🏁 Health check completed")