import re

def emailParser(email):
    
    domain = re.findall(r'[\w+\.\w]+',email)[::-1][0]
    username = email[:email.find(domain) - 1]
    return 'Username: {}\nDomain: {}'.format(username,domain)
