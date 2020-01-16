import sys
import subprocess
import os

#args = str(sys.argv)
#print(args)
program = sys.argv[1]
folder = sys.argv[2]

#command = "ls "+folder+"| grep .in"
ls = subprocess.Popen(["ls", folder],stdout=subprocess.PIPE)
in_files = subprocess.Popen(["grep", ".in"], stdin=ls.stdout, stdout=subprocess.PIPE)
ls.stdout.close()
in_files = sorted(in_files.communicate()[0].splitlines())
ls.wait()

ls = subprocess.Popen(["ls", folder],stdout=subprocess.PIPE)
out_files = subprocess.Popen(["grep", ".out"], stdin=ls.stdout, stdout=subprocess.PIPE)
ls.stdout.close()
out_files = sorted(out_files.communicate()[0].splitlines())

for i, v in enumerate(in_files):
    #print(i)
    #print(type(i))
    with open(folder+"/"+str(v, 'utf-8'), 'r') as f:
        with open("out", "w+") as outfile:
        #print(f)
            print("-------------------------------------")
            print("testing file: ", str(v, 'utf-8'))
            print("-------------------------------------")
            subprocess.Popen(program, stdin=f, stdout=outfile)
            test = subprocess.Popen(["diff", "out", folder+"/"+str(out_files[i], 'utf-8')], stdout=subprocess.PIPE)
            print("difference: ") 
            print(str(test.communicate()[0], 'utf-8'), end='')