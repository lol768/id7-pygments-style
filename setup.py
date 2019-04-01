""" 
An ID7 style for Pygments
""" 
from setuptools import setup 

setup( 
    name         = 'id7', 
    version      = '1.1', 
    description  = __doc__, 
    author       = "Adam Williams, Pieter Belmans", 
    install_requires = ['pygments'],
    packages     = ['id7'], 
    entry_points = '''
    [pygments.styles]
    id7 = id7:IDSevenStyle
    '''
) 
