# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:21:43 2019

@author: Zomens
"""
import jieba
import json
import os
import _thread


def createStopWordDict():
    stopWordDict = {}
    with open("stopWord.txt", "r", encoding="utf-8") as lines:
        for line in lines:
#            print(type(line))
            line = line.strip()
            key = str(line)
            stopWordDict[key] = 1
    with open("stopWordDict.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(stopWordDict, ensure_ascii=False, indent=4))

def readStopWordDict():
    with open("stopWordDict.json", "r", encoding="utf-8") as file:
        stopWordDict = json.load(file)
    return stopWordDict

def cutWord(path, stopWordDict):
    text = ""
    with open(path, "r", encoding="utf-8") as lines:
        for line in lines:
            line = line.strip()
            text = text + " " + line
    cutList = jieba.cut(text)
    return list(cutList)
    # for word in cutList:
        # if word not in stopWordDict:
            # segList.append(word)
    # return segList
        
def processText(path, label, stopWordDict):
    fileNameSave = label + ".txt"
    for root, dirNames, files in os.walk(path):
        for fileName in files:
            filePath = os.path.join(root, fileName)
            textCutWord = " ".join(cutWord(filePath, stopWordDict))
            textCutWord = "__label__"+ label + " " + textCutWord
            with open(fileNameSave, "a+", encoding="utf-8") as textSingel:
                textSingel.write(textCutWord + "\n")
    threadFlag.pop()
    print(threadFlag)
    print(label+" is over!")

if __name__ == "__main__":
    newsPath = "../THUCNews"
    stopWordDict = readStopWordDict()
    label = ""
    threadFlag = []
    for root, dirNames, files in os.walk(newsPath):
#        for dir_ in dirNames:
#            print(dir_)
            for file in files:
                if label != root[12:]:
                    filePath = root
                    label = root[12:]
                    print(filePath)
                    print(label)
                    _thread.start_new_thread( processText, ( filePath, label, stopWordDict, ))
                    threadFlag.append(1)
#                print(label)
#                print(os.path.join(root, fileName))

#    threadFlag = []
#    stopWordDict = readStopWordDict()
#
#try:
#    #multip thread
#    _thread.start_new_thread( processText, ( path1, label, ))
#    _thread.start_new_thread( processText, ( path1, label, ))
#    _thread.start_new_thread( processText, ( path1, label, ))
#except:
#    print("Error: thread error!")
#
while threadFlag:
    pass
print("work is over!")
