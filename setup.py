from setuptools import setup

def read_description():
    with open("README.md") as f:
        desc = f.read()
    return desc

setup(
    name = "extraexceptionsreloaded",
    version = "0.0.0.1",
    
    description = "Extra (may be unuseful) Exceptions",
    long_description = open("README.md").read(),
    long_description_content_type="text/markdown",
    
    author = "Alt-Ger",
    author_email = "youriy727@gmail.com",
    
    url = "https://github.com/Alt-Gerutro/extra_exceptions_reloaded/",
    
    packages = ["extraexceptionsreloaded"],
    include_package_data=True,
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    keywords = "extra exception reloaded extraexceptions extra_exception",
    
    python_requires=">=3.6",
    license = "MIT",
    platforms = ["any"],
    
    provides = ["extraexceptionreloaded"])
