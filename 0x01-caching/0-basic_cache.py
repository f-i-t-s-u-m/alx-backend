#!/usr/bin/env python3
""" python basic cache file """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ basic caching class that extend base
        caching class """

    def put(self, key, item):
        """ put function """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ get function """

        return self.cache_data.get(key, None)
