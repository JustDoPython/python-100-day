import os
import random

fileName = 'Frozen.mp4'
logoName = 'logo.png'

# 截取视频
#os.popen('ffmpeg -i '+fileName+' -ss 00:31:15 -to 00:34:45 -c copy LetItGo.mp4')

#截取图片

# for i in range(10):
#     hour = str(random.randint(0, 1))
#     min = str(random.randint(0, 59))
#     sec = str(random.randint(0, 59))
#     os.popen('ffmpeg -ss ' + hour + ':' + min + ':' + sec + ' -i ' + fileName + ' -vframes:v 1 -q:v 2 ' + str(i) +'.jpg')

# 添加水印
#os.popen('ffmpeg -i '+fileName + ' -i ' + logoName  + ' -filter_complex "overlay=main_w-overlay_w:10" logo.mp4')

# 添加文字水印
os.popen('ffmpeg -i '+fileName+' -vf "drawtext=fontfile=Arial Unicode.ttf:text=\'文字水印\':x=w-100:y=100:fontsize=24:fontcolor=red@0.5:shadowy=2" wordWatemark.mp4')

# 提取音频
os.popen('ffmpeg -i LetItGo.mp4 -vn -c:a copy LetItGo.aac')
