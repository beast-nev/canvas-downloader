# canvas-downloader
Tool designed to make it easier to download course materials from Canvas (en masse).
Configured originally for WPI's Canvas but can be easily modified for other schools.

# Step by Step guide
1. Clone the repo.
2. Run `pip install -r depend.txt`.
3. Add your API token from before to the .env file key `API_TOKEN`.
4. Run the script with `python main.py` and it will prompt you for each of your courses if you want to download it or not.
5. Once you have selected your courses it will create a directory named `data` and download each courses files to subdirectories named after the course name.

## Output configuration and Notes
1. Edit the variable at the top of the file `ALLOWED_FILE_TYPES` to choose what files you want. Default is `pdf`, `pptx`, and `docx`.
2. Edit the variable at the top of the file `OUTPUT_DIR` to be what you want. Default is `data`.
3. Files with the same name will be *overwritten*.

# Resources that helped me make this
- I followed this guide and used these docs to build this tool
- https://github.com/ucfopen/canvasapi
- https://canvasapi.readthedocs.io/en/stable/
- https://github.com/ubc/getting-started-with-the-canvas-api-with-python
