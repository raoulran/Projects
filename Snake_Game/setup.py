from cx_Freeze import setup, Executable

base = None

executables = [Executable("Python.py", base=base)]

packages = ["idna"]
include_files = [
    r"C:\Users\kamin_t7sflus\Desktop\New folder",
    r"C:\Users\kamin_t7sflus\Desktop\New folder"
]


options = {
    'build_exe': {
        'packages': packages,
        'include_files': include_files,
    },
}

setup(
    name="Python",
    options=options,
    version="1.0.0",  # Replace with your actual version number
    description='Try to get the highest score',
    executables=executables
)
