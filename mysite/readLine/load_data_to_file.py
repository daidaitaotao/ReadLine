import os

from readLine.file_reading_service import TextFiles


# This is a simple script which created an index file for the input file.
# Each line of the index file will contain the number of bytes that must be skipped to reach the
# corresponding line in the input file.

file_read = open(TextFiles.FileTemplate, 'r')
lines = file_read.readlines()
with open(TextFiles.FirstFile, 'w') as file_to_write:
    for line in lines:
        file_to_write.write(line)

index_file_to_write = open(TextFiles.FirstFileIndex, 'w')

offset = 0
total_line_number = 0
with open(TextFiles.FirstFile, 'r') as file:
    for line in file:
        line_to_write = ('{:'+ str(TextFiles.LINE_LENGTH) + 'd}').format(offset) + '\n'
        index_file_to_write.write(line_to_write)
        offset += len(line)
        total_line_number += 1

with open(TextFiles.FirstFileMeta, 'w') as meta_file_to_write:
    meta_file_to_write.write(str(total_line_number))
