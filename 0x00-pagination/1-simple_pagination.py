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
            assert int == type(page) and page > 0
            assert int == type(page_size) and page_size > 0
            self.dataset()
            pg = index_range(page, page_size)
            return self.__dataset[pg[0]:pg[1]]

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ indx range function """

    last: int = page * page_size
    return (last - page_size, last)


