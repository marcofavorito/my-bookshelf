#!/usr/bin/env python3

import requests
import concurrent.futures 
import logging
from logging import StreamHandler, FileHandler

from items import get_items_from_bookshelf, Item

OUTPUT_FILENAME = "deadlinks.tsv"

logger = logging.getLogger("check_dead_links")
logger.setLevel(logging.INFO)
logger.addHandler(StreamHandler())
logger.addHandler(FileHandler(OUTPUT_FILENAME, mode='w'))


def parallelize_requests(items):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_url_and_log_on_error, item): item for item in items}
        for future in concurrent.futures.as_completed(future_to_url):
            item = future_to_url[future]
            future.result()


class ItemNotFoundError(Exception):
    def __init__(self):
        super().__init__("Item not found (status!=200)")


def check_url_and_log_on_error(item: Item):
    try:
        response = requests.head(item.link)
        if response.status_code != 200:
            raise ItemNotFoundError()
    except (ItemNotFoundError,
            requests.exceptions.MissingSchema,
            requests.exceptions.SSLError,
            requests.ConnectionError) as e:
        logger.warning("{:05}\t{}\t{}\t{}".format(item.id, item.title, item.link, e))
        return True


if __name__ == "__main__":
    items = get_items_from_bookshelf()
    parallelize_requests(items)


