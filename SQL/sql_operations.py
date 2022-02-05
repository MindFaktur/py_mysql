import logging

import pymysql


class SQLOperations:
    logging.basicConfig(filename='log.log', filemode='a', format=f'%(asctime)s - %(message)s \n ', level=logging.DEBUG)

    def __init__(self):
        """
        Initializes connection and cursor object.
        """
        self.con = pymysql.connect(host='localhost', user='root', password='root', db='schooldb')
        self.cursor_obj = self.con.cursor()

    def insert_query_operation(self, query, data):
        """
        Perform the insert operation using the query and data received.
        :param query: Insert query with placeholders
        :param data: placeholder value
        :return: boolean
        """
        try:
            if self.cursor_obj.execute(query, data):
                self.con.commit()
                return True
            else:
                return False
        except (pymysql.InternalError, pymysql.ProgrammingError, pymysql.OperationalError, Exception) as IR:
            logging.exception(IR)
            self.con.rollback()
            self.con.commit()
            return False

    def delete_query_operation(self, query, data):
        """
        Perform the delete operation using the query and data received.
        :param query: Delete query with placeholders
        :param data: placeholder value
        :return: boolean
        """
        try:
            if self.cursor_obj.execute(query, data):
                self.con.commit()
                return True
            else:
                return False
        except (pymysql.InternalError, pymysql.ProgrammingError, pymysql.OperationalError, Exception) as IR:
            logging.exception(IR)
            self.con.rollback()
            self.con.commit()
            return False

    def update_query_operation(self, query, data):
        """
        Perform the update operation using the query and data received.
        :param query: update query with placeholders
        :param data: placeholder value
        :return: boolean
        """
        try:
            if self.cursor_obj.execute(query, data):
                self.con.commit()
                return True
            else:
                return False
        except (pymysql.InternalError, pymysql.ProgrammingError, pymysql.OperationalError, Exception) as IR:
            logging.exception(IR)
            self.con.rollback()
            self.con.commit()
            return False

    def select_query_operation(self, query):
        """
        Perform the select operation using the query received.
        :param query: Insert query without placeholders
        :return: cursor object or boolean
        """
        try:
            self.cursor_obj.execute(query)
            return self.cursor_obj
        except (pymysql.InternalError, pymysql.ProgrammingError, pymysql.OperationalError, Exception) as IR:
            logging.exception(IR)
            self.con.rollback()
            return False

    def get_value_query_operation(self, query, data):
        """
        Fetch the id from the table based on given name.
        :param query: Select query with placeholders.
        :param data: placeholder value
        :return: cursor object or boolean
        """
        try:
            self.cursor_obj.execute(query, data)
            value = self.cursor_obj.fetchone()
            return value[0]
        except (pymysql.InternalError, pymysql.ProgrammingError, pymysql.OperationalError, Exception) as IR:
            logging.exception(IR)
            self.con.rollback()
            return False

    def close_sql(self):
        """
        Closes the con and cursor object.
        :return:nothing
        """
        self.cursor_obj.close()
        self.con.close()
