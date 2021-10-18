from __future__ import print_function
# Import the necessary packages
import os
import sys
import argparse

#  Import src libs
from src.engine import API_Fetcher
from src.filegen import FileGen
from src.io import IO
# Global Variables

PATH = "/home/USER/godown/buff.txt"

def check_args():
    """
    The function will check for arguments inputed and verify if the API
    endpoint is given or not.
    If Endpoint is not given rasise error from Banner
    """

    parser =  argparse.ArgumentParser(description='API endpoint gathering for caffinated event')
    parser.add_argument('-e', '--entrypoint', help='Add the API endpoint URL')

    # Check if the argument has all the arguments
    if not len(sys.argv) > 1:
        parser.print_help()
        # can include a banner here

    if parser.parse_args().entrypoint:
        api_url = parser.parse_args().entrypoint
        fetcher = API_Fetcher(api_url)
        response = fetcher.request()
        
        io = IO(PATH, response)
        io.entrypoint()

# Entry point python
if __name__ == "__main__":
    fileCheck = FileGen(PATH)
    fileCheck.isFile()
    check_args()     
