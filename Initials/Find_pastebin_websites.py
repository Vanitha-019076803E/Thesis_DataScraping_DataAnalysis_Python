import whois
import sys
import csv

domain_extensions = []
websites = []
domain_names = []
domains_taken = []
domains_doesnot_exist = []

with open('tld.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        domain_extensions.append(line[0])

with open('Pastebin_like_websites.csv', 'r') as csv_file2:
    csv_reader2 = csv.reader(csv_file2)

    for line in csv_reader2:
        websites.append(line[0])

print(len(websites))

for extension in domain_extensions:
    for website in websites:
        domain_names.append(website+"."+extension)

def domains_avail():
    print("Loading.....")
    for domains in domain_names:
        try:
            domain = whois.query(domains) 
            if domain.name == None:
                sys.exit(1)
        except:
            domains_doesnot_exist.append(domains)  
        else:
            domains_taken.append(domains)

domains_avail()
print("\nDomains available\n")
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

