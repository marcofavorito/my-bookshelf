from typing import List


class Item:

    def __init__(self, id_:int, title:str, link:str, tags: List[str]):
        self.id = id_
        self.title = title
        self.link = link
        self.tags = tags


def get_items_from_bookshelf() -> List[Item]:
    bookshelf_lines = open("bookshelf.tsv").readlines()
    items = [Item(i, line[0], line[1], line[2:])
             for i, line in enumerate(map(lambda line: line.split("\t"), bookshelf_lines[1:]))]
    return items
