from setuptools import setup

setup(
    name = 'Dcluster',
    packages = ['Dcluster'], # this must be the same as the name above
    version = '0.4.0',
    description = 'A Python package for Clustering by fast search and find of density peaks',
    author = 'Guipeng Li',
    author_email = 'guipenglee@gmail.com',
    url = 'https://github.com/GuipengLi/Dcluster',   # use the URL to the github repo
    keywords = ['Cluster', 'fast', 'density'], # arbitrary keywords
    classifiers = [],
    long_description=open('README.rst').read(),
    include_package_data=True,
    install_requires=["numpy >= 1.2.0", "matplotlib >= 1.3.0"],
)
