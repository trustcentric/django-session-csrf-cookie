import os
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))


setup(
    name='django-session-csrf-cookie',
    version='0.1',
    description=('Django middleware that works with session-csrf and '
                 'sends a CSRF token cookie.'),
    long_description=open(os.path.join(ROOT, 'README.rst')).read(),
    author='Jody McIntyre',
    author_email='jodym@trustcentric.com',
    url='http://github.com/trustcentric/django-session-csrf-cookie',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django', 'django-session-csrf'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
