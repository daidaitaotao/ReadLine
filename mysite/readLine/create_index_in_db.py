from readLine.file_reading_service import TextFiles
from readLine.models import LineIndex

# (NOTE: This is optional functionality.  It is not used by default.)

# This is a simple script which created an index table in the database for the input file.
# The table will contain the each line number mapped to the number of bytes that must be
# skipped to reach that line in the file.
line_number = 1
offset = 0
with open(TextFiles.FirstFile, 'r') as file:
    for line in file:
        line_entity = LineIndex(line_number=line_number, offset=offset)
        line_entity.save()
        line_number += 1
        offset += len(line)

