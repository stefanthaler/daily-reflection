import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='daily-reflection',
     version='0.0.6',
     scripts=['daily-reflection'] ,
     author="Stefan Thaler",
     author_email="bruthaler@gmail.com",
     description="A small command-line tool that helps you conduct your daily morning/evening reflection.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/stefanthaler/maildaily-reflection",
     packages=setuptools.find_packages(),
     install_requires=[
          'tinydb',
          'pyinquirer',
          'pycryptodome',
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
