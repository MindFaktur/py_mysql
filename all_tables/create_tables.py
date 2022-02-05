

class CreateTables:

    create_departments_table = "CREATE TABLE departments (" \
                               "dp_id INT AUTO_INCREMENT PRIMARY KEY," \
                               "dp_name VARCHAR(50) UNIQUE " \
                               ")"

    create_subjects_table = "CREATE TABLE subjects (" \
                            "sub_id INT AUTO_INCREMENT PRIMARY KEY," \
                            "sub_name VARCHAR(50) UNIQUE, " \
                            "dp_id INT," \
                            "FOREIGN KEY (dp_id) REFERENCES departments(dp_id) ON DELETE CASCADE" \
                            ");"

    create_teachers_table = "CREATE TABLE teachers (" \
                            "teacher_id INT AUTO_INCREMENT PRIMARY KEY," \
                            "teacher_first_name VARCHAR(50), " \
                            "teacher_last_name VARCHAR(50), " \
                            "email VARCHAR(50) UNIQUE, " \
                            "sub_id INT," \
                            "FOREIGN KEY (sub_id) REFERENCES subjects(sub_id) ON DELETE CASCADE" \
                            ");"

    create_students_table = "CREATE TABLE students (" \
                            "student_id INT AUTO_INCREMENT PRIMARY KEY," \
                            "student_first_name VARCHAR(50), " \
                            "student_last_name VARCHAR(50), " \
                            "teacher_id INT," \
                            "FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE" \
                            ");"

    left_join_statement = "SELECT students.student_first_name, students.student_last_name, " \
                          "teachers.teacher_first_name, " \
                          "teachers.teacher_last_name, subjects.sub_name, departments.dp_name" \
                          " FROM students " \
                          " LEFT JOIN teachers USING(teacher_id) " \
                          " LEFT JOIN subjects USING(sub_id) " \
                          " LEFT JOIN departments USING(dp_id) "
