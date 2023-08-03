import os
import canvasapi
import dotenv
from time import sleep
import logging as log

log.basicConfig(format='%(levelname)s:%(message)s', level=log.WARNING)

dotenv.load_dotenv(dotenv.find_dotenv())

# TOKEN is in the .env file. If you don't publish any of this anywhere then you don't need .env file and can just write
# in the TOKEN and USER_ID here.
TOKEN = os.environ.get('API_TOKEN')
BASEURL = 'https://wpi.instructure.com'  # WPI canvas API endpoint
ALLOWED_FILE_TYPES = ['pdf', 'pptx', 'docx']

class API:
    def __init__(self, api: canvasapi.Canvas) -> None:
        self.user_id = api.get_current_user()
        self.user = api.get_user(self.user_id)
        self.courses = api.get_courses()
        self.removing_courses = []
        self.courses_to_download = []
    
    def log_course_names(self):
        """_summary_
        Print all of the courses withing the `courses` object above
        """
        for course in self.courses:
            try:
                log.info(course.name)
            except Exception as ex:
                log.warning('Could not print course name', exc_info=ex)

    def get_courses_to_download(self):
        """_summary_
        Get all of the courses to download by only adding the ones not specified in the `removing_courses` list
        """
        for course in self.courses:
            try:
                if course.name not in self.removing_courses and course.name == 'Data Analytics And Statistical Learning':
                    self.courses_to_download.append(course)
            except:
                log.info('Could did not have "name" attribute, trying "display_name"')
                try:
                    if course.display_name not in self.removing_courses and course.name == 'Data Analytics And Statistical Learning':
                        self.courses_to_download.append(course)
                except:
                    log.warning(f'Could not add course to download list. Course has no code or name.')
    
    def get_course_files(self):
        """_summary_
        Download all of the courses into a 'data' directory, will be in the same directory as this script.
        """
        for course in self.courses_to_download:
            try:
                log.warning(f'Trying to download files for: {course.name}')
                try:
                    files = course.get_files()
                    for file in files:
                        try:
                            file_type = file.display_name.split('.')[1]
                            if file_type in ALLOWED_FILE_TYPES:
                                log.info(f'Downloading {str(file)}')
                                file.download(f'data/{str(file)}')
                        except:
                            log.warning(f'Failed downloading {str(file)}')
                except:
                    log.info(f'Failed downloading some files.')
            except:
                log.info(f'Could not download any course information.')
            sleep(0.2) # some time b/n request
if __name__ == '__main__':
    canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

    api = API(canvas_api)

    api.get_courses_to_download()

    api.get_course_files()
