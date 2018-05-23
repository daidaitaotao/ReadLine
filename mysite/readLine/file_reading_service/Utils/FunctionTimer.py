import time
from functools import wraps


class FunctionTimer(object):
    """
        class of all function timing util functions
    """
    def fn_timer(function):
        """
            function decorator to track the running time
        """
        @wraps(function)
        def function_timer(*args, **kwargs):
            t0 = time.time()
            result = function(*args, **kwargs)
            t1 = time.time()
            print("Total time running %s: %s seconds" %
                  (function, str(t1 - t0))
                  )
            return result

        return function_timer
