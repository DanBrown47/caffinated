"""
Caffinated Event, Core Snippet

Author : Danwand NS    github.com/DanBrown47
"""
from typing import Set
import requests 

class API_Fetcher():
    """
    The class sends a GET Request to the API to fetch and return the 
    content to a JSON
    """

    def __init__(self, api_url:'str') -> None:
        self.url = api_url
        
    def request(self) -> str:
        """
        The requests are taken, awaits resposes from the
        server and returned as JSON string
        """
        response = requests.get(self.url)
        #  Check if 200 else expection
        return response.json()
        

        
        