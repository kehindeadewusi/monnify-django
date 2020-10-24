import monnify

class MonnifyError(Exception):
    def __init__(
        self,
        message = None,
        http_body = None,
        http_status = None,
        json_body = None,
        headers = None,
        code = None
    ):
        super(MonnifyError, self).__init__(self)
        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}
        self.code = code
        #self.request_id = self.headers.get("request-id", None)
        self.error = self.construct_error_object()

    def __str__(self) -> str:
        return self._message or "<empty message>"
    
    @property
    def user_message(self):
        return self._message
    
    def __repr__(self):
        return "%s(message=%r, http_status=%r, request_id=%r)" % (
            self.__class__.__name__,
            self._message,
            self.http_status,
            'N/A',
        )

    def construct_error_object(self):
        return ""


class APIError(MonnifyError):
    pass


class APIConnectionError(MonnifyError):
    def __init__(
        self,
        message,
        http_body=None,
        http_status=None,
        json_body=None,
        headers=None,
        code=None,
        should_retry=False,
    ):
        super(APIConnectionError, self).__init__(
            message, http_body, http_status, json_body, headers, code
        )
        self.should_retry = should_retry

class IdempotencyError(MonnifyError):
    pass

