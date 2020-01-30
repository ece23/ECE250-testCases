# ECE 250 Test Cases
This repo is intened to host test cases for students to run against their ECE 250 projects. This does not garentee that by passing
all cases that it will pass the automarker

# Running Test Cases on Windows 10 (PowerShell)
Place the following in a .ps1 file
```
$testin=$args[0]
$testout=$args[1]
$testdriver=$args[2]
diff (cat $testin | %testdriver) (cat $testout)
```
Example running a test: 
.\runTest.ps1 test1.in test1.out .\testDriver.exe

# Running Test Cases using `test_runner.py`

Note that this tool only works in linux/unix environments. It will run on WSL in windows.
If you want to check for memory leaks you need to install valgrind (already on eceubuntu)

```
sudo apt-get install valgrind
```

Usage: `python3 test_runner.py [mem] <exacutable location> <tests folder>`

mem : checks your program for memory leaks using valgrind

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
