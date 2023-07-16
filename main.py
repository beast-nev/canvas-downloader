import os
import canvasapi
import dotenv
from time import sleep
from reactpy import component, html, run

dotenv.load_dotenv(dotenv.find_dotenv())

# TOKEN is in the .env file. If you don't publish any of this anywhere then you don't need .env file and can just write
# in the TOKEN and USER_ID here.
TOKEN = os.environ.get('API_TOKEN')
BASEURL = 'https://wpi.instructure.com'  # WPI canvas API endpoint

class API:
    def __init__(self, api: canvasapi.Canvas) -> None:
        self.user_id = api.get_current_user()
        self.user = api.get_user(self.user_id)
        self.courses = api.get_courses()
        self.removing_courses = []
        self.courses_to_download = []
    def print_course_names(self):
        """_summary_
        Print all of the courses withing the `courses` object above
        """
        for course in self.courses:
            try:
                print(course.name)
            except:
                print('Could not print course name')

    def get_courses_to_download(self):
        """_summary_
        Get all of the courses to download by only adding the ones not specified in the `removing_courses` list
        """
        for course in self.courses:
            try:
                if course.name not in self.removing_courses:
                    self.courses_to_download.append(course)
            except:
                print('Could not add course to list')

    def get_course_files(self):
        """_summary_
        Download all of the courses into the 'data' directory
        """
        course_bad_counter = 0  # some courses are odd and did not work properly, this will tell you how many you had. I had 5
        for course in self.courses_to_download:
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


@component
def App():
    return html.h1(
        "Hi there!"
    )
run(App)


if __name__ == '__main__':
    """_summary_
    Follow the GitHub step-by-step before uncommenting these functions below
    """
    # initialize canvas api with the WPI endpoint and your account token
    canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

    api = API(canvas_api)

    # the line below will show you all of your course names
    run(App)

    # uncomment the line below to add all of your desired courses to the `courses_to_download` list
    # get_courses_to_download()

    # uncomment the following line to begin downloading courses
    # get_course_files()
