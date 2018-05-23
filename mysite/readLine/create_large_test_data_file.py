import os

from readLine.file_reading_service import TextFiles

size = 100 * 1000 * 1000 * 1000  # 100 G
sample_file_size = os.path.getsize(TextFiles.FileTemplate)
loop_number = int(size / sample_file_size) + 1  # the times to copy the small file

file_read = open(TextFiles.FileTemplate, 'r')
lines = file_read.readlines()
with open(TextFiles.FirstFile, 'w') as file_to_write:
    for i in range(loop_number):
        for line in lines:
            file_to_write.write(line)