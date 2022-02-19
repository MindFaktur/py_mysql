from SQL.sql_object_adapter import SqlObjectAdapter
from utilities.table_utilitis import TableUtilities
import logging


class Departments:
    logging.basicConfig(filename='log.log', filemode='a', format=f'%(asctime)s - %(message)s \n ', level=logging.DEBUG)

    def __init__(self):
        self.utility_object = TableUtilities()
        self.sql_object = SqlObjectAdapter.return_sql()

    def add_department(self):
        """
        Add department to the departments table.
        :return: nothing
        """
        str_department_name = self.utility_object.get_input(" Department name ")
        insert_query = "INSERT INTO departments(dp_name) VALUES(%s)"
        if self.sql_object.insert_query_operation(insert_query, (str_department_name,)):
            print("Added department")
        else:
            print(f"Error at {insert_query}, {str_department_name}")

    def delete_department(self):
        """
        Delete department from the departments table.
        :return: nothing
        """
        str_department_name = self.utility_object.get_input(" Department name ")
        delete_query = "DELETE FROM departments WHERE dp_name = %s"
        if self.sql_object.delete_query_operation(delete_query, (str_department_name,)):
            print("deleted department")
        else:
            print(f"{str_department_name} doesnt exist")

    def update_department(self):
        """
        update department from the departments table.
        :return: nothing
        """
        old_department_name = self.utility_object.get_input(" Present Department name ")
        new_department_name = self.utility_object.get_input(" new Department name ")
        update_query = "UPDATE departments SET dp_name = %s WHERE dp_name = %s"
        if self.sql_object.update_query_operation(update_query, (new_department_name, old_department_name, )):
            print("updated department")
        else:
            print(f"{old_department_name} doesnt exist")

    def print_departments_table(self):
        """
        Fetch departments table and print it
        :return:
        """
        fetch_query = "SELECT * FROM departments"
        cursor_obj = self.sql_object.select_query_operation(fetch_query)
        for row in cursor_obj.fetchall():
            print(row)
