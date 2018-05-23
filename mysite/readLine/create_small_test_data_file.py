from readLine.file_reading_service import TextFiles


file_read = open(TextFiles.FileTemplate, 'r')
lines = file_read.readlines()
with open(TextFiles.FirstFile, 'w') as file_to_write:
    for line in lines:
        file_to_write.write(line)

