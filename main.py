import logging
import argparse
import generate

logger = logging.getLogger(__name__)

def get_work_dir(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--work-dir', required=True, help='Work directory')
    return parser.parse_args(argv)

def main():
    generate.generate(work_dir)
    logger.info('Completed.')

if __name__ == '__main__':
    work_dir = get_work_dir().work_dir
    main()