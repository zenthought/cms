from rest_framework.pagination import PageNumberPagination



class DefaultPagination(PageNumberPagination):
    page_size = 8#一页多少条
    page_query_param = 'page' #分页查询条件的key
    page_size_query_param = 'size'
    # max_page_size = 8