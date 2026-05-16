# d. Create a sample log file access.log containing records of web server access logs 
# (timestamp, IP address, URL). Write a Python program to extract and display all unique IP addresses. 
# Count the number of occurrences of each IP address.


file = open("access.log", "r")

ips = []

for line in file:
    parts = line.split()
    ips.append(parts[1])

file.close()

unique_ips = set(ips)

print("Unique IP Addresses:")
for ip in unique_ips:
    print(ip)

print("\nIP Address Count:")
for ip in unique_ips:
    print(ip, ":", ips.count(ip))