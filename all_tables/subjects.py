import pymysql

from SQL.sql_operations import SQLOperations
from utilities.table_utilitis import TableUtilities
import logging


class Subjects:

    logging.basicConfig(filename='log.log', filemode='a', format=f'%(asctime)s - %(message)s \n', level=logging.DEBUG)

    def __init__(self):
        self.utility_object = TableUtilities()
        self.sql_object = SQLOperations()

    def add_subject(self):
        """
        Add subject to subject table.
        :return: nothing
        """
        str_subject_name = self.utility_object.get_input(" Subject name ")
        str_department_name = self.utility_object.get_input(" Department name ")
        department_id_query = "SELECT dp_id FROM departments WHERE dp_name=%s"
        insert_query = "INSERT INTO subjects(sub_name, dp_id) VALUES(%s, %s)"

        department_id = self.sql_object.get_value_query_operation(department_id_query, (str_department_name,))
        data = (str_subject_name, department_id, )
        if self.sql_object.insert_query_operation(insert_query, data):
            print("Added subject")
        else:
            print(f"Error at {insert_query}, {str_subject_name}, {str_department_name}")

    def delete_subject(self):
        """
        Delete a subject from the subject table.
        :return: nothing
        """
        str_subject_name = self.utility_object.get_input(" Subject name ")
        delete_query = "DELETE FROM subjects WHERE sub_name = %s"
        if self.sql_object.delete_query_operation(delete_query, (str_subject_name,)):
            print("Deleted")
        else:
            print(f"{str_subject_name} doesnt exist")

    def update_subject(self, column_name):
        """
        update subject from the subject table.
        :return: nothing
        """
        column = None
        if column_name == "subject":
            column = "sub_name"
        else:
            column = "dp_id"
            dp_id_query = "SELECT dp_id FROM departments WHERE dp_name=%s"
            new_dp_name = self.utility_object.get_input(f" new department name ")
            subject_name = self.utility_object.get_input(f" subject name ")
            update_query = "UPDATE subjects SET dp_id = %s WHERE sub_name = %s"
            department_id = self.sql_object.get_value_query_operation(dp_id_query, (new_dp_name,))
            if self.sql_object.update_query_operation(update_query, (department_id, subject_name,)):
                print("updated subject")
            else:
                print(f"error while updating subject")
        old_name = self.utility_object.get_input(f" old {column_name} name ")
        new_name = self.utility_object.get_input(f" new {column_name}name ")
        update_query = "UPDATE subjects SET sub_name = %s WHERE sub_name = %s"
        if self.sql_object.update_query_operation(update_query, (new_name, old_name, )):
            print("updated subject")
        else:
            print(f"{old_name} doesnt exist")

    def print_subjects_table(self):
        """
        Print subjects table row by row.
        :return:
        """
        fetch_query = "SELECT * FROM subjects"
        cursor_obj = self.sql_object.select_query_operation(fetch_query)
        for row in cursor_obj.fetchall():
            print(row)