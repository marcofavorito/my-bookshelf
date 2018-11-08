import requests
import concurrent.futures 
import logging
from typing import List

# logging.getLogger("requests").setLevel(logging.WARNING)

def parallelize_requests(links):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor, open("deadlinks.txt", "w") as output:
        future_to_url = {executor.submit(is_url_dead, i, link): (i, link) for i, link in enumerate(links)}
        for future in concurrent.futures.as_completed(future_to_url):
            i, link = future_to_url[future]
            url_is_dead = future.result()
            if url_is_dead:
                msg = "line={: 3d}, url={}".format(i, link)
                print(msg)
                output.write(msg + "\n")



def is_url_dead(line_id: int, url: str) -> bool:
    response = requests.head(url)
    return response.status_code != 200

def get_links_from_bookshelf() -> List[str]:
    bookshelf = open("bookshelf.tsv").read()
    links = [line.split("\t")[1] for line in bookshelf.split("\n")[1:] if line]
    return links

if __name__ == "__main__":
    links = get_links_from_bookshelf()
    parallelize_requests(links)


