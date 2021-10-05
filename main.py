from __future__ import print_function
# import the necessary packages

import os
import sys
import argparse

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
        
    



# Entry point python
if __name__ == "__main__":
    check_args()     
