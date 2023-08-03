import os
import canvasapi
import dotenv
from time import sleep
import logging as log

logger = log.getLogger(__name__)
hdlr = log.StreamHandler()
logger.addHandler(hdlr)
logger.level = log.INFO
LOG_TYPE_ERROR = 'Could not access course. Course has no code or name.'

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('API_TOKEN')
BASEURL = 'https://wpi.instructure.com'  # WPI canvas API endpoint, change to your school if applicable
ALLOWED_FILE_TYPES = ['pdf', 'pptx', 'docx'] # edit this list to whatever you want
OUTPUT_DIR = 'data' # edit this to whatever you want

class Downloader:
    def __init__(self, api: canvasapi.Canvas) -> None:
        self.user_id = api.get_current_user()
        self.user = api.get_user(self.user_id)
        self.courses = list(api.get_courses())
        self.removing_courses = []
        self.courses_to_download = []
    
    def remove_bad_courses(self):
        """_summary_
        Print all of the courses withing the courses object above.
        """
        for course in self.courses:
            try:
                logger.info(f'Found good course: {course.name}, code: {course.course_code}')
            except:
                logger.info(f'Removing bad course.')
                self.courses.remove(course)
    
    def download_course(self, course):
        """_summary_
        Download a course's files to the output directory. Will create a subdirectory with the course name.
        """
        try:
            logger.info(f'Trying to download files for: {course.name}')
            files = course.get_files()
            os.mkdir(f'{OUTPUT_DIR}/{course.name}')
            for file in files:
                try:
                    file_type = file.display_name.split('.')[1]
                    if file_type in ALLOWED_FILE_TYPES:
                        logger.info(f'Downloading {str(file)}')
                        file.download(f'{OUTPUT_DIR}/{course.name}/{str(file)}')
                except:
                    logger.warning(f'Failed downloading {str(file)}')
        except:
            logger.warning(LOG_TYPE_ERROR)

    def get_course_files(self):
        """_summary_
        Download all of the courses into a output directory, will be in the same directory as this script.
        """
        for course in self.courses_to_download:
            self.download_course(course)
            sleep(0.2) # some time b/n request

if __name__ == '__main__':
    canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

    downloader = Downloader(canvas_api)

    downloader.remove_bad_courses()

    for course in downloader.courses:
        print(course.name)
        print('Download course? Yes:1, No:0')
        choice = int(input())
        if choice == 1:
            downloader.courses_to_download.append(course)
        elif choice != 0:
            log.error('Please enter only 1 for Yes and 0 for No.')
            exit()

    print('You choose the following courses to download:')
    print([x.name for x in downloader.courses_to_download])
    print('Starting download now...')
    try:
        os.mkdir(OUTPUT_DIR)
    except Exception as ex:
        logger.critical(f'Could not create directory: {OUTPUT_DIR}', ex)
    downloader.get_course_files()
