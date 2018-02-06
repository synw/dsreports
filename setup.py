from setuptools import setup, find_packages


version = __import__('dsreports').__version__

setup(
    name='dsreports',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='Create static reports for Dataswim with Hugo',
    author='synw',
    author_email='synwe@yahoo.com',
    url='https://github.com/synw/django-dsreports',
    download_url='https://github.com/synw/django-dsreports/releases/tag/' + version,
    keywords=['reporting'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False
)
