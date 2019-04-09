import urllib.request

def connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

# test
check_connection = connected()
print( 'connected' if check_connection else 'no internet!' )
