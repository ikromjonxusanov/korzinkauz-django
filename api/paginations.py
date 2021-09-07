from rest_framework.response import Response
from rest_framework import pagination
class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data, filter_fields = []):
        return Response({
            "code":200,
            "error":False,
            "status":"success",
            "filter_fields":filter_fields,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'current_page_number':self.page.number,
            'total_pages':self.page.paginator.num_pages,
            'item_par_page':len(self.page),
            'results': data
        })
