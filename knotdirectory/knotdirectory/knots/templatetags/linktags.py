from django import template
from urllib2 import urlparse
import re

register = template.Library()

def format_link(link):
    url_parts = urlparse.urlparse(link.link)
    if re.match(r'(www\.)?facebook\.com', url_parts[1]):
        return '<div class="fb-post" data-href="%s"></div>' % link.link
    elif re.match(r'(www\.)?youtu(\.be|be\.com)', url_parts[1]):
        qs = urlparse.parse_qs(url_parts[4])
        v = qs.get('v', ['', ])[0]
        return '<iframe title="YouTube video player" width="480" height="390" src="http://www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>' % v
    else:
        return '<a href="%s">%s</a>' % (link.link, link.name)

register.simple_tag(format_link)
