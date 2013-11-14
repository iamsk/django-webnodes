django-webnodes
===============

The goal of this project is to create a new way of writing Django templates which is fully compatible with the current Django templating infrastructure.

This use as templatetags

## Usage:

```
{% webnode webnode_name [value1 value2 key1=value1 key2=value2, ...] %}
```
- ``value1``: position value passed as ``value1`` in ``get_context()`` and ``render()`` methods
- ``key1=value1``: dictionary key-value pairs passed as ``key1`` in ``get_context()`` and ``render()`` methods

## Demo

Simplest "hello world" component example (place it in ``yourapp/webnodes`` module):

    from django_webnodes import WebNode
    
    class HelloWorld(WebNode):
        def render(self, context):
            return u'Hello world!'

Calling from template:

    {% load webnode %}

    <h1>{% webnode HelloWorld %}</h1>

# Refs
Based on [django-widgets(1)](https://code.google.com/p/django-widgets) and [django-widgets(2)](https://github.com/marcinn/django-widgets)
