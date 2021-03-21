import psycopg2
from datamanager import DataManager


class DatabaseManager(DataManager):
    __host = ''
    __port = 0
    __user = ''
    __pass = ''
    __base = ''

    _conn = None
    _closeFlag = False

    def __init__(self, conn=None, closeFlag=True):
        super().__init__()
        self._conn = conn
        self._closeFlag = closeFlag

    def __access(self):
        (self.__host, 
            self.__port, 
            self.__base, 
            self.__user, 
            self.__pass) = '192.168.122.164:5432:geo:geo:geo'.split(':')

    def __connect(self):
        try:
            return psycopg2.connect(
                user=self.__user,
		password=self.__pass,
		host=self.__host,
		port=int(self.__port),
		database=self.__base)
        except Exception as ex:
            print(ex)
	
        return None 

    def _open(self):
        if self._conn is None:
            self.__access()
            self._conn = self.__connect()
            if not self._conn:
                return False
        return True

    def close(self):
        if self._conn is not None:
            self._conn.close()

    def commit(self):
        if self._conn is not None:
            self._conn.commit()
