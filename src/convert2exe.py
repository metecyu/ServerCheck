
from distutils.core import setup
import py2exe

# setup(windows=["app1.py"])  


setup(  
    name = 'song',  
    description = 'software',  
    version = '0.0.1',  
    zipfile = None,  
    author = "metecyu",
    author_email = "metecyu@gmail.com",
    #console = [  
     #   'con.py'  
    #],  
    windows = [  
        {  
            'script':'main.py',
            'icon_resources':[(0,'resource/images/sc.ico')],
        }  
    ],
    data_files=[  
        ('resource/images',[  
            'resource/images/red.jpg',
            'resource/images/green.jpg',
            'resource/images/360.ico',
            'resource/images/sc.ico',
        ]),  
        ('resource',[  
            'resource/checkItem.xml',
            'resource/checkItem_oa.xml',
            
        ]),  
    ]  
) 
