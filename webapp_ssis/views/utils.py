from webapp_ssis.functions import Student,Course
from werkzeug.utils import secure_filename
import cloudinary.uploader as cloud
import cloudinary.api
import os
from os import getenv

      
def save_image(file: str = None, config=None) -> str:
    local_upload = 'local' == getenv('LOCAL_UPLOAD')
    if local_upload:
        parent_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + \
                        '/static/photo/student/'
        image = file
        filename = secure_filename(file.filename)
        image.save(os.path.join(parent_folder, filename))
        return filename
    else:
        result = cloud.upload(file)
        url = result.get('url')
        return url