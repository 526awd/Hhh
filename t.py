import os
os.system('cp Zundamon「なのだ」1735928147797.mp4 1.mp4')
os.mkdir('morr')
os.system('cp 1.mp4 morr/1.mp4')

for i in range(400):
    os.system('ffmpeg -f concat -safe 0 -i input.txt -c copy output.mp4')
    os.system('rm -f 1.mp4')
    print(i)
    os.system('mv output.mp4 1.mp4')
os.system('rm -f morr/1.mp4')
os.system('cp 1.mp4 morr/1.mp4')
for i in range(216):
    os.system('ffmpeg -f concat -safe 0 -i input.txt -c copy output.mp4')
    os.system('rm -f 1.mp4')
    os.system('mv output.mp4 1.mp4')
    print(i)
