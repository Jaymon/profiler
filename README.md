# Profiler

A simple module to profile code blocks in Python

This just wraps the time function to allow you to start and stop profiling blocks so you can
quickly see how long something takes to run.


    import profiler

    profiler.start("my title")

    for x in xrange(5):
       # do something crazy

    p = profiler.stop()
    print p # [PROFILE] x.xx ms - my title"

You can also profile sub blocks

    import profiler

    profiler.start("foo")

    for i in xrange(5):
        profiler.start("bar")
        for j in xrange(5):
            # do more stuff

    print profiler.stop() # print info for bar
    print profiler.stop() # print info for foo

## Install

Use PIP

    pip install git+https://github.com/Jaymon/profiler#egg=profiler

## License

MIT I guess, use this code any way you want, if you extend it I'd love a pull request
so I can merge any new stuff in.

