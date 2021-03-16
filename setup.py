from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name='biketrauma_jll',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='http://github.com/jsakher/packaging_tutorial.git',
  author='Jalal Sakher',
  author_email='jalal.sakher@etu.umontpellier.fr',
  license='MIT',
  packages=['biketrauma','biketrauma.io', 'biketrauma.preprocess', 'biketrauma.vis'],
  zip_safe=False
)