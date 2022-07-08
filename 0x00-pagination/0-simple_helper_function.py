#!/usr/bin/env python3
""" pthon file containing one function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ indx range function """

    last: int = page * page_size
    return (last - page_size, last)
