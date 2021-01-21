#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""
@Author: Dian Di
@Date: 2021-1-21
@Decription: Reading wav Files
@Vision: 1.0
@Last Revising Date: 2021-1-21
@Logs
|Date|Author|Contents|Remarks|
|:-|:-|:-|:-|
|2021-1-21|Dian Di|1. Finished the basic functions |wav: 16bis single uncompress|

"""


class WavProcess:
    def __init__(self,fileName,mode):
        with open(fileName,mode) as f:
            # RIFF
            self.riffId =  f.read(4).decode()
            self.riffSize = int.from_bytes(f.read(4),byteorder="little",signed=False)
            self.riffType = f.read(4).decode()

            # Format
            self.formatID = f.read(4).decode()
            self.formatSize = int.from_bytes(f.read(4),byteorder="little",signed=False)
            self.formatAudioFormat = int.from_bytes(f.read(2),byteorder="little",signed=False)
            self.formatNumChannels = int.from_bytes(f.read(2),byteorder="little",signed=False)
            self.formatSampleRate = int.from_bytes(f.read(4),byteorder="little",signed=False)
            self.formatByteRate = int.from_bytes(f.read(4),byteorder="little",signed=False)
            self.formatBlockAlign = int.from_bytes(f.read(2),byteorder="little",signed=False)
            self.formatBitsPerSample = int.from_bytes(f.read(2),byteorder="little",signed=False)

            # Data
            self.dataId = f.read(4).decode()
            self.dataSize = int.from_bytes(f.read(4),byteorder="little",signed=False)
            self.dataNum = int(self.dataSize/2)
            self.data=[]
            for i in range(self.dataNum):
                self.data.append(int.from_bytes(f.read(2),byteorder="little",signed=True))

    def displayWavHead(self):
        print("#####    RIFF    ###############")
        print("RIFF ID: "+ self.riffId)
        print("RIFF SIZE: "+ str(self.riffSize))
        print("RIFF TYPE: "+ self.riffType)
        print("#####    FORMAT    ###############")
        print("Format ID : "+ self.formatID)
        print("Format size："+str(self.formatSize))
        print("Format Audio Format："+str(self.formatAudioFormat))
        print("Format Num Channels："+str(self.formatNumChannels))
        print("Format Sample Rate："+str(self.formatSampleRate))
        print("Format Byte Rate："+str(self.formatByteRate))
        print("Format Block Align："+str(self.formatBlockAlign))
        print("Format Bits Per Sample："+str(self.formatBitsPerSample))
        print("#####    Data    ###############")
        print("Data Id："+ self.dataId)
        print("Data Size："+ str(self.dataSize))
        print("Data Num："+str(self.dataNum))

    def displayWavData(self):
        self.displayWavHead();
        for i in range(len(self.data)):
            if i%11 != 0:
                print(self.data[i],end="\t")
            else:
                print()

"""
### Test
wav = WavProcess(wavFile,"rb")
wav.displayWavData();
"""
