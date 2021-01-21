#!/usr/bin/env python3
#-*- coding:utf-8 -*-

## import libs
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


## visables
filePath = "./demoTestAudio/"
fileName = "opensmile.wav"
wavFile = filePath+fileName
# print(wavFile)

with open(wavFile,"rb") as f:
    # RIFF
    riffId =  f.read(4).decode()
    riffSize = int.from_bytes(f.read(4),byteorder="little",signed=False)
    riffType = f.read(4).decode()

    # Format
    formatID = f.read(4).decode()
    formatSize = int.from_bytes(f.read(4),byteorder="little",signed=False)
    formatAudioFormat = int.from_bytes(f.read(2),byteorder="little",signed=False)
    formatNumChannels = int.from_bytes(f.read(2),byteorder="little",signed=False)
    formatSampleRate = int.from_bytes(f.read(4),byteorder="little",signed=False)
    formatByteRate = int.from_bytes(f.read(4),byteorder="little",signed=False)
    formatBlockAlign = int.from_bytes(f.read(2),byteorder="little",signed=False)
    formatBitsPerSample = int.from_bytes(f.read(2),byteorder="little",signed=False)

    # Data
    dataId = f.read(4).decode()
    dataSize = int.from_bytes(f.read(4),byteorder="little",signed=False)
    dataNum = int(dataSize/2)
    data=[]
    for i in range(dataNum):
        data.append(int.from_bytes(f.read(2),byteorder="little",signed=True))



    # Test && Debug

    print("#####    RIFF    ###############")
    print("RIFF ID: "+ riffId)
    print("RIFF SIZE: "+ str(riffSize))
    print("RIFF TYPE: "+ riffType)
    print("#####    FORMAT    ###############")
    print("Format ID : "+ formatID)
    print("Format size："+str(formatSize))
    print("Format Audio Format："+str(formatAudioFormat))
    print("Format Num Channels："+str(formatNumChannels))
    print("Format Sample Rate："+str(formatSampleRate))
    print("Format Byte Rate："+str(formatByteRate))
    print("Format Block Align："+str(formatBlockAlign))
    print("Format Bits Per Sample："+str(formatBitsPerSample))
    print("#####    Data    ###############")
    print("Data Id："+ dataId)
    print("Data Size："+ str(dataSize))
    print("Data Num："+str(dataNum))
    #for i in data:
    #    print(i)

    plt.plot(data)
    plt.show()
