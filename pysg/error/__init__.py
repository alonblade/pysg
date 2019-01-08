"""Define all exceptions that occur in pysg.
"""


class Error(Exception):
    """Base class for exceptions."""
    pass


class CameraParameterError(Error):
    """Exception raised for invalid camera parameter."""

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg