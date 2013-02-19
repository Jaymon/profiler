# std modules
import time
import os
import inspect
import copy
import unittest

# first party
import profiler

class ProfilerTest(unittest.TestCase):
    """
    tests the profiler just to make sure it does what it's supposed to
    since -- 4-6-12
    author -- Jay
    """
    
    def testProfiler(self):
        '''makes sure the profiler can be started and stopped and has the right value'''
        
        profiler.start("my name")
        time.sleep(1)
        d = profiler.stop()
        
        self.assertGreaterEqual(d.elapsed,1.00)
        self.assertEqual(d.name,"my name")
        self.assertEqual(d.name,"my name")
        
    def testGeneratedName(self):
        '''makes sure a suitable name is generated if no specific name is passed into start()'''
        
        profiler.start()
        d = profiler.stop()
        self.assertEqual(d.name,self.id().rpartition('.')[-1])

    def testStopException(self):
        '''an exception should be raised if stop() is called before start()'''
        
        with self.assertRaises(LookupError):
            profiler.stop()

if __name__ == '__main__':
    unittest.main()
