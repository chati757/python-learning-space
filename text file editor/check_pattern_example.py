

def check_host_and_dns_on_ssh_config(hostname_config:str=None,hostname_dns:str=None):
    if(not(hostname_config or hostname_dns)):
        raise Exception('no argument')
    
    need_hostname_config = bool(hostname_config and hostname_config.strip())
    need_hostname_dns = bool(hostname_dns and hostname_dns.strip())

    with open('./test_read_config',mode='r') as f:
        for line in f:
            buff_line = line.strip()
            if(need_hostname_config and buff_line.startswith('Host') and hostname_config in buff_line):
                return True
            elif(need_hostname_dns and buff_line.startswith('HostName') and hostname_dns in buff_line):
                return True
    
    return False

if __name__=='__main__':
    print(check_host_and_dns_on_ssh_config(hostname_config='',hostname_dns='192.168.1.100'))