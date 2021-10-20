import os  
import psutil
import shutil
import netifaces
import pprint
import platform
print('')
print("="*40, "Ip Addresses", "="*40)
print('')
ip_ = os.popen("ip a").readlines()      
from pprint import pprint
pprint(ip_)
print('')
print("="*40, "Network Interfaces Names", "="*40)
print('')
addrs = psutil.net_if_addrs()
eth = list(addrs.keys())
print(str(eth))
print('')
print("="*40, "Network Interfaces Ip & Names", "="*40)
print('')

netifaces.interfaces()

for i in range(len(eth)):
    eth_ = str(eth[i])
    print(eth_)
    print(netifaces.ifaddresses(eth_))
print('')
print('')
print(eth[0] + ' ' + netifaces.ifaddresses(eth[0])[netifaces.AF_INET][0]['addr'])

print(eth[1] + ' ' + netifaces.ifaddresses(eth[1])[netifaces.AF_INET][0]['addr'])

print('')
print("="*40, "Disk Usage", "="*40)
print('')

total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))

print('')
# let's print CPU information
print("="*40, "CPU Info", "="*40)
print('')

# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")

print('')
print("="*40, "System Information", "="*40)
print('')

uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

#link_show= os.popen("ip -br -c link show").readlines()      
#from pprint import pprint
#pprint(link_show)

