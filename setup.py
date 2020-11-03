import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='matplotlib-tuda',
    version='0.0.2',
    author='Fabian Damken',
    author_email='fabian.damken@frisp.org',
    description='Small package to add the corporate colors of the TU Darmstadt to Matplotlib.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fdamken/matplotlib-tuda',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.8'
)
