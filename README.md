# ECE 250 Test Cases
This repo is intened to host test cases for students to run against their ECE 250 projects. This does not garentee that by passing
all cases that it will pass the automarker

# Running Test Cases using `test_runner.py`

```
sudo apt-get install valgrind
```

Usage: `python3 test_runner.py [mem] <exacutable location> <tests folder>`

mem : checks your program for memory leaks using valgrind

Usage: `python3 test_runner.py <exacutable location> <tests folder>`


Example for project 0:

```
# cd into ECE250-testCases
python3 test_runner.py ../playlistdriver p0
```

Example for project 1 with memory leak checking:
```
# cd into ECE250-testCases
python3 test_runner.py mem ../dequedriver p1
```

### Owner
Quinn Hodges
