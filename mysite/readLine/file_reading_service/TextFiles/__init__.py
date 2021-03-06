import codecs
import os

path = os.path.dirname(os.path.abspath(__file__))

FileTemplate = '{0}/test-data-template.txt'.format(path)
"""
    path of template file to read, the test-file can be copy of it
"""

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

MEMORY_PROFILE_FILE = '{0}/memory_profiler_basic.log'.format(path)
"""
    path of memory profiler file generated by memory_profiler
"""

