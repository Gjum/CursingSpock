try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='CursingSpock',
      py_modules=['cursingspock'],
      version='0.1.0',
      description='A SpockBot plugin for controlling the client from the terminal. Built with Curses.',
      author='Gjum',
      author_email='code.gjum@gmail.com',
      url='https://github.com/Gjum/CursingSpock',
      license='MIT',
      # TODO enable when released
      # install_requires=[
      #     'spockbot >= 0.2.0',
      # ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console :: Curses',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Games/Entertainment',
          'Topic :: Home Automation',
          'Topic :: System :: Monitoring',
      ],
)
