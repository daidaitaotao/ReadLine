from django.http import HttpResponse
from readLine.file_reading_service.ApplicationService.ReadLineAService import ReadLineAService
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return HttpResponse("<h4>Welcome to the ReadLine REST API!</h4>" +
                        "To retrieve a line from the backend file, please append its number to the current URL.<br>" +
                        "Example: GET /lines/201")


class LineDetail(APIView):
    def get(self, request, line_number):
        """
            Implement GET method of line detail API, which accepts a line number 
            and returns the text located at that line in the backing file.
            @param request: Request
            @param line_number: The line number client wishes to read
            @return: Response
        """
        max_line_number = ReadLineAService.find_max_line_number_from_meta_file()
        if max_line_number == 0 or max_line_number < line_number:
            return Response('The line number exceed max number of lines in the file, {0}'.format(max_line_number),
                            status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

        # cache used here
        cache_key = 'line_number' + str(line_number)  # key needs to be unique
        cache_time = 60 * 15  # 15 minutes for cache to be valid
        line_text = cache.get(cache_key)  # returns None if no key-value pair

        if not line_text:
            line_text = ReadLineAService.find_line_from_index_file(line_number)

            cache.set(cache_key, line_text, cache_time)

        if line_text:
            return Response({'data': line_text})
        else:
            return Response('line does not exist', status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)