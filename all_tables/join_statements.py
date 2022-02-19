from SQL.sql_object_adapter import SqlObjectAdapter
from SQL.sql_operations import SQLOperations


class JoinFunctions:

    def __init__(self):
        self.sql_object = SqlObjectAdapter.return_sql()

    def print_left_join_table(self):
        """
        Print's values from the result of left join.
        :return: nothing
        """

        fetch_query = "SELECT students.student_first_name, students.student_last_name, " \
                      "teachers.teacher_first_name, " \
                      "teachers.teacher_last_name, subjects.sub_name, departments.dp_name" \
                      " FROM students " \
                      " LEFT JOIN teachers USING(teacher_id) " \
                      " LEFT JOIN subjects USING(sub_id) " \
                      " LEFT JOIN departments USING(dp_id) "
        cursor_obj = self.sql_object.select_query_operation(fetch_query)
        print("------------- Left Join Result ---------------")
        for row in cursor_obj.fetchall():
            print(row)
        print("------------------ END ----------------")

    def print_right_join_table(self):
        """
        Print's values from the result of right join.
        :return:
        """

        fetch_query = "SELECT students.student_first_name, students.student_last_name, " \
                      "teachers.teacher_first_name, " \
                      "teachers.teacher_last_name, subjects.sub_name, departments.dp_name" \
                      " FROM students " \
                      " RIGHT JOIN teachers USING(teacher_id) " \
                      " RIGHT JOIN subjects USING(sub_id) " \
                      " RIGHT JOIN departments USING(dp_id) "
        cursor_obj = self.sql_object.select_query_operation(fetch_query)
        print("------------- Right Join Result ---------------")
        for row in cursor_obj.fetchall():
            print(row)
        print("------------------ END ----------------")

    def print_cross_join_table(self):
        """
        Print's values from the result of cross join.
        :return:
        """

        fetch_query = "SELECT students.student_first_name, students.student_last_name, " \
                      "teachers.teacher_first_name, " \
                      "teachers.teacher_last_name, subjects.sub_name, departments.dp_name" \
                      " FROM students " \
                      " CROSS JOIN teachers USING(teacher_id) " \
                      " CROSS JOIN subjects USING(sub_id) " \
                      " CROSS JOIN departments USING(dp_id) "
        cursor_obj = self.sql_object.select_query_operation(fetch_query)
        print("------------- Cross Join Result ---------------")
        for row in cursor_obj.fetchall():
            print(row)
        print("------------------ END ----------------")

    def print_inner_join_table(self):
        """
        Print's values from the result of inner join.
        :return:
        """

        fetch_query = "SELECT students.student_first_name, students.student_last_name, " \
                      "teachers.teacher_first_name, " \
                      "teachers.teacher_last_name, subjects.sub_name, departments.dp_name" \
                      " FROM students " \
                      " INNER JOIN teachers USING(teacher_id) " \
                      " INNER JOIN subjects USING(sub_id) " \
                      " INNER JOIN departments USING(dp_id) "
        cursor_obj = self.sql_object.select_query_operation(fetch_query)
        print("------------- Inner Join Result ---------------")
        for row in cursor_obj.fetchall():
            print(row)
        print("------------------ END ----------------")
