from webapp_ssis import mysql
import mysql.connector as mysql
from flaskext.mysql import MySQL


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

    @classmethod  
    def search_student(cls, key):
        query = "SELECT * FROM student WHERE id_no=%s or first_name=%s or last_name=%s"
        data = [key, key]
        cursor.execute(query,data)
        data = cursor.fetchall()
        return data


class Course():
    def __init__(self, code, code_name, college_name):
        self.code = code 
        self.code_name = code_name
        self.college_name = college_name

    @classmethod
    def get_course(cls):
        query = "SELECT * FROM course"
        cursor.execute(query)
        course = cursor.fetchall()
        return course 
    
    def add_course(self):
        query = "INSERT INTO course(code, code_name, college_name) VALUES \
                 (%s,%s,%s)"
        data = [self.code, self.code_name, self.college_name]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def display_course(cls):
        query = "SELECT * FROM course"
        cursor.execute(query)
        course = cursor.fetchall()
        return course

    @classmethod
    def edit_course(cls, code, code_name, college_name, old_course_code):
        query = "UPDATE course SET code=%s, code_name=%s, college_name=%s WHERE code=%s"
        data = [code, code_name, college_name, old_course_code]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def delete_course(cls, code):
        query = "DELETE FROM course WHERE code=%s"
        data = [code]
        cursor.execute(query, data)
        database.commit()

class College():
    def __init__(self, college_code, colcode_name):
        self.college_code = college_code 
        self.colcode_name = colcode_name

    @classmethod
    def get_college(cls):
        query = "SELECT * FROM college"
        cursor.execute(query)
        college = cursor.fetchall()
        return college
    
    def add_college(self):
        query = "INSERT INTO college(college_code, colcode_name) VALUES \
                 (%s,%s)"
        data = [self.college_code, self.colcode_name]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def display_college(cls):
        query = "SELECT * FROM college"
        cursor.execute(query)
        college = cursor.fetchall()
        return college

    @classmethod
    def edit_college(cls, college_code, colcode_name, old_college_code):
        query = "UPDATE college SET college_code=%s, colcode_name=%s WHERE college_code=%s"
        data = [college_code, colcode_name, old_college_code]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def delete_college(cls, college_code):
        query = "DELETE FROM college WHERE college_code=%s"
        data = [college_code]
        cursor.execute(query, data)
        database.commit()
