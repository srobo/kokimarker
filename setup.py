#!/usr/bin/env python
from distutils.core import setup

setup( name = "kokimarker",
       version = "0.0.1",
       py_modules = [ "kokimarker" ],
       packages = ["kokimarker"],
       scripts = [ "koki-marker-gen" ],

       install_requires = [ "numpy", "pycairo" ],

       maintainer = "Student Robotics",
       maintainer_email = "kit-team@studentrobotics.org",
       url = "https://github.com/srobo/kokimarker",
       )
