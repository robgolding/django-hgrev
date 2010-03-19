from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

HGREV_HG_PATH = getattr(settings, 'HGREV_HG_PATH', None)

if HGREV_HG_PATH is None:
	raise ImproperlyConfigured, "You need to define HGREV_HG_PATH in your settings.py file"
