from cx_Freeze import setup, Executable

setup(
    name="Tapetka",
    version="1.0",
    description="Tapeta z pliku MP4 lub GIF",
    executables=[Executable("main.py")]
)