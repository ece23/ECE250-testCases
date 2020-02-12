import subprocess
import platform
import sys

NLC = '\\n'


def getTestFilesAsList(folder):
    if platform.system() == 'Windows':
        ls = subprocess.run(['dir', folder], stdout=subprocess.PIPE)
    else:
        ls = subprocess.run(['ls', folder], stdout=subprocess.PIPE)
    files = str(ls.stdout).lstrip("b'").rstrip("'").replace('\\t', ' ').replace(NLC, ' ').split()
    outFiles = filter(lambda file: file[-4:] == '.out', files)
    inFiles = filter(lambda file: file[-3:] == '.in', files)
    testFiles = {'inFiles': [], 'outFiles': []}
    for file in inFiles:
        testFiles['inFiles'].append(folder + '/' + file)
    for file in outFiles:
        testFiles['outFiles'].append(folder + '/' + file)

    return testFiles


check_memory = False
if sys.argv[1] == 'mem':
    check_memory = True

program = sys.argv[1+int(check_memory)]
folder = sys.argv[2+int(check_memory)]

testFiles = getTestFilesAsList(testFolder)

for testNumber in range(len(testFiles['inFiles'])):
    with open(testFiles['inFiles'][testNumber], 'r') as inFile:
        completedProcess = subprocess.run([program], stdin=inFile, stdout=subprocess.PIPE)

    output = str(completedProcess.stdout).lstrip("b'").rstrip("'")
    # print(output)
    output = output.split(NLC)

    with open(testFiles['outFiles'][testNumber], 'r') as outFile:
        for line in output:
            expectedOutput = outFile.readline().strip()
            if expectedOutput != line:
                print('Expected: ', expectedOutput)
                print('Recieved: ', line)
                print('Are equal: ', bool(expectedOutput == line))
                print('Exiting...')
    print(f'test {testFiles['inFiles'][testNumber]} passed')
    # You'll need valgrind installed for this (its alread on eceubuntu)
    if check_memory:
        with open(folder+"/"+str(v, 'utf-8'), 'r') as f:
            with subprocess.Popen(["valgrind", program], stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as mem:
                print("memory leak: ")
                out = str(mem.communicate()[1], 'utf-8')
                if not 'All heap blocks were freed -- no leaks are possible' in out:
                    print(out)
print('All tests passed')

