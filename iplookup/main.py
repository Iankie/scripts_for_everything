import argparse
from dns import resolver,reversename
from colorama import init, Fore, Style

# colorama
init()

# argparse
parser = argparse.ArgumentParser(
    prog='DI.LookUp',
    description='DNS and IP look up tool'
)

parser.add_argument('-dL','--domain-list', help='Set a file with domain names')
parser.add_argument('-iL', '--ip-list', help='Setting a file with IP')
parser.add_argument('-o', '--output-file', help='Set a name of output file', required=False)

args = parser.parse_args()

# Main
## DNS LookUp domains list
if args.domain_list:
    with open(f'{args.domain_list}', 'r') as file:
        domain_list = file.readlines()
        
        not_resolved = []
        
        print(Fore.GREEN + "Resolved Domains" + Style.RESET_ALL)
        
        for domain in domain_list:
            domain = domain.strip()
            
            try:
                ips = resolver.resolve(domain)
                print(f'{domain} : ')
                for ip in ips:
                    print(f' - {ip}')
            except:
                not_resolved.append(domain)

        print(Fore.RED + "\nNot resolved domains" + Style.RESET_ALL)
        for domain in not_resolved:
            print(f" - {domain}")

## IP Reverse Look Up
elif args.ip_list:
    with open(f'{args.ip_list}', 'r') as file:
        ips = file.readlines()
        
        not_reversed = []
        
        print(Fore.GREEN + "Reversed Look Up" + Style.RESET_ALL)
        
        for ip in ips:
            ip = ip.strip()
            
            try:
                addr = reversename.from_address(f"{ip}")
                domains = resolver.resolve(addr, "PTR")
                print(f'{ip} : ')
                for domain in domains: 
                    print(f' - {str(domain).strip('.')}')
            except:
                not_reversed.append(ip)
        
        print(Fore.RED + "\nWasn't reverse look up : " + Style.RESET_ALL)
        for ip in not_reversed:
            print(f' - {ip}')