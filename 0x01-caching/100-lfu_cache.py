#!/usr/bin/env python3
"""
LFU Caching (Least Frequently Used)
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.keys = []
        self.freq = {}

    def put(self, key, item):
        """
        Put an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = None
            min_freq = min(self.freq.values())
            keys = [k for k, v in self.freq.items() if v == min_freq]
            if len(keys) == 1:
                discard = keys[0]
            else:
                for idx, k in enumerate(self.keys):
                    if k in keys:
                        discard = k
                        break
            self.keys.remove(discard)
            del self.cache_data[discard]
            del self.freq[discard]
            print("DISCARD: {}".format(discard))
        self.keys.append(key)
        self.cache_data[key] = item
        self.freq[key] = 1

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        return self.cache_data[key]
