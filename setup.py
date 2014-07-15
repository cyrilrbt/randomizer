from setuptools import setup, find_packages


setup(
    name='randomizer',
    version=0.0,
    author='',
    author_email='cyril@hippie.io',
    url='http://67labs.com',
    install_requires=[
        'setuptools',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['randomizer', ],
    entry_points={
        'console_scripts': [
            'randomizer = randomizer.main:run',
        ]},
)