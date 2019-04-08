import urllib.request

wp = urllib.request.urlopen("http://google.com")
pw = wp.read()

# Print confirmation of connection:
print( 'connected' if pw else 'no internet!' )

# Print Webpage Content:
# print(pw)
