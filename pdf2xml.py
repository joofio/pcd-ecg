###This code is for converting PDF to XML
"""A code that converts a PDF file into an XML file.
Input: The folder where the PDF file is located. A list of all the files in that folder will be inputted into the execute function.
Output: Folder where converted XML files will be stored. The XML file will be created in that folder.
Because multiprocessing is used, the speed may vary depending on your CPU configuration."""
##import library for converting ##
from multiprocessing import Process
from multiprocessing import Pool, cpu_count
from os import listdir
import time
import os

## execute function for converting ##
def execute(filelist):
    os.chdir("/Users/joaoalmeida/Desktop/pcd-ecg/directory/pdf")
    command = (
        "pdftohtml -xml /Users/joaoalmeida/Desktop/pcd-ecg/directory/pdf/"
        + filelist
        + " /Users/joaoalmeida/Desktop/pcd-ecg/directory/xml/"
        + filelist
        + ".xml"
    )
    os.system(command)
    os.chdir("/Users/joaoalmeida/Desktop/pcd-ecg/directory/pdf")
    # directory is the physical directory where the file is located


if __name__ == "__main__":
    print("Start convert ECG data!")

    os.chdir("directory/")
    search_directory = "pdf"
    filelist = listdir(search_directory)
    print(filelist)
    processor = cpu_count()
    proc = os.getpid()

    print("proc_id", proc)
    print(os.fork())
    print("Number of processor:", processor)

    print("Number_of_pdf_file :", len(filelist))

    # pool = Pool(processes=cpu_count())

    startTime = int(time.time())
    print(startTime)
    # pool.map(execute, filelist)
    for f in filelist:
        execute(f)
    endTime = int(time.time())
    print("Total converting time", (endTime - startTime))
