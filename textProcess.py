# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:21:43 2019

@author: Zomens
"""
import jieba
import json
import os

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
    segList = []
    for word in cutList:
        if word not in stopWordDict:
            segList.append(word)
    return segList
        
    

if __name__ == "__main__":
#    createStopWordDict()
    newsPath = "../THUCNews/体育"
    stopWordDict = readStopWordDict()
    for root, dirNames, files in os.walk(newsPath):
        for fileName in files:
            path = os.path.join(root, fileName)
#            print(path)
            label = "__sports__"
            textCutWord = " ".join(cutWord(path, stopWordDict))
            textCutWord = textCutWord + "    \t" + label
            with open("sports.txt", "a+", encoding="utf-8") as textSingel:
                textSingel.write(textCutWord + "\n")
            
