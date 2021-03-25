
from setuptools import setup

setup(
    author='Arseniy Baranov',
    author_email='arseniy.baranov@gmail.com',
    description='Fork of rfc6266 package with python 3.6+ support',
    url='https://github.com/genme/python-rfc6266-parser',
    keywords='rfc6266 parser Content-Disposition http attachments',
    name='rfc6266-parser',
    version='0.1.0',
    license='GNU LGPL',
    platforms='OS-independent',
    py_modules=['rfc6266_parser', 'test_rfc6266_parser'],
    install_requires=[
        'werkzeug==1.0.1'
    ],
    extras_require={
        'dev': [
            'pytest==4.6.11',
            'flake8',
            'pytest-localserver',
            'requests',
            'httplib2'
        ],
    },
    long_description=open('README').read(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Topic :: Internet :: WWW/HTTP',
    ),
)

