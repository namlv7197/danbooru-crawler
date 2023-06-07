from src.crawler import ChromeDriver
import argparse
from src.utils import crawl

def args_parser():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--start_id",
                        type=str,
                        default=1,
                        help="""parse the specific post id to crawl""")
    
    parser.add_argument("--uri",
                        type=str,
                        default=None,
                        help="""parse the specific uri to store""")
    
    parser.add_argument("--db",
                        type=str,
                        default=1,
                        help="""parse the specific database name""")
    
    parser.add_argument("--collection",
                        type=str,
                        default=1,
                        help="""parse the specific collection name""")
    
    parser.add_argument("--username",
                        type=str,
                        default='',
                        help="""This argument means that providing username if require_login is True""")
    
    parser.add_argument("--password",
                        type=str,
                        default='',
                        help="""This argument means that providing password if require_login is True""")
    
    return parser.parse_args()

def main(args):
    crawl(args)


if __name__=='__main__':
    args=args_parser()
    main(args)