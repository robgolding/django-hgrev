"""
Creates a template tag called {% hgrev %} that returns the current hg revision
in the following format:

	r23:fe07

"""

from django import template
from hgrev.templatetags import REVISION

register = template.Library()

@register.simple_tag
def hgrev():
    """
    Output the revision:

    	{% hgrev %}
    
    """
    return REVISION
