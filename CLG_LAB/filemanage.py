file = open("access.log","w")
file.write("2036-04-05 192.168.1.1 /home\n")
file.write("2036-04-05 192.168.1.2 /about\n")
file.write("2036-04-05 192.168.1.1 /contact\n")
from collections import Counter
file = open("access.log","r")
lines = file.readlines()
file.close()
ips = []
for line in lines:
    parts = line.split()
    ips.append(parts[1])
ip_count = Counter(ips)
print("\nIP addresses count:")
for ip,count in ip_count.items():
     print(f"{ip}: {count}")

'''
OUTPUT:-
IP addresses count:
192.168.1.1: 2
192.168.1.2: 1
'''