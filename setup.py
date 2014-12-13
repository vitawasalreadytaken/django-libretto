from setuptools import setup

setup(
	name = 'django-libretto',
	version = '0.1.0',
	author = 'Vita Smid',
	author_email = 'me@ze.phyr.us',
	packages = ['django_libretto', 'django_libretto.templatetags',],
	url = 'https://github.com/ze-phyr-us/django-libretto',
	license = 'LICENSE',
	description = 'Symlink packages from your virtualenv so that GAE can find and deploy them.'
)
