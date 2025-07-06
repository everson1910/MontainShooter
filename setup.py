from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name='DeadCemetery',
    version="1.0",
    description="Dead Cemetery app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)