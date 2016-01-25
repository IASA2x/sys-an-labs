import sys, matplotlib
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

includefiles = ['lab_4/', ( matplotlib.get_data_path(),"mpl-data")] # include any files here that you wish
includes = ['sip', 'sys','PyQt5.QtCore','PyQt5.QtGui','PyQt5.QtWidgets',
            'matplotlib','matplotlib.figure','matplotlib.backends.backend_qt5agg',
            'PyQt5.uic',
            'matplotlib.figure']
excludes = []
packages = ["os", 'tabulate','pandas']

exe  = Executable(
       script = "main.py", # the name of your main python script goes here
       initScript = None,
       base = None,
       #base = 'Win32GUI' if sys.platform=='win32' else None,# if creating a GUI instead of a console app, type "Win32GUI"
       targetName = "lab4.exe", # this is the name of the executable file
       copyDependentFiles = False,
       compress = True,
       appendScriptToExe = True,
       appendScriptToLibrary = True,
       icon = None # if you want to use an icon file, specify the file name here
)

setup(
    name = "lab4_exe", # program name
    version = "1.2",
    description = 'app',
    author = "Fatenko",
    author_email = "",
    options = {"build_exe": {"excludes":excludes,
                             "packages":packages,
                             "include_files":includefiles,
                             'includes':includes}},
    executables = [exe]
)


