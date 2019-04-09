import urllib2

def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

check_internet = internet_on()
print( 'connected' if check_internet else 'no internet!' )

