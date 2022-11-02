class BaseResponse(object):
    data = None
    success = False
    message = None
    status = None

    def __init__(self, data, exception,code):
        self.data = data
        self.status = code
        # self.message = str(exception) if exception is not None else None
        self.message = 'success' if exception is None else 'error'

    def to_dict(self):
        return {
            'status code': self.status,
            'message': self.message,
            'data': self.data,
        }