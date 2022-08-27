# ffmpegthreading
To reproduce a bug to do with compiling a python script and ffmpeg 

1). First, copy the files into new repo
2). pip install: (pydub, simpleaudio)
2.1). Install ffmpeg and add the folder path to your system variables (http://ffmpeg.org/ for download) (should end in '/ffmpeg/bin')
3). Verify that script it works inside of IDE, run main.py and click the buttons (mind that the bottom button will play a song very loudly
4). Compile using auto-py-to-exe
5). Add main.py as "script location"
6). Add 'audio' folder under additional files
7). Compile
8). Open main.exe from the output folder
9). Click "(it is very loud btw, use volume mixer. turn down)" button
10). Watch command prompt open & close very quickly
