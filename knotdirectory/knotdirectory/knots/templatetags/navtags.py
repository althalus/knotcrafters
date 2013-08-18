from django import template

register = template.Library()


@register.simple_tag
def navactive(request, urls):
    if request.resolver_match.url_name in urls.split():
        return "active"
    return ""
