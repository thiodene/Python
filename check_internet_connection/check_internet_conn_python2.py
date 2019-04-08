import urllib2
from urllib2 import urlopen

wp = urlopen("http://google.com")
pw = wp.read()

# Print confirmation of connection:
print( 'connected' if pw else 'no internet!' )

# Print Webpage Content:
# print(pw)
