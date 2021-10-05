import os
"""
File Generator

Author Danwand NS   github.com/DanBrown47
verify if the buffer file is present, if not generates one
as temp storage of the file
"""

class FileGen:
    """
    Checks if the file is present if not generate
    """

    def __init__(self, path) -> None:
        self.path = path
        pass
    
    def generate(self) -> None:
        os.mkdir("godown")
        os.chdir("godown")
        f = open("buff.txt","x")

    def isFile(self) -> None:
        presence = os.path.isfile(self.path)
        if not presence:
            FileGen.generate(self)
        else:
            # Can Add banner here
            print("File Exists")
            pass
