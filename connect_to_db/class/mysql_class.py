class Mysql(object):
    __instance = None

    __host = None
    __user = None
    __password = None
    __database = None

    __session = None
    __connection = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Mysql, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, host='localhost', user='root', password='', database=''):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def prin(self):
        print(self.__host, self.__user, self.__password, self.__database)

a = Mysql('192.168.1.12', 'user', 'user1234', 'test')
a.prin()  # output ('192.168.1.12', 'user', 'user1234', 'test')
b = Mysql('192.168.1.132', 'admin', 'admin1234', 'train')
b.prin() # output ('192.168.1.132', 'admin', 'admin1234', 'train')
a.prin() # output ('192.168.1.132', 'admin', 'admin1234', 'train')
