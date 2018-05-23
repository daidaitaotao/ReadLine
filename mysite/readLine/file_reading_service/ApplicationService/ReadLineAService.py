import logging

from readLine.file_reading_service import TextFiles
from readLine.models import LineIndex
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
from readLine.file_reading_service.Utils.FunctionTimer import FunctionTimer
from memory_profiler import profile


class ReadLineAService(object):
    """
        Application service designed to read a user-specified line from a file
    """

    # Variables used for memory profiling
    precision = 10
    memory_file = open(TextFiles.MEMORY_PROFILE_FILE, 'w')

    @staticmethod
    @FunctionTimer.fn_timer
    def find_line_from_db(line_number):
        """
            A static method to find the specified line in the file using an index stored in a database
            @param line_number: the line number, with the first line being 1
            @type line_number: int
            @retype: None or str

            @precondition: isinstance(line_number, int)
        """
        assert isinstance(line_number, int), type(line_number)

        try:
            line_index_entity = LineIndex.objects.get(line_number=line_number)
        except ObjectDoesNotExist:
            ReadLineAService.__LOGGER.debug(
                'Unable to find the line index entity for line number {0}'.format(line_number)
            )
            return None

        file = open(TextFiles.FirstFile, 'r')
        offset = line_index_entity.offset
        file.seek(offset)
        line = file.readline()
        return line

    @staticmethod
    @FunctionTimer.fn_timer
    @profile(precision=precision, stream=memory_file)
    def find_line_from_index_file(line_number):
        """
            A static method to find the specified line in the file using an index stored in a file
            @param line_number: the line number, with the first line being 1
            @type line_number: int
            @retype: None or str

            @precondition: isinstance(line_number, int)
        """
        assert isinstance(line_number, int), type(line_number)

        # Calculate how many bytes must be skipped to find the entry corresponding to the line number in the index.
        # Note: The +1 is added to account for the newline character ('\n') at the end of each line.
        index_offset = (line_number - 1) * (TextFiles.LINE_LENGTH + 1)
        index_file = open(TextFiles.FirstFileIndex, 'r')
        index_file.seek(index_offset)
        index_offset_text = index_file.readline()
        if not index_offset_text:
            return None
        offset = int(index_offset_text)

        file = open(TextFiles.FirstFile, 'r')
        file.seek(offset)
        line = file.readline()
        return line

    @staticmethod
    @FunctionTimer.fn_timer
    def find_max_line_number_from_db():
        """
            A static method to find max line number of the file based on the index in the database
            @rtype: int
        """
        cache_key = 'max_line_number'
        max_line_number = cache.get(cache_key)
        if not max_line_number:
            max_line_index_entity = LineIndex.objects.latest('line_number')
            if max_line_index_entity:
                max_line_number = max_line_index_entity.line_number
            else:
                max_line_number = 0

            cache_time = 60 * 60 * 8
            cache.set(cache_key, max_line_number, cache_time)
        return max_line_number

    @staticmethod
    @FunctionTimer.fn_timer
    def find_max_line_number_from_meta_file():
        """
            A static method to find max line number of the file as stored in the meta file
            @rtype: int
        """
        cache_key = 'max_line_number'
        max_line_number = cache.get(cache_key)
        if not max_line_number:
            meta_file = open(TextFiles.FirstFileMeta, 'r')
            max_line_number = meta_file.readline()
            if max_line_number is not None and max_line_number != '':
                max_line_number = int(max_line_number)
            else:
                max_line_number = 0

            cache_time = 60 * 60 * 8
            cache.set(cache_key, max_line_number, cache_time)
        return max_line_number

    __LOGGER = logging.getLogger(__name__)
    """ logger for the current class """


