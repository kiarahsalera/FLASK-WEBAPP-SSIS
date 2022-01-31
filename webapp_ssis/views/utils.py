from webapp_ssis.functions import Student,Course,College
from werkzeug.utils import secure_filename
import cloudinary.uploader as cloud
import os
from os import getenv

def add_student(student: list) -> bool:
    id_no = student['id_no'].strip()
    first_name = student['first_name']
    last_name = student['last_name']
    course = student['course']
    year_level = student['year_level']
    gender = student['gender']
    photo = student['photo']
    
    if id_no:
        if id_no not in Student().get_ID():
           
            if first_name and last_name:
                Student(
                    id_no=id_no,  
                    first_name=first_name,
                    last_name=last_name,
                    year_level=year_level,
                    gender=gender,  
                    course=course,
                    photo = photo
                ).add_student()
                return True
            else:
                return False
        else:
            return False


def update_student_record(student: list = None) -> bool:
    id_no = student['id_no']
    first_name = student['first_name']
    last_name = student['last_name']
    course = student['course']
    year_level = student['year_level']
    gender = student['gender']
    photo = student['photo']
    
    if first_name and last_name:
        if photo:
            Student(
                id_no=id_no, 
                first_name=first_name,
                last_name=last_name,
                course=course,
                year_level=year_level,
                gender=gender, 
                photo=photo
                ).edit_student()
        else:
            Student(
                id_no=id_no, 
                first_name=first_name,
                last_name=last_name,
                 course=course,
                year_level=year_level,
                gender=gender
                ).edit_student()
            return None
    else:
        return False
     
def save_image(file: str = None, config=None) -> str:
    local_upload = 'local' == getenv('PHOTO_UPLOAD')
    if local_upload:
        parent_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + \
                        '/static/photo/student'
        image = file
        filename = secure_filename(file.filename)
        image.save(os.path.join(parent_folder, filename))
        return filename
    else:
        result = cloud.upload(file)
        url = result.get('url')
        return url

def delete_image(id_no: str = None) -> bool:
    local_upload = 'local' == getenv('LOCAL_UPLOAD')
    if not local_upload:
        image_url = (Student().get_image_url(id_no))[0]
        file_name = (image_url.split('/')[-1]).split('.')[0]
        print(file_name)
        cloud.destroy(file_name)
    return 

def add_courses(course: str = None) -> bool:
    code = (course['code'].strip()).upper()
    code_name = (course['code_name'])
    college_name = (course['college_name'])
    # code validation
    if code and code:
        # name validation
        if code_name:
            Course(
                code,
                code_name,
                college_name
            ).add_course()
            return None
        else:
            return False
    return False

def update_course(course: str = None) -> bool:
    code = course['code']
    code_name = course['code_name'].strip()
    college_name = course['college_name']
    print(code, code_name, college_name)

    if code and code_name:
        Course(
            code,
            code_name,
            college_name
        ).edit_course()
        return None
    else:
        return False

def add_colleges(college: str = None) -> bool:
    college_code = (college['college_code'].strip()).upper()
    colcode_name = (college['colcode_name'].strip()).title()
    # code validation
    if college_code and college_code not in College().get_collegecode():
        # name validation
        if colcode_name:
            College(
                college_code,
                colcode_name
            ).add_college()
            return None
        else:
            return False
    return False


def update_college(college: str = None) -> bool:
    college_code = college['college_code']
    colcode_name = college['colcode_name'].strip()
    
    if colcode_name:
        College(
            college_code,
            colcode_name
        ).edit_college()
        return None
    else:
        return False