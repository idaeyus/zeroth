from cx_Freeze import setup, Executable


files = ['logo.png', 'zeroth.html']


setup(
    name="zerothIDE",
    version="0.1",
    description="Code editor",
    executables=[Executable("zeroth.py")],
    options={
        'build_exe': {
            'include_files': files
        }
    }
)
