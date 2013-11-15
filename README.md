django-webnodes
===============

The goal of `WebNodes` is to create a new way of writing Django templates which is fully compatible with the current Django templating infrastructure. It borned to make it easy to support standard, reusable UI widgets across your application. WebNodes are like special functional calls to render components of your page.

## Usage:

This use as templatetags

```
{% webnode node_name [value1 value2 ... key1=value1 key2=value2 ...] %}
```
- ``value1``: position value passed as ``value1`` in ``get_context()`` and ``render()`` methods
- ``key1=value1``: dictionary key-value pairs passed as ``key1`` in ``get_context()`` and ``render()`` methods

## Demo

For example, if you are implementing a app statistics website, and you want to have app ratings appear on both list page and detail page, you can make an `Ratings` WebNode to render them on both pages.

First, create a Python module for your webnods, e.g., webnodes.py(place it in ``yourapp`` module)

    from django_webnodes import WebNode

    class RatingsNode(WebNode):

    	template = 'webnodes/ratings.html'

        def get_context(self, app_id):
        	...
	        ratings = ...
    	    return {'ratings': ratings}

Calling from template:

    {% load webnode %}

    <p>{% webnode RatingsNode app.id %}</p>
    
## Extension

If you want see this webnode single, add this in your urls' urlpatterns

	url(r'^webnodes/', include('django_webnodes.ext.urls'))
	
Then open `http://127.0.0.1:8000/webnodes/RatingsNode?app_id=414603431` in your browser, you will see it.

# Refs

Inspired by [tornado UI Module](https://github.com/facebook/tornado/blob/master/tornado/web.py), [django custom templatetags](https://docs.djangoproject.com/en/dev/howto/custom-template-tags/).

Based on [django-widgets(1)](https://code.google.com/p/django-widgets) and [django-widgets(2)](https://github.com/marcinn/django-widgets)