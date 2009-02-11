"""Register a number of non-portable, Jinja2-only filters with a Coffin
library object.
"""

from jinja2 import environmentfilter, contextfilter

@environmentfilter
def environment(environment, value):
    return ""

@contextfilter
def context(context, value):
    return ""

def multiarg(value, arg1, arg2):
    return ""

def jinja_forced(value):
    return ""


from coffin.template import Library
register = Library()
register.filter('environment', environment)
register.filter('context', context)
register.filter('multiarg', multiarg)
register.filter('jinja_forced', jinja_forced, jinja2_only=True)