from rest_framework.response import Response as DRFResponse
from rest_framework import status


class Response(DRFResponse):
    """统一API响应格式"""
    
    def __init__(self, data=None, status_code=None, content_type=None, message='success', **kwargs):
        """
        统一响应格式
        :param data: 实际返回的数据
        :param status_code: HTTP状态码
        :param message: 响应消息
        """
        if status_code is None:
            status_code = status.HTTP_200_OK
            
        formatted_data = {
            'code': status_code,
            'message': message,
            'data': data
        }
        super().__init__(data=formatted_data, status=status_code, content_type=content_type, **kwargs)