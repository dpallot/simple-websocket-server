from distutils.core import setup

setup(
    name='SimpleWebSocketServer',
    version='0.1.1',
    author='Dave Pallot',
    author_email='d.e.pallot@gmail.com',
    packages=['SimpleWebSocketServer'],
    url='https://github.com/dpallot/simple-websocket-server/',
    description='A Simple Websocket Server written in Python',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
