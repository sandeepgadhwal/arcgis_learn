
from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
    long_description = fh.read()

dependencies = []

kwargs = {
    "name": 'arcgis_learn',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    "version": '0.1',

    "description": 'ArcGIS API for Python',
    "long_description": long_description,
    "long_description_content_type": "text/markdown",

    # The project's main homepage.
    "url": 'https://developers.arcgis.com/python/',

    # What does your project relate to?
    "keywords":'gis arcgis geographic spatial spatial-data '\
             'spatial-data-analysis spatial-analysis data-science maps '\
             'mapping web-mapping python native-development',

    "classifiers":[
        'Development Status :: 3 - Alpha',

        # Topics
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',

        # Frameworks
        'Framework :: IPython',
        'Framework :: Jupyter',

        # OS
        'Operating System :: OS Independent',

        # Pick your license as you wish (should match "license" above)
        'License :: Other/Proprietary License',


        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    "packages": find_packages(),
    "include_package_data": True,

    "install_requires": dependencies,
    "setup_requires": dependencies,

    "python_requires":'>:3.4',
}

setup(**kwargs)
