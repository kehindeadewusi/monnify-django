#supporting only requests to get this off the ground, but thinking of non-requests clients already.

import sys
import threading
import textwrap
from monnify import error

http_client_impl = None

def new_http_client(*args, **kwargs):
    return http_client_impl(*args, **kwargs)


class HttpClient(object):
    def __init__(self):
        self._thread_local = threading.local()
    
    def request(self, method, url, headers, post_data=None):
        raise NotImplementedError(
            "Should be implemented in subclasses"
        )
    
    def close(self):
        raise NotImplementedError(
            "Should be implemented in subclasses"
        )


class RequestsClient(HttpClient):
    name = "requests"

    def __init__(self, timeout=60, session=None, **kwargs) -> None:
        super(RequestsClient, self).__init__(kwargs)
        self._timeout = timeout
        self._session = session
    
    def request(self, method, url, headers, post_data=None):
        kwargs = {}

        if self._proxy:
            kwargs["proxies"] = self._proxy

        if getattr(self._thread_local, "session", None) is None:
            self._thread_local.session = self._session or requests.Session()

        try:
            try:
                result = self._thread_local.session.request(
                    method,
                    url,
                    headers=headers,
                    data=post_data,
                    timeout=self._timeout,
                    **kwargs
                )
            except TypeError as e:
                raise TypeError(
                    "Warning: It looks like your installed version of the "
                    '"requests" library is imcompatible '
                    "(HINT: The most likely cause is that "
                    'your "requests" library is out of date. You can fix '
                    'that by running "pip install -U requests".) The '
                    "underlying error was: %s" % (e,)
                )

            # This causes the content to actually be read, which could cause
            # e.g. a socket timeout. TODO: The other fetch methods probably
            # are susceptible to the same and should be updated.
            content = result.content
            status_code = result.status_code
        except Exception as e:
            # Would catch just requests.exceptions.RequestException, but can
            # also raise ValueError, RuntimeError, etc.
            self._handle_request_error(e)
        return content, status_code, result.headers

    def _handle_request_error(self, e):

        # Catch SSL error first as it belongs to ConnectionError,
        # but we don't want to retry
        if isinstance(
            e,
            (requests.exceptions.Timeout, requests.exceptions.ConnectionError),
        ):
            msg = (
                "Error communicating with Monnify.  "
                "If this problem persists, contact Monnify."
            )
            err = "%s: %s" % (type(e).__name__, str(e))
            should_retry = True
        # Catch remaining request exceptions
        elif isinstance(e, requests.exceptions.RequestException):
            msg = (
                "Error communicating with Monnify.  "
                "If this problem persists, contact Monnify."
            )
            err = "%s: %s" % (type(e).__name__, str(e))
            should_retry = False
        else:
            msg = (
                "Error communicating with Monnify. "
                "This could be a configuration error"
            )
            err = "A %s was raised" % (type(e).__name__,)
            if str(e):
                err += " with error message %s" % (str(e),)
            else:
                err += " with no error message"
            should_retry = False

        msg = textwrap.fill(msg) + "\n\n(Network error: %s)" % (err,)
        raise error.APIConnectionError(msg, should_retry=should_retry)
    
    def close(self):
        if getattr(self._thread_local, "session", None) is not None:
            self._thread_local.session.close()


try:
    import requests
    http_client_impl = RequestsClient
except ImportError:
    raise
