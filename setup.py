import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="cx_freeze_test",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": build_options},
    executables=[Executable("./cx_freeze_test/main.py", base=base)],
)
