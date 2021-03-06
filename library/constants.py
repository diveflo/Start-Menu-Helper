"""Constants used in the whole project."""
import pathlib
import os
import sys

PROGRAM_NAME = "Start Menu Helper"
VERSION_NUMBER = "1.0.3"
ICON_FILE_NAME = "icon.ico"
TIME_BETWEEN_SCANS_IN_MINUTES = 5
APP_DATA_PATH = pathlib.Path.home().joinpath("AppData")
CONFIGURATION_PATH = pathlib.Path(os.sys.path[0]).parent.joinpath("configurations").joinpath("start-menu-helper")
CONFIGURATION_FILE_PATH = CONFIGURATION_PATH.joinpath("config.ini")
LOG_FILE_PATH = CONFIGURATION_PATH.joinpath("log.txt")
STARTUP_PATH = pathlib.Path.home().drive + \
               "\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
EXECUTABLE_PATH = pathlib.Path.cwd().joinpath(PROGRAM_NAME + ".exe")
START_MENU_PATHS = [
    pathlib.WindowsPath(pathlib.Path.home().drive + "/ProgramData/Microsoft/Windows/Start Menu"),
    APP_DATA_PATH.joinpath("Roaming/Microsoft/Windows/Start Menu")
]
START_MENU_PROGRAMS_PATHS = [
    pathlib.WindowsPath(
        pathlib.Path.home().drive + "/ProgramData/Microsoft/Windows/Start Menu/Programs"),
    APP_DATA_PATH.joinpath("Roaming/Microsoft/Windows/Start Menu/Programs")
]
PROTECTED_FOLDERS = [
    "StartUp",
    "Startup",
    "Administrative Tools"
]
FLATTEN_FOLDERS_EXCEPTIONS_PATH = CONFIGURATION_PATH.joinpath("flatten_folders_exceptions.txt")
DELETE_FILES_WITH_NAMES_CONTAINING_LIST_PATH = CONFIGURATION_PATH.joinpath(
    "delete_files_with_names_containing.txt"
)
DELETE_FILES_MATCHING_FILE_TYPES_LIST_PATH = CONFIGURATION_PATH.joinpath(
    "delete_based_on_file_type_list.txt"
)
