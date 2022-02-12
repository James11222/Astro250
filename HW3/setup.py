"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup

setup(
    name='calcalc_js',  # Required
    version='0.9.0',  # Required
    description='A package that serves as an all purpose calculator.',  # Optional
    long_description=('README.md').read_text(encoding='utf-8'),  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/James11222/Astro250/tree/main/HW3',  # Optional

    author='James Sunseri',  # Optional

    author_email='jamessunseri@berkeley.edu',  # Optional

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only'],
    keywords='calculator, simple, berkeley, cal, js',  # Optional
    packages=['calcalc'],
    platforms=['any'],
    license="MIT",
    python_requires='>=3.6, <4',
    setup_requires=['pytest-runner'],
    install_requires=['requests'],  # Optional
    tests_require=['pytest'],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/James11222/Astro250/issues',
        'Funding': 'https://donate.pypi.org',
        'Check out my Website!': 'http://www.jamessunseri.com',
        'Source': 'https://github.com/James11222/Astro250/tree/main/HW3/calcalc/',
    }
)




