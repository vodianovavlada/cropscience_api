from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    """
        Custom pagination class that allows clients to control the page size.

        Configuration:
        - page_size: Default number of items per page (10).
        - page_size_query_param: URL parameter to override page size (e.g., ?page_size=20).
        - max_page_size: Maximum limit to prevent server overload (100).
    """

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
