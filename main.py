import os
from os.path import join, dirname
import canvasapi
import dotenv
from time import sleep

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('API_TOKEN')
BASEURL = 'https://wpi.instructure.com'
USER_ID = int(os.environ.get('USER_ID'))

# initialize canvas api
canvas_api = canvasapi.Canvas(BASEURL, TOKEN)
# initialize the user object
user = canvas_api.get_user(USER_ID)

# get all of the users courses
courses = user.get_courses()


def print_course_names():
    """_summary_
    Print all of the courses withing the `courses` object above
    """
    for course in courses:
        try:
            print(course.name)
        except:
            print('Could not print course name')


# uncomment the line below to see all course names
# print_course_names()

# delete this list and make your own
removing_courses = ['ID 2050 Prague A term', 'HISTORY OF AMERICAN POPULAR MUSIC (Latin American Stream)', 'Geology',
                    'AMERICAN HISTORY, 1877-1920', 'ANIMAL BEHAVIOR', 'CHEMICAL REACTIONS LAB', 'CS Undergraduate Advising Site', 'ID 2050 Prague A term',
                    'INQUIRY SEMINAR IN HUMANITIES AND ARTS', 'INTRODUCTION TO BIOLOGY', 'ITS Scavenger Hunt 2018', 'MODERN EUROPEAN HISTORY',
                    'NECHE Accreditation - Students', 'ODE C07, C09-C12', 'Online Success Coach Resources', 'ORDINARY DIFFERENTIAL EQUATIONS',
                    'Ordinary Differential Equations', 'ORDINARY DIFFERENTIAL EQUATIONS (A20 DTang)', 'ORDINARY DIFFERENTIAL EQUATIONS (D06-D11)',
                    'TA/GLA/PLA Training - Math', 'THE SHAPING OF POST-1920 AMERICA', 'TOPICS IN INTERNATIONAL POLITICS',
                    "'20-'21 Ready to Launch – Global Projects"]

courses_to_download = []


def get_courses_to_download():
    """_summary_
    Get all of the courses to download by only adding the ones not specified in the `removing_courses` list
    """
    for course in courses:
        try:
            if course.name not in removing_courses:
                courses_to_download.append(course)
        except:
            print('Could not add course to list')


get_courses_to_download()


def get_course_files():
    """_summary_
    Download all of the courses into the 'data' directory
    """
    course_bad_counter = 0
    for course in courses_to_download:
        try:
            print(f'Course name: {course.name}')
            try:
                files = course.get_files()
                for file in files:
                    try:
                        print(f'Downloading {str(file)}')
                        file.download(f'data/{str(file)}.pdf')
                    except:
                        print(f'Failed downloading {str(file)}')
            except:
                print(f'Could not find file in course {course.name}')
        except:
            course_bad_counter += 1
            print(
                f'Could not print/download course information for {course_bad_counter} courses')
        sleep(0.5)
    print(f'{course_bad_counter} courses could not be downloaded')


# uncomment the following line to begin downloading courses
# get_course_files()
