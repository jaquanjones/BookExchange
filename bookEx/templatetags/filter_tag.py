from django import template

register = template.Library()


@register.simple_tag
def replace_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)

    if urlencode:
        # split parameters into a list
        querystring = urlencode.split('&')

        # filters string and eliminates the page parameter
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url
