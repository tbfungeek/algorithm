#!/usr/bin/env python3
#-*-coding:utf-8-*-
import functools

def excute_time(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print("%s result: %s"%(tag,str(result)))
            return result
        return wrapper
    return decorator
