import sys
import subprocess
import os

check_memory = False
if sys.argv[1] == 'mem':
    check_memory = True

program = sys.argv[1+int(check_memory)]
folder = sys.argv[2+int(check_memory)]

in_files = []
with subprocess.Popen(["ls", folder],stdout=subprocess.PIPE) as ls:
    with subprocess.Popen(["grep", ".in"], stdin=ls.stdout, stdout=subprocess.PIPE) as files:
        in_files = sorted(files.communicate()[0].splitlines())

out_files = []
with subprocess.Popen(["ls", folder],stdout=subprocess.PIPE) as ls:
    with subprocess.Popen(["grep", ".out"], stdin=ls.stdout, stdout=subprocess.PIPE) as files:
        out_files = sorted(files.communicate()[0].splitlines())

for i, v in enumerate(in_files):
    with open(folder+"/"+str(v, 'utf-8'), 'r') as f:
        with open("out", "w+") as outfile:
            print("-------------------------------------")
            print("testing file: ", str(v, 'utf-8'))
            print("-------------------------------------")
            with subprocess.Popen(program, stdin=f, stdout=outfile) as a:
                pass
            with subprocess.Popen(["diff", "out", folder+"/"+str(out_files[i], 'utf-8')], stdout=subprocess.PIPE) as test:
                print("difference: ") 
                print(str(test.communicate()[0], 'utf-8'), end='')
    
    # You'll need valgrind installed for this (its alread on eceubuntu)
    if check_memory:
        with open(folder+"/"+str(v, 'utf-8'), 'r') as f:
            with subprocess.Popen(["valgrind", program], stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as mem:
                print("memory leak: ")
                out = str(mem.communicate()[1], 'utf-8')
                if not 'All heap blocks were freed -- no leaks are possible' in out:
                    print(out)