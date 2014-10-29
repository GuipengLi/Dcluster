from setuptools import setup

setup(
    name = 'sharepathway',
    packages = ['sharepathway'], # this must be the same as the name above
    version = '0.4.2',
    description = 'A Python package for KEGG pathway enrichment analysis with multiple gene lists',
    author = 'Guipeng Li',
    author_email = 'guipenglee@gmail.com',
    url = 'https://github.com/GuipengLi/sharepathway',   # use the URL to the github repo
    keywords = ['detection', 'pathway', 'enrichment', 'share', 'multiple gene lists'], # arbitrary keywords
    classifiers = [],
    long_description=open('README.rst').read(),
    include_package_data=True,
    install_requires=["numpy >= 1.4.0", "scipy >= 0.9.0"],
)
