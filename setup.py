from setuptools import setup

setup(name="robohash",
      version="0.0.2",
      packages=["robohash"],
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
