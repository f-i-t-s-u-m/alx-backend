#!/usr/bin/env python3


import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page function to return pagginated index """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        pg: Tuple[int, int] = index_range(page, page_size)
        data: List[List] = self.dataset()
        return data[pg[0]:pg[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ indx range function """

    last: int = page * page_size
    return (last - page_size, last)
