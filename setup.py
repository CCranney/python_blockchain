import setuptools


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()

setuptools.setup(
    name="python-blockchain",
    version="0.0.1",
    author="Caleb Cranney",
    author_email="caleb.cranney.app@gmail.com",
    description="Trial Blockchain Package",
    long_description=readfile('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/CCranney/python_blockchain",
    classifiers=[
        'Intended Audience :: Science/Research',
        "Programming Language :: Python :: 3",
    ],
    py_modules=['backend','backend.blockchain','backend.util', 'backend.app'],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    #license=readfile('LICENSE'),
    #entry_points={
    #    'console_scripts': [
    #        'csodiaq = csodiaq:main'
    #    ]
        #gui_scripts?
    #},
    install_requires=[
        'pytest==5.1.2',
        'flask==1.1.1',
        'pubnub==4.1.6',
        'requests==2.22.0',
    ],
)
