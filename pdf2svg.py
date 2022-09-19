###This code is for converting PDF file to SVG file.
"""A code that converts a PDF file into a SVG file.
Input: The folder where the PDF file is located. A list of all the files in that folder will be inputted into the execute function.
Output: Folder where converted SVG files will be stored. The SVG file will be created in that folder.
Because multiprocessing is used, the speed may vary depending on your CPU configuration."""
##import library for converting ##
from multiprocessing import Process
from multiprocessing import Pool, cpu_count
from os import listdir
import time
import os

## execute function for converting ##
def execute(filelist):
    """needs inkscape installed"""
    """-z is for no gui"""
    """-f is for file"""
    # print(os.getcwd())
    # os.chdir("pdf")
    print(filelist)
    dirs = "directory/"
    pdf_directory = dirs + "pdf/"  # pdf directory
    svg_directory = dirs + "svg/"  # svg directory
    # command = (
    #    "inkscape -z  "
    #    + pdf_directory
    #    + filelist
    #    + " "
    #    + svg_directory
    #    + filelist[:-4]
    #    + ".svg"
    # )
    command = (
        "inkscape --export-filename="
        + svg_directory
        + filelist[:-4]
        + ".svg "
        + pdf_directory
        + filelist
    )

    print(command)
    os.system(command)


# os.chdir("/directory/pdf ")
# directory is the physical directory where the file is located


if __name__ == "__main__":
    """assumes a directory with two folder (pdf and svg) exists in the same folder as this script"""

    print("Start convert ECG data!")

    # os.chdir("directory/")
    # search_directory = "pdf"
    pdf_directory = "directory/pdf"
    filelist = listdir(pdf_directory)
    print(filelist)

    # processor = cpu_count()
    # proc = os.getpid()

    # print("proc_id", proc)
    # print(os.fork())
    # print("Number of processor:", processor)

    print("Number_of_pdf_file :", len(filelist))

    # pool = Pool(processes=cpu_count())

    startTime = int(time.time())
    print(startTime)
    # pool.map(execute, filelist)
    for f in filelist:  # no need for multiprocessing
        execute(f)
    endTime = int(time.time())
    print("Total converting time", (endTime - startTime))
