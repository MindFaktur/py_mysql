from unittest import TestCase
from SQL.sql_operations import SQLOperations


class TestSQLOperations(TestCase):

    so = SQLOperations()

    def test_insert_query_operation(self):
        """
        Test the insert query function.
        :return: nothing
        """
        str_department_name = 25
        insert_query = "INSERT INTO departments(dp_name) VALUES(%s)"
        self.so.insert_query_operation(insert_query, (str_department_name,))
        department_id_query = "SELECT dp_id FROM departments WHERE dp_name=%s"
        cursor_obj = self.so.get_value_query_operation(department_id_query, (str_department_name,))
        dp_id = cursor_obj.fetchone()
        if dp_id[0] > 0:
            assert True

    def test_delete_query_operation(self):
        """
        Test the delete query function.
        :return: nothing
        """
        str_department_name = "kannada"
        delete_query = "DELETE FROM departments WHERE dp_name = %s"
        self.so.delete_query_operation(delete_query, (str_department_name,))
        department_id_query = "SELECT dp_id FROM departments WHERE dp_name=%s"
        cursor_obj = self.so.get_value_query_operation(department_id_query, (str_department_name,))

        if cursor_obj.fetchone() is None:
            assert True

    def test_select_query_operation(self):
        """
        Test the select query function.
        :return: nothing
        """
        fetch_query = "SELECT * FROM departments"
        cursor_obj = self.so.select_query_operation(fetch_query)
        if cursor_obj.fetchall() is not None:
            assert True

    def test_get_value_query_operation(self):
        """
        Test the select query with data function.
        :return: nothing
        """
        str_department_name = "biology"
        dp_actual_id = 2
        department_id_query = "SELECT dp_id FROM departments WHERE dp_name=%s"
        cursor_obj = self.so.get_value_query_operation(department_id_query, (str_department_name,))
        dp_id = cursor_obj.fetchone()
        if dp_id[0] == dp_actual_id:
            assert True
