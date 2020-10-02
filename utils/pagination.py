from rest_framework.pagination import PageNumberPagination


class BeeCashPageNumberPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 1000
    page_size_query_param = "page_size"
    page_query_param = "page"
