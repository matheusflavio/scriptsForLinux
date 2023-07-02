import re, os
ts = []
t = input()
while(t != ""):
    t = re.sub('%20',' ', t)
    t = re.sub('%28','(', t)
    t = re.sub('%29',')', t)
    ts.append(t)
    t = input()

for i in ts:
    os.system('ffmpeg -i "' + i + '" "' + re.sub('ftp://192.168.0.91:3721/', '', i) + '"')