from distutils.core import setup

setup(
    name='django_webnodes',
    version='0.0.1',
    author='iamsk',
    author_email='iamsk.info@gmail.com',
    packages=['django_webnodes', 'django_webnodes.templatetags',
              'django_webnodes.ext'],
    url='https://github.com/bin-zhang/django_webnodes',
    description='',
    long_description=open('README.md').read(),
    install_requires=[
        "django >= 1.3.7",
    ]
)
