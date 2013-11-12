
from distutils.core import setup
import py2exe

# setup(windows=["app1.py"])  


setup(  
    name = 'song',  
    description = 'software',  
    version = '0.0.1',  
    zipfile = None,  
    #console = [  
     #   'con.py'  
    #],  
    windows = [  
        {  
            'script':'app1.py',
            'icon_resources':[(1,'resource/images/360.ico')],
        }  
    ],    
    data_files=[  
        ('resource/images',[  
            'resource/images/red.jpg','resource/images/green.jpg']),  
        ('resource',[  
            'resource/checkItem.xml']),  
    ]  
) 
