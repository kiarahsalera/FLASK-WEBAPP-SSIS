from webapp_ssis import mysql
import mysql.connector as mysql


database = mysql.connect(
    host = 'localhost',
    user = 'root',
    password= '',
    database = 'ssis-webapp'
    )

cursor = database.cursor() 

class Student():
    
    def __init__(self, id_no, first_name, last_name, course, year_level, gender):
        self.id_no = id_no
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.year_level = year_level
        self.gender = gender

    def add_student(self):
        query = "INSERT INTO student(id_no, first_name, last_name, course, year_level, gender) \
                VALUES (%s,%s,%s,%s,%s,%s)"
        data = [self.id_no, self.first_name, self.last_name, self.course, self.year_level, self.gender]
        cursor.execute(query, data)
        database.commit() 

    @classmethod
    def display_students(cls):
        query = "SELECT * FROM student"
        cursor.execute(query)    
        student = cursor.fetchall()
        return student

    @classmethod
    def delete_student(cls, id_no):
        query = "DELETE FROM student WHERE id_no=%s"
        data = [id_no]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def edit_student(cls, id_no, first_name, last_name, course, year_level, gender, old_id_number):
        query = "UPDATE student SET id_no=%s, first_name=%s, last_name=%s, course=%s, year_level=%s, \
                gender=%s WHERE id_no=%s"
        data = [id_no, first_name, last_name, course, year_level, gender, old_id_number]
        cursor.execute(query,data)
        database.commit()
 