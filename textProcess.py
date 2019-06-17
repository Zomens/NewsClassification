# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:21:43 2019

@author: Zomens
"""
import jieba
import json

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

if __name__ == "__main__":
#    createStopWordDict()
    stopWordDict = readStopWordDict()
