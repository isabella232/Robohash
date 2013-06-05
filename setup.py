from setuptools import setup

setup(name="robohash",
      version="0.0.2",
      packages=["robohash"],
      package_data={'robohash': ['blue/*/*', 
                                 'brown/*/*',
                                 'green/*/*',
                                 'grey/*/*',
                                 'orange/*/*',
                                 'pink/*/*',
                                 'purple/*/*',
                                 'red/*/*',
                                 'white/*/*',
                                 'yellow/*/*',
                                 'set2/*/*',
                                 'set3/*/*',
                                 'bg1/*',
                                 'bg2/*',
                                 ]},
      entry_points={
        'console_scripts' :
        '''
        robohash=robohash.webfront:main
        '''
        },
      install_requires=[
        "tornado",
        ],
      )
