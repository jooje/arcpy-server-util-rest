from distutils.core import setup
import os

setup(
    name='arcrest',
    version='10.0',
    description="""Wrapper to the ArcGIS REST API, and a Python analogue to the Javascript APIs""",
    author="ESRI",
    author_email="jscheirer@esri.com",
    packages=['arcrest', 'arcrest.admin'],
    scripts=[
             os.path.join('scripts', 'createservice.py'),
             os.path.join('scripts', 'manageservice.py'),
            ]
)
