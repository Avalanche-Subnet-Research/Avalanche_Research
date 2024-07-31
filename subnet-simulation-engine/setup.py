from setuptools import setup, find_packages

setup(
    name='subnet-simulation-engine',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'subnet-sim=subnet_simulation_engine.cli:main',
        ],
    },
)
