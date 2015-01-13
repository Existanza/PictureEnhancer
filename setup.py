__author__ = 'Deca'
from cx_Freeze import setup, Executable

setup(
    name='Picture enhancer',
    version="1",
    description="Picture enhancer",
    executables=[Executable("pics.py")],
    )
