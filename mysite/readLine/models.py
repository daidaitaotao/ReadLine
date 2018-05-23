from django.db import models


class LineIndex(models.Model):
    """
        class to store one specific file index, include the line number as primary key, and the starting position
        as offset
    """
    line_number = models.BigIntegerField(primary_key=True)
    offset = models.BigIntegerField()

    class Meta:
        ordering = ('line_number',)
