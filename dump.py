import logging
import multiprocessing
import os
import re
import subprocess
import shutil

from items import get_items_from_bookshelf

logger = logging.getLogger("dump")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.FileHandler("dump.log", mode='w'))

TEMP_DOWNLOAD_DIR = "download"
ARCHIVE_BASE_NAME = "dump"


def wget_download(item):
    logger.info("Start download of {:04}:'{}'".format(item.id, item.title))
    try:
        FNULL = open(os.devnull, 'w')
        cmd_list = ['wget',
                    "%s" % item.link,
                    "-P",
                    "%s/%s" % (TEMP_DOWNLOAD_DIR, re.sub("[^A-Za-z0-9._-]", "_", item.title)),
                    "--no-parent",
                    ">/dev/null",
                    "2>&1"
                    ]
        logger.info(subprocess.list2cmdline(cmd_list))
        subprocess.call(cmd_list, stdout=FNULL, stderr=FNULL)
        logger.info("Finished download of {:04}:'{}'".format(item.id, item.title))
    except Exception as e:
        logger.info("Problems with {}:'{}'. {}".format(item.id, item.title, str(e)))


if __name__ == "__main__":
    items = get_items_from_bookshelf()

    logger.info("Pre-clean")
    shutil.rmtree(TEMP_DOWNLOAD_DIR, ignore_errors=True)
    os.mkdir(TEMP_DOWNLOAD_DIR)

    logger.info("Downloading...")
    with multiprocessing.Pool(10) as pool:
        pool.map(wget_download, items)

    logger.info("Compressing...")
    shutil.make_archive(ARCHIVE_BASE_NAME, 'gztar', base_dir=TEMP_DOWNLOAD_DIR)

    logger.info("Cleaning...")
    shutil.rmtree(TEMP_DOWNLOAD_DIR)
