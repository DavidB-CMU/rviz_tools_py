from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
     packages=[
          'rviz_tools_py',
     ],
     package_dir={'': 'include'},
     install_requires=['numpy']
)
setup(**d)
