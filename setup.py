from setuptools import setup, find_packages

setup(
    name="py-myaskapi",
    version="1.0.0",
    packages=find_packages(),
    author="Ed Menendez",
    author_email="ed@menendez.com",
    description="Simple interface to the MyAsk API.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/edmenendez/py-myaskapi",
    install_requires=[
        "requests",
    ],
    classifiers=[
        # https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
