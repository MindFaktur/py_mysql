import logging

import psycopg2


class PSQLOperations:

    logging.basicConfig(filename='psqllog.log', filemode='a', format=f'%(asctime)s - %(message)s \n ', level=logging.DEBUG)

    def __init__(self):
        """
        Initializes connection and cursor object.
        """
        self.con = psycopg2.connect(dbname='teacher_student', user='postgres', password='root')
        self.cursor_obj = self.con.cursor()

    def insert_query_operation(self, query, data):
        """
        Perform the insert operation using the query and data received.
        :param query: Insert query with placeholders
        :param data: placeholder value
        :return: boolean
        """
        try:
            self.cursor_obj.execute(query, data)
            self.con.commit()
            return True
        except (psycopg2.InternalError, psycopg2.ProgrammingError, psycopg2.OperationalError, Exception) as IR:
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
            self.cursor_obj.execute(query, data)
            self.con.commit()
            return True

        except (psycopg2.InternalError, psycopg2.ProgrammingError, psycopg2.OperationalError, Exception) as IR:
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
            self.cursor_obj.execute(query, data)
            self.con.commit()
            return True
        except (psycopg2.InternalError, psycopg2.ProgrammingError, psycopg2.OperationalError, Exception) as IR:
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
        except (psycopg2.InternalError, psycopg2.ProgrammingError, psycopg2.OperationalError, Exception) as IR:
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
        except (psycopg2.InternalError, psycopg2.ProgrammingError, psycopg2.OperationalError, Exception) as IR:
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


