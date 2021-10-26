from re import search
from webapp_ssis import mysql
import mysql.connector as mysql
from flaskext.mysql import MySQL
from flask import jsonify



database = mysql.connect(
    host = 'localhost',
    user = 'root',
    password= '',
    database = 'ssis-webapp'
    )

cursor = database.cursor() 

class Student():
    
    def __init__(
        self, 
        id_no: str = None,
        first_name: str = None,
        last_name: str = None,
        course: str = None,
        year_level: str = None,
        gender: str = None) -> None:
    

        self.id_no = id_no
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.year_level = year_level
        self.gender = gender


    def search(self, keyword: str = None, field: str = None) -> list:
        keyword = keyword.upper()
        student = self.display_students()
        result = []

        if field is None: 
            result = self.search_by_field(student, keyword, 'all')
        elif field == 'id_no':
            result = self.search_by_field(student, keyword, 'id_no')
        elif field == 'first_name':
            result = self.search_by_field(student, keyword, 'first_name')
        elif field == 'last_name':
            result = self.search_by_field(student, keyword, 'last_name')
        elif field == 'course':
            result = self.search_by_field(student, keyword, 'course')
        elif field == 'year_level':
            result = self.search_by_field(student, keyword, 'year_level')
        elif field == 'gender':
            result = self.search_by_field(student, keyword, 'gender')
        
        return result


    @staticmethod
    def search_by_field(rows: list = None, keyword: str = None, field: str = None) -> list:
        result = []
        for row in rows:
            row_allcaps = [str(cell).upper() for cell in row]

            if field == 'all':
                if keyword in row_allcaps:
                    result.append(row)
            elif field == 'id_no':
                if keyword == row_allcaps[0]:
                    result.append(row)
                    return result
            elif field == 'first_name':
                if keyword == row_allcaps[1]:
                    result.append(row)
            elif field == 'last_name':
                if keyword == row_allcaps[2]:
                    result.append(row)
            elif field == 'course':
                if keyword == row_allcaps[3]:
                    result.append(row)
            elif field == 'year_level':
                if keyword == row_allcaps[4]:
                    result.append(row)
            elif field == 'gender':
                if keyword == row_allcaps[5]:
                    result.append(row)

        return result




    def add_student(self):
        query = "INSERT INTO student(id_no, first_name, last_name, course, year_level, gender) \
                VALUES (%s,%s,%s,%s,%s,%s)"
        data = [self.id_no, self.first_name, self.last_name, self.course, self.year_level, self.gender]
        cursor.execute(query, data)
        database.commit() 

    @classmethod
    def display_students(self)-> list:
        query = '''
            SELECT id_no, 
                   first_name,  
                   last_name, 
                   course, 
                   year_level, 
                   gender 
            FROM student
            
        '''
        cursor.execute(query)  
        result = cursor.fetchall() 
        student = [list(student) for student in result]
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
