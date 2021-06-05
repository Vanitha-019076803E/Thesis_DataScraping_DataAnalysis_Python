import whois
import sys
import csv

domain_extensions = []
domain_names = []
domains_taken = []
domains_doesnot_exist = []

with open('/Users/Downloads/000Data_collection/tld.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        domain_extensions.append(line[0])

print(len(domain_extensions))

for extension in domain_extensions:
    domain_names.append("pastebin"+"."+extension)

for domains in domain_names:
    try:
        domain = whois.query(domains) 
        print("Loading.........")
        if domain.name == None:
            sys.exit(1)
    except:
        domains_doesnot_exist.append(domains)  
    else:
        domains_taken.append(domains)

print("\n domainsTaken \n")
print(domains_taken)

# https://www.geany.org/p/ 
# https://defuse.ca/pastebin.htm
# http://paste.lisp.org/ - blocked
# http://paste.pound-python.org/ - blocked
# http://everfall.com/paste/
# https://gitlab.com/explore
#
#
#
#
#
#

