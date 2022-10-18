import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__version_info__ = (1, 3)
__version__ = '.'.join([str(v) for v in __version_info__])

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='regal',
    version=__version__,
    packages=['regal'],
    include_package_data=True,
    license='MIT License',
    description='A/B Testing or publish smart grouping engine.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/boylegu/regal',
    author='BoyleGu',
    author_email='gubaoer@hotmail.com',
    install_requires=['six==1.11.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
)
