
# def setup():
#     """
#
#     """
#
#     print("UM-40 SMART Framework")

import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="JSON_Backend_Framework",
    version="0.2",
    author="Buslin Nicolay",
    author_email="n.Buslin@allmonitoring.ru",
    description="Package to eaZZZy work with JSON_Backend_framework.",
    # long_description=long_description, <<---README.md
    packages=setuptools.find_packages(),

    install_requires=[
        'requests==2.25.1',
    ]
)
