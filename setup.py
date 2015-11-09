from setuptools import setup, find_packages

setup(
    name="gopherairtime-cli",
    version="0.0.1",
    url='http://github.com/westerncapelabs/gopherairtime-cli',
    license='BSD',
    description="A command-line interface for Gopher Airtime's HTTP APIs",
    long_description=open('README.rst', 'r').read(),
    author='Western Cape Labs',
    author_email='devops@westerncapelabs.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'click',
    ],
    entry_points="""
        [console_scripts]
        gopherairtime-cli=gopherairtime_cli.main:cli
    """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)
