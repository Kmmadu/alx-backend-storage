#!/usr/bin/env python3
"""Main file"""
from cache import Cache, replay

cache = Cache()

# Store some values
s1 = cache.store("first")
s2 = cache.store("second")
s3 = cache.store("third")

# Get values
print(cache.get(s1))  # Output: b'first'
print(cache.get_str(s2))  # Output: 'second'
print(cache.get_int(s3))  # Will raise an error if s3 is not an int

# Replay history
replay(cache.store)

