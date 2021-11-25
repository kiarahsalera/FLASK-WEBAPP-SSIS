from re import search
from webapp_ssis import college, course, mysql
import mysql.connector as mysql
from flaskext.mysql import MySQL
from flask import jsonify
import os 
from dotenv import load_dotenv


load_dotenv()
HOST = os.getenv('DB_HOST')
USERNAME = os.getenv('DB_USERNAME')
NAME = os.getenv('DB_NAME')


database = mysql.connect(
        host=HOST,
        user=USERNAME,
        database=NAME
    )
cursor = database.cursor(buffered=True)

class Student():
    
    def __init__(
        self, 
        id_no: str = None,
        first_name: str = None,
        last_name: str = None,
        course: str = None,
        year_level: str = None,
        gender: str = None,
        photo: str = None) -> None:
    

        self.id_no = id_no
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.year_level = year_level
        self.gender = gender
        self.photo = photo


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
        query = "INSERT INTO student(id_no, first_name, last_name, course, year_level, gender, photo) \
                VALUES (%s,%s,%s,%s,%s,%s)"
        data = [self.id_no, self.first_name, self.last_name, self.course, self.year_level, self.gender, self.photo]
        cursor.execute(query, data)
        database.commit() 

    @classmethod
    def display_students(self)-> list:
        query = '''
            SELECT id_no,
                    photo, 
                   first_name,  
                   last_name, 
                   course, 
                   year_level, 
                   gender,
                   course.code_name
            FROM student
            JOIN course
            ON student.course = course.code
            
        '''
        cursor.execute(query)  
        result = cursor.fetchall() 
        student = [list(student) for student in result]
        return student

    @staticmethod
    def get_student(id_no: str = None) -> str:
        query = f'''
           SELECT id_no, 
                   first_name,  
                   last_name,   
                   course, 
                   year_level, 
                   gender 
            FROM student
            WHERE id_no = '{id_no}'
        '''
        cursor.execute(query)
        student = list(cursor.fetchone())
        return student

    @staticmethod
    def delete(id_no: str = None) -> None:
        query = f'''
            DELETE FROM student
            WHERE id_no='{id_no}'
        '''
        cursor.execute(query)
        database.commit()
        return None

    @classmethod
    def edit_student(cls, id_no, first_name, last_name, course, year_level, gender, old_id_number):
        query = "UPDATE student SET id_no=%s, first_name=%s, last_name=%s, course=%s, year_level=%s, \
                gender=%s WHERE id_no=%s"
        data = [id_no, first_name, last_name, course, year_level, gender, old_id_number]
        cursor.execute(query,data)
        database.commit()


class Course():
    def __init__(
        self, 
        code: str = None,
        code_name: str = None,
        college_name: str = None) -> None:


        self.code = code 
        self.code_name = code_name
        self.college_name = college_name


    def search(self, keyword: str = None, field: str = None) -> list:
        keyword = keyword.upper()
        course = self.display_course()
        result = []

        if field is None: 
            result = self.search_by_field(course, keyword, 'all')
        elif field == 'code':
            result = self.search_by_field(course, keyword, 'code')
        elif field == 'code_name':
            result = self.search_by_field(course, keyword, 'code_name')
        elif field == 'college_name':
            result = self.search_by_field(course, keyword, 'college_name')
        
        return result


    @staticmethod
    def search_by_field(rows: list = None, keyword: str = None, field: str = None) -> list:
        result = []
        for row in rows:
            row_allcaps = [str(cell).upper() for cell in row]

            if field == 'all':
                if keyword in row_allcaps:
                    result.append(row)
            elif field == 'code':
                if keyword == row_allcaps[0]:
                    result.append(row)
                    return result
            elif field == 'code_name':
                if keyword == row_allcaps[1]:
                    result.append(row)
            elif field == 'college_name':
                if keyword == row_allcaps[2]:
                    result.append(row)

        return result


    def add_course(self):
        query = "INSERT INTO course(code, code_name, college_name) VALUES \
                 (%s,%s,%s)"
        data = [self.code, self.code_name, self.college_name]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def display_course(self)-> list:
        query = '''
            SELECT course.code, 
                   course.code_name,  
                   course.college_name 
            FROM course
            JOIN college
            ON course.college_name = college.college_code
            
        '''
        cursor.execute(query)
        result = cursor.fetchall() 
        course = [list(course) for course in result]
        return course
        
    @staticmethod
    def get_coursecode_for(course_name: str = None) -> str:
        query = f'''
                SELECT code
                FROM course
                WHERE code_name = '{course_name}'
            '''
        cursor.execute(query)
        coursecode = cursor.fetchone()
        return coursecode[0]

    @staticmethod
    def get_collegecode(course_name: str = None) -> str:
        query = f'''
            SELECT course.code_name, college.college_code
            FROM course
            JOIN college
            ON course.college_name = college.college_code
            WHERE course.code_name = '{course_name}'
            LIMIT 1
        '''
        cursor.execute(query)
        _, collegecode = cursor.fetchone()
        return collegecode

 
    @classmethod
    def edit_course(cls, code, code_name, college_name, old_course_code):
        query = "UPDATE course SET code=%s, code_name=%s, college_name=%s WHERE code=%s"
        data = [code, code_name, college_name, old_course_code]
        cursor.execute(query, data)
        database.commit()

    @staticmethod
    def delete(code: str = None) -> None:
        query = f'''
            DELETE FROM course
            WHERE code='{code}'
        '''
        cursor.execute(query)
        database.commit()
        return None

class College():
    def __init__(
        self, 
        college_code: str = None,
        colcode_name: str = None) -> None:

        self.college_code = college_code 
        self.colcode_name = colcode_name

    def search(self, keyword: str = None, field: str = None) -> list:
        keyword = keyword.upper()
        college = self.display_college()
        result = []

        if field is None: 
            result = self.search_by_field(college, keyword, 'all')
        elif field == 'college_code':
            result = self.search_by_field(college, keyword, 'college_code')
        elif field == 'colcode_name':
            result = self.search_by_field(college, keyword, 'colcode_name')
        
        return result

    @staticmethod
    def search_by_field(rows: list = None, keyword: str = None, field: str = None) -> list:
        result = []
        for row in rows:
            row_allcaps = [str(cell).upper() for cell in row]

            if field == 'all':
                if keyword in row_allcaps:
                    result.append(row)
            elif field == 'college_code':
                if keyword == row_allcaps[0]:
                    result.append(row)
                    return result
            elif field == 'colcode_name':
                if keyword == row_allcaps[1]:
                    result.append(row)

        return result

    
    def add_college(self):
        query = "INSERT INTO college(college_code, colcode_name) VALUES \
                 (%s,%s)"
        data = [self.college_code, self.colcode_name]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def display_college(self)-> list:
        query = '''
            SELECT college_code, 
                   colcode_name  
            FROM college
            
        '''
        cursor.execute(query)
        result = cursor.fetchall() 
        college = [list(college) for college in result]
        return college

    @classmethod
    def edit_college(cls, college_code, colcode_name, old_college_code):
        query = "UPDATE college SET college_code=%s, colcode_name=%s WHERE college_code=%s"
        data = [college_code, colcode_name, old_college_code]
        cursor.execute(query, data)
        database.commit()

    @staticmethod
    def delete(college_code: str = None) -> None:
        query = f'''
            DELETE FROM college
            WHERE college_code='{college_code}'
        '''
        cursor.execute(query)
        database.commit()
        return None
