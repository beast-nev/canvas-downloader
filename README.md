# canvas-downloader
Tool to download all course files from Canvas

# Step by Step guide
1. Go to Canvas to get your API token - `Account` -> `Settings` -> `Approved Integrations:` -> `New Access Token`. Generate one and **COPY IT DOWN**, once you generate it you cannot access it again, i.e you will need to repeat this step.
2. You then need to take this token and then in a command prompt type `curl https://canvas.wpi.edu/api/v1/users/self -H "Authorization: Bearer <your-token-here>"`. Within the response of this you will see your `id` which is your personal user id, save this for later as well.
3. Clone the repo.
4. Run `npm i -r depend.txt` within the directory of `canvas-downloader`
5. Create a `.env` file and add in your API TOKEN to a field called `API_TOKEN` within the `.env` (you will make it) **OR** if you keep this all local within the `main.py` file you can just replace `TOKEN = os.environ.get('API_TOKEN')` with `TOKEN = <your-api-token>`.
6. Do the same steps in #5 for `USER_ID`
7. Next I recommend running the `print_course_names()` function by uncommenting out the line and seeing all of your courses
8. Next go through and add to the `removing_courses` list the names of any course you don't want to download material for
9. Once you add to the `removing_courses` list you can run the `get_courses_to_download()` function and that will add to the list `courses_to_download` list
10. Create a directory within your project called `data`, add one file like `example.txt` to it
11. Run `get_course_files()` to get all of your course files

# Warnings
- I was lazy and did not account for file types **AT ALL**, meaning this will download videos, images, pdfs, pptx...every file type. This can make a 10mb folder -> many GB after downloading all of the material so make sure you have disk space
- Another issue with this and my laziness is that I just make every file a pdf - which will have for example `.mov` files be `.pdf` while is obviously wrong so you will need to manually change all of them to the correct file type. This was not really an issue for me as most of my files were `.pdf`

# Resources that helped me make this
- I followed this guide and used these docs to build this tool
- https://github.com/ucfopen/canvasapi
- https://canvasapi.readthedocs.io/en/stable/
- https://github.com/ubc/getting-started-with-the-canvas-api-with-python
