import psycopg2


class Database:
    """
    Class is used to update 
    postgreSQL database in django
    """
    __conn = None
    __cursor = None

    def connection(self, user):
        # connect to the database
        self.__conn = psycopg2.connect(user)
        # cursor = conn.cursor()

    def cursor(self):
        # opens cursor
        self.__cursor = self.__conn.cursor()

    def insert(self, name, des, years, weight, url):
        # add each element to the database and map to correct field
        insertCommand = 'INSERT INTO src_animals("name", "description", "age", "weight", "url" )' + \
                        ' VALUES (%s, %s, %s, %s, %s)'
        data = (name, des, years, weight, url)
        self.__cursor.execute(insertCommand, data)

    def commit(self):
        self.__conn.commit()

    def close(self):
        self.__conn.close()
