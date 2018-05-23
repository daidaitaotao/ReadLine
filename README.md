## How does your system work? (if not addressed in comments in source)

The purpose of the program is to quickly read a user-specified line from a large file.  Since there is no easy way to go about jumping to a specific line in a file, I could think of two potential solutions: load each line of the file into a database paired with its line number, or calculate how many bytes you’d have to skip in the file in order to jump to a specific line.  Seeing as the latter option had less external dependencies, I decided to go with that.

When considering how to go about building the file row index, I first considered using a hash table, with the line number as key and byte offset as value.  It quickly became obvious that this would not scale well, and thus I needed to look into a way to store the index outside of memory.  This led me to two potential options: store the index in a database or in an text file, both of which I implemented (but only the latter of which is currently enabled). 

- In the database, I created a table which has the line number as primary key, and the number of bytes that must be skipped to find that line in the original file as the only other column. 

- When building the index using a file, it is necessary that each line of the index file is the same length so we can skip around to specific lines easily.  The required line length is based off of the size of the input file; the last line of the index file must be able to hold a number that represents (something just shy of) the total bytes in the input file.  After calculating the required line length, each line is populated with the byte offset corresponding to the line number. For example, when I look up the offset of one specific line, I can do <line_number * length_of_each_index_line> to find the starting position of the index line, and read the index from there. 

After I get the offset byte count either from the database or the index file, I can skip to the starting position of the requested line I want to read and read the line from there. 

While the database code is present in my project, it currently only uses the index file.  This is primarily because of requirements; I have not tested the performance of one against the other.

## How will your system perform with a 1 GB file? a 10 GB file? a 100 GB file?
I did not have enough time to test 1GB, 10GB file, but I did test with 100 GB file.  In such a situation, the memory usage was reported to be around 36 MB and remained constant across requests.  Requests had an average response time of 4-5 ms with caching disabled.  This is all thanks to the index being prebuilt before any requests were served, though, a process which took almost 30 minutes.

## How will your system perform with 100 users? 10000 users? 1000000 users?
Django itself is just a framework, and thus can only handle one user at a time.  It must be placed behind Apache to support multiple concurrent users, in which case the limitation will be an Apache setting.  By default Apache is configured to support up to 150 concurrent connections, but it can be tuned to support over 8000 or more.  If a request comes in with no available workers, it will need to wait until the next worker become available for it to get served.

The only Django-based limitation would be the number of concurrent file reads that it can support.  It turns out that this is only limited by the maximum number of file system handles the host operating system supports.  On my Mac, this limit was set to “unlimited” (checkable by running “ulimit” from a shell), though I am sure this is limited in practice by the system’s available memory.

## What documentation, websites, papers, etc did you consult in doing this assignment?
I actually got a lot help from online resources. I have listed my links here.
- I learned how to write python decorator to track function running time from
http://www.marinamele.com/7-tips-to-time-python-scripts-and-control-memory-and-cpu-usage 
- I learned how to create a profile of a function memory usage here:
https://vknight.org/unpeudemath/python/2016/09/26/Profiling-and-reducing-memory-consumption-in-python.html
- I also learned how to add response status in Django REST framework:
http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
- Of course Django tutorial
https://docs.djangoproject.com/en/2.0/topics/cache/
- Various websites were also perused for information on how to use JMeter for load testing.

## What third-party libraries or other tools does the system use? How did you choose each library or framework you used?
The two main third party libraries I used were the Django rest_framework and memcached, which allow me to create the REST API end point in Django and cache the response for reuse if the same line should be requested within 15 minutes, respectively.  Django was also used, of course.

- I chose these Python libraries primarily because I wanted to write this project in Python.  Python is a popular language used in Machine Learning and Big Data applications, and thus I felt it would be a good fit for this project.

JMeter and memory_profiler (for Python) were used to measure performance.
- JMeter is one of the leading load testing toolsets, making it an obvious choice for load testing my project.  As for memory_profiler, it integrates tightly with Python to create a clean report of memory usage over time. 

## How long did you spend on this exercise? If you had unlimited more time to spend on this, how would you spend it and how would you prioritize each item?
In total, it took me about 3 days to write and test this project.  I spent 5 hours one afternoon to write the basic structure and functions of the project; 4 hours the following night to clean, optimize, and document my code, as well as write test cases for it; and 3 hours another night to do performance testing and write README file. If I had more time, these are the additional steps I’d like to takes to learn more and improve the performance:

- I may consider refactoring my program to support a configuration setting that would specify whether to use a database-based or file-based index.
- Django is a framework that needs to be fronted by a web server to support multiple simultaneous users.  I did not have time to integrate it with Apache, but would like to in the future.
- Try different django cache methods to find if there are ones more optimized for file access.
- If I were to support a database-based index, I would try different databases, such as MySQL and PostgreSQL, to compare the query performance. 
- Test out the reading the line index from the file and reading it from database with incremental size file, to see which method fits better with what size of file.
- Add more complete unit tests, such as testing a empty file.
- I want to find the complexity of the python function file.seek(), which I used to find the location of index and location of line.  I was not able to find out the answer in the documentation; I learned it could be O(1) time but I would like to find a way to prove it under various conditions. 
## If you were to critique your code, what would you have to say about it?
- While I always kept performance in mind, some aspects of it I did not give significant though until I was part-way through the project.  I could create a better plan to measure the performance in the beginning the project.
- I could think of other specialized situations in which the code could be optimized; for example, what if all lines in the input file are same length?  Should I select different method to store index based on the file size and average line size?
- The index file can grow rather large due to the storage of the byte count as a string.  If I could store the number as bytes instead, I could significantly reduce the size of the index.
