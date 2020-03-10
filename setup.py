import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='daily-reflection',
     version='0.0.2',
     scripts=['daily-reflection'] ,
     author="Stefan Thaler",
     author_email="bruthaler [at] gmail.com",
     description="A small command-line tool that helps you conduct your daily morning/evening reflection.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/stefanthaler/protonmaildaily-reflection",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
