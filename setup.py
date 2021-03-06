from setuptools import setup, find_packages

setup(
    name='fizzbuzz',
    version="0.0.3",
    description='Fizz Buzz program.',
    author='sotetsuk',
    url='https://github.com/sotetsuk/python-dev-tutorial',
    author_email='koyamada-s@sys.i.kyoto-u.ac.jp',
    license='MIT',
    install_requires=["pytest", "click", "mypy"],
    packages=find_packages(exclude=["tests"]),
    entry_points={
        'console_scripts': 'fizzbuzz-cli = fizzbuzz.fizzbuzz:main'
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License"
    ]
)
