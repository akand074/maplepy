from setuptools import find_packages, setup

VERSION = '0.0.1dev0'

REQUIREMENTS = [
    'requests>=2.5'
]

TEST_REQUIREMENTS = [

]

setup(
    name="maplepy",
    version=VERSION,

    description="Client code generator for GraphQL APIs based on introspection queries and schema files",
    long_description=open('README.md'),

    author='Andrew Kandalaft',
    author_email='andrew.kandalaft@gmail.com',

    license='MIT',

    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    keywords='api graphql generator sdk',

    packages=find_packages(exclude=['tests']),

    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS
)
