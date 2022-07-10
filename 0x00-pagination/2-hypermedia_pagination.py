#!/usr/bin/env python3
""" simple python paggination """

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ get page function to return pagginated index """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        pg: Tuple[int, int] = index_range(page, page_size)
        dataset: List[List] = self.dataset()
        data: List[List] = dataset[pg[0]:pg[1]]
        psize: int = len(data)
        npage: int = page + 1
        tpages: int = round(len(dataset) / page_size)
        ppage: int = page - 1
        if (ppage < 1):
            ppage = None

        if (npage > tpages):
            npage = None
        return {'page_size': psize, 'page': page, 'data': data,
                'next_page': npage, 'prev_page': ppage, 'total_pages': tpages}


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ indx range function """

    last: int = page * page_size
    return (last - page_size, last)
