from SQL.sql_object_adapter import SqlObjectAdapter
from utilities.table_utilitis import TableUtilities
import logging


class Teachers:

    logging.basicConfig(filename='log.log', filemode='a', format=f'%(asctime)s - %(message)s \n', level=logging.DEBUG)

    def __init__(self):
        self.utility_object = TableUtilities()
        self.sql_object = SqlObjectAdapter.return_sql()

    def add_teacher(self):
        """
        Add teacher to the teacher table
        :return: nothing
        """
        str_first_name = self.utility_object.get_input(" First name ")
        str_last_name = self.utility_object.get_input(" Last name ")
        str_email = self.utility_object.get_input(" email ")
        str_subject_name = self.utility_object.get_input(" Subject name ")

        subject_id_query = "SELECT sub_id FROM subjects WHERE sub_name=%s"
        insert_query = "INSERT INTO teachers(teacher_first_name, teacher_last_name, email, sub_id) " \
                       "VALUES(%s, %s, %s, %s)"

        subject_id = self.sql_object.get_value_query_operation(subject_id_query, (str_subject_name,))

        data = (str_first_name, str_last_name, str_email, subject_id,)
        if self.sql_object.insert_query_operation(insert_query, data):
            print("Added teacher")
        else:
            print(f"Error at add teacher, given teacher_name: {str_first_name} {str_last_name}, "
                  f" and sub_name: {str_subject_name} does'nt exist")

    def delete_teacher(self):
        """
        Delete teacher from the teacher table.
        :return:
        """
        str_first_name = self.utility_object.get_input(" First name ")
        str_last_name = self.utility_object.get_input(" Last name ")
        delete_query = "DELETE FROM teachers WHERE teacher_first_name = %s AND teacher_last_name = %s"

        data = (str_first_name, str_last_name,)
        if self.sql_object.delete_query_operation(delete_query, data):
            print("deleted teacher")
        else:
            print(f"{str_first_name} {str_last_name} doesnt exist")

    def update_teacher(self, column_name):
        """
        update teacher from the teacher table.
        :return: nothing
        """
        column = None
        if column_name == "teacher_first_name":
            column = "teacher_first_name"
        elif column_name == "teacher_last_name":
            column = "teacher_first_name"
        else:
            column = "sub_id"

        old_name = self.utility_object.get_input(f" old {column} name ")
        new_name = self.utility_object.get_input(f" new {column}name ")
        update_query = f"UPDATE teachers SET {column} = %s WHERE {column} = %s"
        if self.sql_object.update_query_operation(update_query, (new_name, old_name, )):
            print("updated teachers")
        else:
            print(f"{old_name} doesnt exist")

    def print_teachers_table(self):
        """
        Print teacher table row by row.
        :return:
        """
        fetch_query = "SELECT * FROM teachers"
        cursor_obj = self.sql_object.select_query_operation(fetch_query)
        for row in cursor_obj.fetchall():
            print(row)
