# File-Downloader

### About
File-Downloader is a script that download file from (ex: mediafire) with command line.

### Installation
1. Clone this repository
```
git clone https://github.com/XniceCraft/file-downloader
```
2. Install python3 (if you aren't installed one)
<br>• Windows: ```Download python from https://www.python.org/```
<br>• Linux : ```sudo apt-get install python3```
3. Install required python module
```
pip install -r requirements.txt
```

To use the program read the usage.

### Usage
#### 1. Download

```usage: prog.py download [-h] [-d] [-c int] [-m mode] [-t int] url```

positional arguments:<br>
```url```

optional arguments:
 - -h, --help            show this help message and exit
 - -d, --grabdirectlink  Return direct download link
 - -c int, --chunk int   Override chunk size in config
 - -m mode, --mode mode  Select singlethreaded or multithreaded download
 - -t int, --threads int Override threads count in config
 
> Example: ```python prog.py download https://mediafire.com/xxxxx```

#### 2. Resume
```usage: prog.py resume [-h] [-c int] id```

positional arguments:<br>
```id```

optional arguments:
  - -h, --help           show this help message and exit
  - -c int, --chunk int  Override chunk size in config

> Example: ```python prog.py resume 1```

#### 3. Paused
```usage: prog.py paused```

### Supported File Hosting
- Mediafire
- Solidfiles
- Tusfiles
- Anonfiles
- Bayfiles
- Racaty
- Zippyshare
- Hxfile

### Features
- Download speed meter (updated every second - Multithread / every chunk cycle - Singlethread)
- Internet ping test (based on singapore firstmedia speedtest server)
- Pause (CTRL-C for pause)
- Grab direct download link with -d argument
- Can select singlethreaded or multithreaded (default: multithreaded)

### Known Issues
- 

> Please report if there is a bug on this script
