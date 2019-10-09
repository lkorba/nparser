# nparser
Parser for nmap XML report - displays CSV list od host,port

### Requiremetnts:
python-libnmap 

### Sample usage:
```
user@dev:~$ parser.py ./nmapresult.xml 
10.11.12.1,443
10.11.12.1,8443
10.11.12.3,443
10.11.12.3,465
10.11.12.3,993
```
