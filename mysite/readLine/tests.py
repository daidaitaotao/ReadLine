import os
import random

from django.test import TestCase
from readLine.models import LineIndex
from readLine.file_reading_service.ApplicationService.ReadLineAService import ReadLineAService
from readLine.file_reading_service import TextFiles


class ReadLineTestCase(TestCase):
    """
        class to test functions
        <readLine.file_reading_service.ApplicationService.ReadLineAService.ReadLineAService#find_line_from_index_file>,
        <readLine.file_reading_service.ApplicationService.ReadLineAService.ReadLineAService#find_max_line_number_from_meta_file>
        in <eadLine.file_reading_service.ApplicationService.ReadLineAService>
    """

    def test_max_line_number(self):
        """
            testing the max line number of the file
        """
        max_line_number = ReadLineAService.find_max_line_number_from_meta_file()
        self.assertGreaterEqual(max_line_number, 0)

    def test_get_random_line(self):
        """
            testing get a random line by given random line number
        """
        max_line_number = ReadLineAService.find_max_line_number_from_meta_file()
        if max_line_number > 0:
            random_line_number = random.randint(1, max_line_number)
            line_text = ReadLineAService.find_line_from_index_file(random_line_number)
            self.assertIsNotNone(line_text)
        return True

    def test_get_non_exist_line(self):
        """
            testing get a non-exist line from the file
        """
        max_line_number = ReadLineAService.find_max_line_number_from_meta_file()
        random_line_number = random.randint(max_line_number + 1, max_line_number + 10000)
        line_text = ReadLineAService.find_line_from_index_file(random_line_number)

        self.assertIsNone(line_text)
