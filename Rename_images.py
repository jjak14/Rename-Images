#! /usr/bin/env python

# As I have to rename images located on my computer after every "run",
# I write this script in my learning path with python to automate this.
# The script ask for info about the "survey"
# then uses entered info to build a path, navigate to the folders
# and rename the files

import os, os.path, zipfile
from pathlib import Path

print("Welcome to the rename images script !")


# Get user to enter project number
def project_number():
    while True:
        print("Enter project number (it should be 5 digit long)")
        project = input()
        if project.isnumeric() and len(project) == 5:
            return project
        else:
            continue


# Get user to enter line name
def linename():
    while True:
        print("Enter linename: (i.e: 12LAUREC)")
        line = input().upper()
        if line[:2].isnumeric() and len(line) == 8 and line.isalnum():
            return line
        else:
            continue


# Get user to enter tool technology
def tool_tech():
    while True:
        print("Enter technology: (i.e: CBG, BMG, CDP, AFG, ...)")
        tech = input().upper()
        if tech.isalpha() and len(tech) == 3:
            return tech
        else:
            continue


# function to construct relative path for each of the folder with files to rename
def images_location(project, line, tech):
    images_path = "c:/Proj0/" + project + "/" + line + "/" + tech + "/R1/MRK/Pictures"
    tool_before_path = images_path + "/Tool Before"
    tool_after_path = images_path + "/Tool After"
    launcher_path = images_path + "/Launcher"
    receiver_path = images_path + "/Receiver"
    return images_path, tool_before_path, tool_after_path, launcher_path, receiver_path


# Function to rename the files
# the function takes 4 parameters (project, linename, tool technology and path)
# the file to rename should absolutely not have the target name otherwise the program will return an error
# making this check and circumvent this situation is a work in progress
def rename(project, line, tech, path):

    global n_p, file_ext # this line is not necessary I made these local variables global for testing purposes

    # I use the below lines to extract/build few variable necessary for the proper naming of my file
    last_folder = {"Tool Before": "BR", "Tool After": "AR", "Launcher": "Launcher", "Receiver": "Receiver"}
    folder = path.split("/")
    if folder[-1] in last_folder.keys():
        n_p = last_folder[folder[-1]]

    # I move to the existing directory where I will be naming files
    os.chdir(path)

    # I check that the it is indeed a directory and not a file
    # :) this seems not necessary
    if not os.path.isdir(path):
        return print("{} is not a folder".format(path))
    else:
        i = 0

        # loop through the file in the directory and rename the file
        for file in os.listdir():
            file_name, file_ext = os.path.splitext(file)

            if os.path.isfile(file) and file_ext == ".JPG" and n_p != "Launcher" and n_p != "Receiver":
                os.rename(file, '0-1000-{}-{}-{}-R1-{} ({}){}'.format(project, line, tech, n_p, i, file_ext))
                i += 1

            elif os.path.isfile(file) and file_ext == ".JPG" and n_p == "Launcher" and n_p != "Receiver":
                os.rename(file, '0-1000-{}-{}-{} ({}){}'.format(project, line, n_p, i, file_ext))
                i += 1

            elif os.path.isfile(file) and file_ext == ".JPG" and n_p != "Launcher" and n_p == "Receiver":
                os.rename(file, '0-1000-{}-{}-{} ({}){}'.format(project, line, n_p, i, file_ext))
                i += 1


# Main body of the program call each function to actually perform the required task
(project, line, tech) = project_number(), linename(), tool_tech()
(images_path, tool_before_path, tool_after_path, launcher_path, receiver_path) = images_location(project, line, tech)

rename(project, line, tech, launcher_path)
rename(project, line, tech, receiver_path)
rename(project, line, tech, tool_after_path)
rename(project, line, tech, tool_before_path)
