from misc import nls, nli, title, cls, bcolors, yes_array
import concurrent.futures
from itertools import zip_longest as zip
from scapy.layers.inet import IP, TCP, RandShort
from scapy.sendrecv import sr1

# Common ports to scan
PORTS = {
    20: {"port": "FTP 1", "status": "UNSET"},
    21: {"port": "FTP 2", "status": "UNSET"},
    22: {"port": "SSH", "status": "UNSET"},
    23: {"port": "Telnet", "status": "UNSET"},
    25: {"port": "SMTP", "status": "UNSET"},
    53: {"port": "DNS", "status": "UNSET"},
    80: {"port": "HTTP", "status": "UNSET"},
    110: {"port": "POP3", "status": "UNSET"},
    135: {"port": "Windows RPC", "status": "UNSET"},
    137: {"port": "Windows NetBIOS over TCP #1", "status": "UNSET"},
    138: {"port": "Windows NetBIOS over TCP #2", "status": "UNSET"},
    139: {"port": "Windows NetBIOS over TCP #3", "status": "UNSET"},
    143: {"port": "IMAP", "status": "UNSET"},
    161: {"port": "SNMP 1", "status": "UNSET"},
    162: {"port": "SNMP 2", "status": "UNSET"},
    443: {"port": "HTTPS", "status": "UNSET"},
    587: {"port": "SMTP OVER SSL/TLS", "status": "UNSET"},
    989: {"port": "FTPS 1", "status": "UNSET"},
    990: {"port": "FTPS 2", "status": "UNSET"},
    995: {"port": "POP3 OVER SSL/TLS", "status": "UNSET"},
    1433: {"port": "Microsoft SQL Server #1", "status": "UNSET"},
    1434: {"port": "Microsoft SQL Server #2", "status": "UNSET"},
    1720: {"port": "H.323", "status": "UNSET"},
    3389: {"port": "Remote Desktop Protocol", "status": "UNSET"},
    5060: {"port": "SIP 1", "status": "UNSET"},
    5061: {"port": "SIP 2", "status": "UNSET"},
    8080: {"port": "HTTP Alternative", "status": "UNSET"},
}
