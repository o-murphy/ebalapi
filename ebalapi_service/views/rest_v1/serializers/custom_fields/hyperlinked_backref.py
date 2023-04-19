from django.utils.http import urlencode
from rest_framework import serializers


class HyperlinkedBackRefField(serializers.HyperlinkedRelatedField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {}
        query_kwargs = {self.lookup_field: obj}
        url = self.reverse(view_name,
                           kwargs=url_kwargs,
                           request=request,
                           format=format)
        if obj is not None:
            return f'{url}?{urlencode(query_kwargs)}'
        return
