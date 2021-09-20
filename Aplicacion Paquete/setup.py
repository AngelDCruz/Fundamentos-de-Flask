from setuptools import setup

setup(
    name='Aplicacion',
    packages=['Aplicacion'],
    include_package_data=True,
    install_requires=[
        'flask',
        'SQLAlchemy',
        'BrokenPackage'
    ],
)