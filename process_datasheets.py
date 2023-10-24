import os
import time
import logging
from datetime import timedelta
from concurrent.futures import ProcessPoolExecutor

from utils.utils import read_datasheet

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')


def process_file(src_file):
    df = read_datasheet(src_file)
    print(df)


def process_files_parallel(src_dir, dest_dir, num_processes=4):
    processed_files = 0
    with ProcessPoolExecutor(max_workers=num_processes) as executor:

        for root, _, files in os.walk(src_dir):
            for file in files:
                src_file = os.path.join(root, file)
                executor.submit(process_file, src_file)
                processed_files += 1
    logging.info(f"Total processed files: {processed_files}")

if __name__ == '__main__':
    start_time = time.time()
    # Arguments
    src_dir = 'data'
    dest_dir = 'results'

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    process_files_parallel(src_dir, dest_dir)

    end_time = time.time()
    execution_time = end_time - start_time

    logging.info(f'Script execution time: '
                 f'{str(timedelta(seconds=execution_time))}')
