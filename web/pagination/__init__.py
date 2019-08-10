from rest_framework.pagination import PageNumberPagination



class DefaultPagination(PageNumberPagination):
    page_size = 8#一页多少条
    page_query_param = 'page' #分页查询条件的key
    page_size_query_param = 'size' #每页显示多少条  如果url加了 则不用默认page_size
    # max_page_size = 8