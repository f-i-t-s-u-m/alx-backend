#!/usr/bin/env python3
""" python file that extends other class """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ FIFOCache police caching """

    def put(self, key, item):
        """ cache into cache_data """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                ft = list(self.cache_data.keys())[-1]
                self.cache_data.pop(ft)
                print(f'DISCARD: {ft}')
            self.cache_data[key] = item

    def get(self, key):
        """ return data from caching """
        data = self.cache_data.get(key, None)
        if data:
            self.cache_data.pop(key)
            self.cache_data[key] = data
        return data
