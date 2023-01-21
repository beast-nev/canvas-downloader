import os
import canvasapi
import dotenv
from time import sleep

dotenv.load_dotenv(dotenv.find_dotenv())

# TOKEN is in the .env file. If you don't publish any of this anywhere then you don't need .env file and can just write
# in the TOKEN and USER_ID here.
TOKEN = os.environ.get('API_TOKEN')
BASEURL = 'https://wpi.instructure.com'  # WPI canvas API endpoint
USER_ID = int(os.environ.get('USER_ID'))

# initialize canvas api with the WPI endpoint and your account token
canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

# initialize your user object with your user ID
user = canvas_api.get_user(USER_ID)

# get all of your courses
courses = user.get_courses()

# list of courses you want to download
courses_to_download = []


def print_course_names():
    """_summary_
    Print all of the courses withing the `courses` object above
    """
    for course in courses:
        try:
            print(course.name)
        except:
            print('Could not print course name')


# delete this list and make your own
removing_courses = ['ID 2050 Prague A term', 'HISTORY OF AMERICAN POPULAR MUSIC (Latin American Stream)', 'Geology',
                    'AMERICAN HISTORY, 1877-1920', 'ANIMAL BEHAVIOR', 'CHEMICAL REACTIONS LAB', 'CS Undergraduate Advising Site', 'ID 2050 Prague A term',
                    'INQUIRY SEMINAR IN HUMANITIES AND ARTS', 'INTRODUCTION TO BIOLOGY', 'ITS Scavenger Hunt 2018', 'MODERN EUROPEAN HISTORY',
                    'NECHE Accreditation - Students', 'ODE C07, C09-C12', 'Online Success Coach Resources', 'ORDINARY DIFFERENTIAL EQUATIONS',
                    'Ordinary Differential Equations', 'ORDINARY DIFFERENTIAL EQUATIONS (A20 DTang)', 'ORDINARY DIFFERENTIAL EQUATIONS (D06-D11)',
                    'TA/GLA/PLA Training - Math', 'THE SHAPING OF POST-1920 AMERICA', 'TOPICS IN INTERNATIONAL POLITICS',
                    "'20-'21 Ready to Launch – Global Projects"]


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


def get_course_files():
    """_summary_
    Download all of the courses into the 'data' directory
    """
    course_bad_counter = 0  # some courses are odd and did not work properly, this will tell you how many you had. I had 5
    for course in courses_to_download:
        try:
            print(f'Course name: {course.name}')
            try:
                files = course.get_files()
                for file in files:
                    try:
                        print(f'Downloading {str(file)}')
                        # you can change the directory name from 'data' to whatever you want
                        file.download(f'data/{str(file)}.pdf')
                    except:
                        print(f'Failed downloading {str(file)}')
            except:
                print(f'Failed downloading some files for {course.name}')
        except:
            course_bad_counter += 1
            print(
                f'Could not print/download course information for {course_bad_counter} courses')
        sleep(0.5)
    print(f'{course_bad_counter} courses could not be downloaded')


if __name__ == '__main__':
    """_summary_
    Follow the GitHub step-by-step before uncommenting these functions below
    """
    # the line below will show you all of your course names
    print_course_names()

    # uncomment the line below to add all of your desired courses to the `courses_to_download` list
    # get_courses_to_download()

    # uncomment the following line to begin downloading courses
    # get_course_files()
