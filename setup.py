import os
from setuptools import setup, find_packages
import hgrev

def fullsplit(path, result=None):
	"""
	Split a pathname into components (the opposite of os.path.join) in a
	platform-neutral way.
	"""
	if result is None:
		result = []
	head, tail = os.path.split(path)
	if head == '':
		return [tail] + result
	if head == path:
		return result
	return fullsplit(head, [tail] + result)

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
hgrev_dir = os.path.join(root_dir, 'hgrev')
pieces = fullsplit(root_dir)
if pieces[-1] == '':
    len_root_dir = len(pieces) - 1
else:
    len_root_dir = len(pieces)

for dirpath, dirnames, filenames in os.walk(hgrev_dir):
	# Ignore dirnames that start with '.'
	for i, dirname in enumerate(dirnames):
		if dirname.startswith('.'): del dirnames[i]
	if '__init__.py' in filenames:
		packages.append('.'.join(fullsplit(dirpath)[len_root_dir:]))
	elif filenames:
		data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

setup(
	name = "django-hgrev",
	version = hgrev.VERSION,
	packages = packages,
	data_files = data_files,
	author = "Rob Golding",
	author_email = "rob@robgolding.com",
	description = "A small Django application that adds a templatetag to display the current Mercurial revision.",
	license = "GPL",
	keywords = "python django mercurial hg revision",
	url = "http://bitbucket.org/robgolding63/hgrev",
)
