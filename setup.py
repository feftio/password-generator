from setuptools import setup, find_packages

setup(
  name='pwdgenerator',
  version='0.0.1',
  description='This is the package about password generation.',
  url='https://github.com/feftio/pwdgenerator',
  author='Lik Eduard',
  author_email='feft99@gmail.com',
  keywords='password',
  packages=find_packages(),
  install_requires=[
    'pytest',
    'pyinstaller',
    'rich'
  ]
)
