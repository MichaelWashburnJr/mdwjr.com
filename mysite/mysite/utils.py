from django.shortcuts import _get_queryset

def get_object_or_none(Class, *args, **kwargs):
    """
    Get the object being queried for or return None if no object exists.
    Source: http://stackoverflow.com/questions/2489311/django-objects-get
    """
    queryset = _get_queryset(Class)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None