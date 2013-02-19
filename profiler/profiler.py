"""
basic hooks to quickly profile blocks of code

since -- 4-6-12
author -- Jay
"""

import time
import inspect

# the started profiling jobs are held in this stack
_stack = []

class Profile(dict):
    """
    this is the profiler results object that is returned from the stop() function
    
    link -- http://stackoverflow.com/questions/224026/
    
    attributes:
        start -- the start time
        stop -- the stop time
        elapsed -- how much time elapsed between start and stop time
        summary -- a pretty print version of the information
        total -- the elapsed time in a readable format (eg, "0.2 ms")
    """
    __getattr__= dict.__getitem__
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__
    
    def __str__(self):
        return self.summary

def start(name=""):
    '''
    start a profiling session with the given name
    
    name -- what you want to name the profiling session
    '''
    d = Profile()
    d.start = time.time()
    d.name = name
    _stack.append(d)
    
def stop(name=""):
    '''
    stop a profiling session
    
    name -- what you want to name the profiling session, defaults to name of calling frame
    
    return -- Profile
    '''
    # canary
    if len(_stack) <= 0:
        raise LookupError("There are no currently active profiler sessions")
    
    d = _stack.pop()
    d.stop = time.time()
    d.elapsed = get_elapsed(d.start, d.stop, 1000.00, 1)
    d.total = "%0.1f ms" % (d.elapsed)
    
    # set the name
    if name:
        d.name = name
    
    if not d.name:
        # http://stackoverflow.com/questions/2654113/
        d.name = inspect.stack()[1][3]
    
    d.summary = "[PROFILING] %s - %s" % (d.total,d.name)
    
    return d

def get_elapsed(start, stop, multiplier=1000.00, rnd=2):
    '''
    get the elapsed time from a start and stop timestamp
    
    since -- 6-28-12
    
    start -- float -- the start timestamp
    stop -- float -- the stop timestamp
    multiplier -- integer|float -- 1000 for ms, 1 for sec
    rnd -- integer -- how many digits to round the elapsed value to, 2 gives NNN.NN
    
    return -- float -- the elapsed time
    '''
    
    val = abs(stop - start) * float(multiplier)
    if rnd > 0:
        val = round(val, rnd)
    
    return val
