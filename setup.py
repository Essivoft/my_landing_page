# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ckanext-my_landing_page',
    version='0.0.1',
    description='A CKAN landing page extension',
    long_description=long_description,
    url='https://github.com/yourusername/ckanext-my_landing_page',
    author='Your Name',
    author_email='your.email@example.com',
    license='AGPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='CKAN extension landing page',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['ckanext'],
    install_requires=[
        # CKAN extensions should not list dependencies here, but in a separate
        # ``requirements.txt`` file.
    ],
    include_package_data=True,
    package_data={
        # Hvis du har statiske filer som CSS, legg dem til her.
        '': ['public/*'],
    },
    data_files=[],
    entry_points='''
        [ckan.plugins]
        my_landing_page=ckanext.my_landing_page.plugin:MyLandingPagePlugin

        [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    ''',
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
