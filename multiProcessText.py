# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:21:43 2019

@author: Zomens
"""
import jieba
import json
import os
import _thread
import re
import multiprocessing


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

def removeSpeChar(string):
    #正则表达式去特殊字符
    cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]") # 匹配不是中文、大小写、数字的其他字符
    return cop.sub(' ', string) #将string1中匹配到的字符替换成空格
    
def cutWord(path, stopWordDict):
    text = ""
    with open(path, "r", encoding="utf-8") as lines:
        for line in lines:
            line = line.strip()
            text = text + " " + line
            text = removeSpeChar(text)
    cutList = jieba.cut(text)
    return list(cutList)
    # for word in cutList:
        # if word not in stopWordDict:
            # segList.append(word)
    # return segList
        
def threadTask(path, label, stopWordDict):
    fileNameSave = "./data/" + label + ".txt"
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

def cutWordProcess(path):
    text = ""
    with open(path, "r", encoding="utf-8") as lines:
        for line in lines:
            line = line.strip()
            text = text + " " + line
            text = removeSpeChar(text)
    cutList = jieba.cut(text)
    return list(cutList)    

def processTask(path, label):
    print(label+" is running!")
    
    fileNameSave = "./data1/" + label + ".txt"
    for root, dirNames, files in os.walk(path):
        for fileName in files:
            filePath = os.path.join(root, fileName)
            textCutWord = " ".join(cutWordProcess(filePath))
            textCutWord = "__label__"+ label + " " + textCutWord
            with open(fileNameSave, "a+", encoding="utf-8") as textSingel:
                textSingel.write(textCutWord + "\n")
    
    print(label+" is over!")

if __name__ == "__main__":
    newsPath = "../THUCNews"
    # stopWordDict = readStopWordDict()
    label = ""
    # threadFlag = []
    
    processPool = multiprocessing.Pool()
    
    
    for root, dirNames, files in os.walk(newsPath):
#        for dir_ in dirNames:
#            print(dir_)
            for file in files:
                if label != root[12:]:
                    filePath = root
                    label = root[12:]
                    print(filePath)
                    print(label)
                    processPool.apply_async(processTask, args=(filePath, label, ))
    print('Waiting for all subprocesses done...')
    processPool.close()
    processPool.join()
    print('All subprocesses done.')
                    
                    # _thread.start_new_thread( threadTask, ( filePath, label, stopWordDict, ))
                    # threadFlag.append(1)
#                print(label)
#                print(os.path.join(root, fileName))

# while threadFlag:
    # pass
# print("work is over!")

            
