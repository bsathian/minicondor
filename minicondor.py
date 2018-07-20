from __future__ import print_function
import subprocess
import os
import sys

globalCounter = 0
FNULL = open("temp_outputs.txt","w")
def new_process(nextFile,command):
    global globalCounter
    globalCounter = globalCounter + 1
    command.insert(1,nextFile)
#    command = ["./analyze",nextFile,"Zll_histograms",str(globalCounter),"none","2","1","1"]
#    print(command)
    p = subprocess.Popen(command,stdout = FNULL,stderr = subprocess.STDOUT)
    return p


def minicondor(fileList,command):

    files = open(fileList,"r")

    jobQueue = []
    for i in files:
        jobQueue.append(i.rstrip("\n"))

    pSpace = [] #Process space

    print(len(jobQueue))
    while (len(jobQueue) > 0) or (len(pSpace) > 0):
        temp_pSpace = [i for i in pSpace if i.poll() == None]
        pSpace = temp_pSpace
#        print("pSpace before adding proceses=",len(pSpace))
        newProcs = min(8-len(pSpace),len(jobQueue))
#        print("newProcs=",newProcs)
        for i in range(newProcs):
            print("Running file",jobQueue[0])
            pSpace.append(new_process(nextFile = jobQueue[0],command = command))
            del jobQueue[0]
 #       print("pSpace=",len(pSpace))


command = []
if argc < 3:
    print("Usage : minicondor <filelist> <commands>")
    print("looper should take root file as first argument")
else:
    for i in range(2,argc):
        command.append(i)
        minicondor(filelist = sys.argv[1],command = command)
