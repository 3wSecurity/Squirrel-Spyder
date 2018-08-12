#Hostname Spyder - John Survant

import sqlite3
import ssl
import urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib.parse import urlsplit


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#variables, lists etc
returned_links = list()
unique_hostnames = list()
temp_links = list()
unique_links = list()
new_links = list()
new_hosts = list()
my_company_hosts_list = list()
new_host_list = list()
host = 0

def spider_links(spider_arg):

    print(spider_arg)
    html = urlopen(spider_arg, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags:
        temp_links.append(tag.get('href', None))
    #for x in temp_links:
    #    print(x)

    for site in temp_links:

        if site is None:
            continue
        if 'https://' in site or 'http://' in site:

            #print(site)
            host  = site.split('/')
            #print(host[2])
            host = (host[2])
            #print('host found   ' + host)

            if host not in my_company_hosts_list:

                if host_base_name in host:
                    #print(host_found)
                    my_company_hosts_list.append(host)

            if host not in unique_hostnames:
                unique_hostnames.append(host)
                new_hosts.append(host)
                #print(unique_hostnames)
                print('new host found   ' + host)

    return;


print('#######################################################################')
print('#      Welcome to the Squirrel Spyder module for ReconNG              #')
print('#         Please select one of the following Options                  #')
print('#                                                                     #')
print('#        1) Import Last Scan Data                                     #')
print('#        2) Begin Web Discovery                                       #')
print('#                                                                     #')
print('#                                                                     #')
print('#######################################################################')

value = input('Select Option: ')
if value == '1':
    print('This options is currently not available')
if value == '2':
    print('Lets get this started')

website = input('Enter full url name for your Website: ')
if len(website) < 1:

    website = "https://www.ebay.com/"


base_domain = website.split('.')
base_domain_len = str(len(base_domain))
#print(base_domain_len)


if len(base_domain) > 2:

    '''
    host = website.split('.')
    host = host[:1]
    host = str(host)
    host = host.strip("''")
    base_domain = str(base_domain)
    base_domain = base_domain.strip(host)

    print(base_domain)
    '''
    parsed = urlsplit(website)

    # parsed.scheme is 'http'
    # parsed.netloc is 'www.python.org'
    # parsed.path is None, since (strictly speaking) the path was not defined
    host_base_name = parsed.netloc  # www.python.

    # Removing www.
    # This is a bad idea, because www.python.org could
    # resolve to something different than python.org
    if host_base_name.startswith('www.'):
        host_base_name = host_base_name[4:]
    #print(host_base_name)



html = urlopen(website, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup)


tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    #'TAG:', tag)
    #print('URL:', tag.get('href', None))

    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    returned_links.append(tag.get('href', None))
    unique_links.append(tag)
    #returned_links.append(tag.contents[0])


for site in returned_links:

    if site is None:
        continue
    if 'https://' in site or 'http://' in site:

        #print(site)
        host  = site.split('/')
        #print(host[2])
        host = (host[2])
        if host not in unique_hostnames:
            unique_hostnames.append(host)
            unique_links.append(site)



print('########################################################### ')
print('The following unique_hostnames were referenced in the site: ')
print('########################################################### ')
for host_found in unique_hostnames:
    print(host_found)

print('########################################################### ')
print('These are the hosts fall within your base domain ---  ' + host_base_name)
print('########################################################### ')
for host_found in unique_hostnames:
    if host_base_name in host_found:
        #print(host_found)
        my_company_hosts_list.append(host_found)

for x in my_company_hosts_list:
    print(x)


print('########################################################### ')
print('lets see what other domains that might be yours, we will go through one at a time')
print('########################################################### ')
for host_found in unique_hostnames:
    if host_base_name not in host_found:
        #print(host_found)
        new_host_list.append(host_found)

for x in new_host_list:
    print(x)






for x in new_host_list:
    u_hosts = (str(len(unique_hostnames)))
    c_hosts = (str(len(my_company_hosts_list)))
    print('##############################################################################################')
    print('#      Welcome to the Squirrel Spyder module for ReconNG                                     #')
    print('#        ' +   u_hosts + ' Hosts were discovered                                                            #')
    print('#        ' +   c_hosts + ' Hosts have been identified as belonging to your organization                     #')
    print('#                                                                                            #')
    print('#        1) Print toltal list of unique hosts                                                #')
    print('#        2) Print total list of hosts beloning to my company                                 #')
    print('#        3) Continue my next scan                                                            #')
    print('#        4) Skip this host                                                                   #')
    print('#        5) Scan for email addresses                                                         #')
    print('#        6) Search for file extentions                                                       #')
    print('#        7) Perform Google Hacking                                                           #')
    print('#        8) Save current data to ReconNG                                                     #')
    print('#                                                                                            #')
    print('##############################################################################################')
    print('Next host to scan: ' + x)
    print('usrls that will be tested are listed below:')
    print('')
    for y in unique_links:
        if y is  None: continue
        if x in y:
            print(y)
            new_links.append(y)
            #for r in new_links:
            #    print(r)
            value = input('')
            if value == '1':
                for item in unique_hostnames:
                    print(item)
                continue

            if value == '2':
                for item in my_company_hosts_list:
                    print(item)
                continue

            if value == '3':
                print("Scanning....")
                spider_links(y)
                new_links = list()
                print(str(len(unique_hostnames)) + '  Hosts have been identified so far')
                print(str(len(my_company_hosts_list)) + '  Hosts have been identified as belonging to your organization')
                print(str(len(new_hosts)) + ' New hosts were found')
                new_hosts = list()
                continue

            if value == '4': continue
            if value == '5':
                print('This feature is currently not available')
                break
            if value == '6':
                    print('This feature is currently not available')
                    break
            if value == '7':
                    print('This feature is currently not available')
                    break
            if value == '8':
                print('Import Successful, not really :)')
                break


'''
new_website = input('y/n:   ')
if len(new_website) < 1:
    new_website = ""
'''



'''
for x in unique_hostnames:
    base_domain = x.split('.')
    base_domain = base_domain[1:]
    #base_domain = base_domain[:1]
    my_company_hosts_list.append(base_domain)


for x in my_company_hosts_list:
    print(x)
'''
'''
for my_company_host in unique_hostnames:


    if base_domain in my_company_hosts_list:
         base_domain.append(host)
         company_hosts.append()


    for x in unique_hostnames:
        print(x)


'''


















#end
