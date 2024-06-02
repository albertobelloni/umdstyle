from setuptools import setup

setup(
    name='umdstyle',
    version='0.1.0',    
    description='UMD style for ROOT plots',
    url='https://github.com/albertobelloni/umdstyle',
    author='Alberto Belloni',
    author_email='abelloni@umd.edu',
    packages=['umdstyle'],
    install_requires=['ROOT',
                      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
    ],
)

