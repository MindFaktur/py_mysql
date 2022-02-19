from SQL.sql_object_adapter import SqlObjectAdapter
from utilities.table_utilitis import TableUtilities
import logging


class Students:
    logging.basicConfig(filename='log.log', filemode='a', format=f'%(asctime)s - %(message)s \n', level=logging.DEBUG)

    def __init__(self):
        self.utility_object = TableUtilities()
        self.sql_object = SqlObjectAdapter.return_sql()

    def add_student(self):
        """
        Add student to the student table
        :return: nothing
        """
        str_first_name = self.utility_object.get_input(" Student first name ")
        str_last_name = self.utility_object.get_input(" Student last name ")
        str_teacher_first_name = self.utility_object.get_input(" Teacher fist name teaching the student ")
        str_teacher_last_name = self.utility_object.get_input(" Teacher last name teaching the student ")

        teacher_id_query = "SELECT teacher_id FROM teachers WHERE teacher_first_name = %s AND teacher_last_name = %s"
        insert_query = "INSERT INTO students(student_first_name, student_last_name, teacher_id) " \
                       "VALUES(%s, %s, %s)"
        data = (str_teacher_first_name, str_teacher_last_name,)
        teacher_id = self.sql_object.get_value_query_operation(teacher_id_query, data)

        data = (str_first_name, str_last_name, teacher_id,)
        if self.sql_object.insert_query_operation(insert_query, data):
            print("Student Added")
        else:
            print(f"Error at add student, given student_name: {str_first_name} {str_last_name}"
                  f" and teacher_name: {str_teacher_first_name} {str_teacher_last_name} does'nt exist")

    def delete_student(self):
        """
        Delete the student from the students table.
        :return: nothing
        """
        str_first_name = self.utility_object.get_input(" Student first name ")
        str_last_name = self.utility_object.get_input(" Student last name ")
        delete_query = "DELETE FROM students WHERE student_first_name = %s AND student_last_name = %s"
        data = (str_first_name, str_last_name,)

        if self.sql_object.delete_query_operation(delete_query, data):
            print("Added teacher")
        else:
            print(f"{str_first_name} {str_last_name} doesnt exist")

    def update_student(self, column_name):
        """
        update student from the student table.
        :return: nothing
        """
        column = None
        if column_name == "student_first_name":
            column = "student_first_name"
        elif column_name == "student_last_name":
            column = "student_last_name"
        else:
            column = "teacher_id"
            stud_first_name = self.utility_object.get_input(" Student first name ")
            stud_last_name = self.utility_object.get_input(" Student last name ")
            str_teacher_first_name = self.utility_object.get_input(" New Teacher fist name teaching the student ")
            str_teacher_last_name = self.utility_object.get_input(" New Teacher last name teaching the student ")
            teacher_id_query = "SELECT teacher_id FROM teachers WHERE " \
                               "teacher_first_name = %s AND teacher_last_name = %s"
            teacher_id = self.sql_object.get_value_query_operation(teacher_id_query,
                                                                   (str_teacher_first_name, str_teacher_last_name))
            update_query = "UPDATE students SET teacher_id = %s WHERE " \
                           "student_first_name = %s AND student_last_name = %s"
            if self.sql_object.update_query_operation(update_query, (teacher_id, stud_first_name,
                                                                     stud_last_name)):
                print("updated student")
            else:
                print(f"error at changing teacher_id in student table")
            return

        old_name = self.utility_object.get_input(f" old {column} name ")
        new_name = self.utility_object.get_input(f" new {column}name ")
        update_query = f"UPDATE students SET {column} = %s WHERE {column} = %s"
        if self.sql_object.update_query_operation(update_query, (new_name, old_name,)):
            print("updated student")
        else:
            print(f"{old_name} doesnt exist")

    def print_students_table(self):
        """
        Print the student table.
        :return: nothing
        """
        fetch_query = "SELECT * FROM students"
        cursor_obj = self.sql_object.select_query_operation(fetch_query)

        for row in cursor_obj.fetchall():
            print(row)
