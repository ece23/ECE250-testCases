import sys
import subprocess
import os

program = sys.argv[1]
folder = sys.argv[2]

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
