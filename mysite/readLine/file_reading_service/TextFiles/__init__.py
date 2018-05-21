import codecs
import os

path = os.path.dirname(os.path.abspath(__file__))

FirstFile = '{0}/test-data.txt'.format(path)
"""
    path of file to read
"""

FirstFileIndex = '{0}/file-index.txt'.format(path)
"""
    path of index file to read
"""

FirstFileMeta = '{0}/file-meta.txt'.format(path)
"""
    path of meta file of the file to read
"""


LINE_LENGTH = len(str(os.stat(FirstFile).st_size))
"""
    line length of each line in file index file. 
"""
