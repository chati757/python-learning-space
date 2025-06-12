import psutil

# ดึงรายละเอียดของ network interfaces
interfaces = psutil.net_if_addrs()

# แสดง IP address ของแต่ละ interface
print([addrs[1].address for interface, addrs in interfaces.items() if(interface=='Ethernet')][0])
    