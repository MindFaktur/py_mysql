import pymysql

from SQL.sql_object_adapter import SqlObjectAdapter
from SQL.sql_operations import SQLOperations
from all_tables.departments import Departments
from all_tables.join_statements import JoinFunctions
from all_tables.students import Students
from all_tables.subjects import Subjects
from all_tables.teachers import Teachers


class Operations:

    def operation(self):
        """
        Perform operations until the exit value is clicked.
        :return: nothing
        """
        option = self.main_menu()
        exit_at = 19
        while option != exit_at:
            self.menu_operations(option)
            option = self.main_menu()

    def main_menu(self):
        """
        Shows all operations available
        :return: use choice(operation)
        """
        user_choice = int(input(f" Press "
                                "\n 1) Add Department " +
                                "\n 2) Delete Department " +
                                "\n 3) Print Departments " +
                                "\n 4) Add Subject " +
                                "\n 5) Delete Subject " +
                                "\n 6) Print Subjects " +
                                "\n 7) Add Teacher " +
                                "\n 8) Delete Teacher " +
                                "\n 9) Print Teachers " +
                                "\n 10) Add Student " +
                                "\n 11) Delete Student " +
                                "\n 12) Print Students " +
                                "\n 13) Print left join " +
                                "\n 14) Print right join " +
                                "\n 15) Print cross join " +
                                "\n 16) Print inner join " +
                                "\n 17) Update Department in department table" +
                                "\n 18) Update other tables" +
                                "\n 19) Quit " +
                                "\n "
                                ))

        return user_choice

    def update_operations(self):

        user_choice = int(input(f" Press "
                                "\n 1) Update subject in subject table" +
                                "\n 2) Update department of subject in subject table" +
                                "\n 3) Update teacher first name of teachers table" +
                                "\n 4) Update teacher last name of teachers table" +
                                "\n 5) Update subject name of teachers table" +
                                "\n 6) Update student first name of students table" +
                                "\n 7) Update student last name of students table" +
                                "\n 8) Update teacher name of students table" +
                                "\n 9) Quit " +
                                "\n "
                                ))
        sub = Subjects()
        teach = Teachers()
        stud = Students()

        sql_obj = SqlObjectAdapter.return_sql()

        choices = ("subject", "dp_id", "teacher_first_name", "teacher_last_name", "sub_id",
                   "student_first_name", "student_last_name", "teacher_name")
        functions_dict = {1: sub.update_subject, 2: sub.update_subject, 3: teach.update_teacher,
                          4: teach.update_teacher, 5: teach.update_teacher, 6: stud.update_student,
                          7: stud.update_student, 8: stud.update_student
                          }
        if user_choice == 9:
            return
        functions_dict.get(user_choice)(choices[user_choice - 1])
        sql_obj.close_sql()

    def menu_operations(self, choice):
        """
        Performs the user chosen operation
        :param choice: user choice which we get from the main menu
        :return: nothing
        """
        dp = Departments()
        sub = Subjects()
        teach = Teachers()
        stud = Students()
        joins = JoinFunctions()

        sql_obj = SqlObjectAdapter.return_sql()

        functions_dict = {1: dp.add_department, 2: dp.delete_department, 3: dp.print_departments_table,
                          4: sub.add_subject, 5: sub.delete_subject, 6: sub.print_subjects_table,
                          7: teach.add_teacher, 8: teach.delete_teacher, 9: teach.print_teachers_table,
                          10: stud.add_student, 11: stud.delete_student, 12: stud.print_students_table,
                          13: joins.print_left_join_table, 14: joins.print_right_join_table,
                          15: joins.print_cross_join_table, 16: joins.print_inner_join_table, 17: dp.update_department,
                          18: self.update_operations
                          }

        functions_dict.get(choice)()
        sql_obj.close_sql()


