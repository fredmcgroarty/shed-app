from setuptools import find_packages, setup

setup(
    name='shed_app',
    version='1.0.1',
    packages=find_packages('pifacerelayplus', 'pifacecommon', 'flask-cors'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 'pifacerelayplus', 'pifacecommon', 'flask-cors', 'requests'
    ],
)
