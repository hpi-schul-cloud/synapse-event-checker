from setuptools import setup, find_packages

setup(
    name="synapse-event-checker",
    version="0.0.3",
    packages=find_packages(),
    description="Checks user events to enforce custom rules",
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
)
