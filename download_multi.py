"""
File Downloader from python
Don't steal any code from this script
"""

import threading
#pylint: disable=invalid-name,multiple-statements,missing-function-docstring,missing-class-docstring,line-too-long
ua=lambda: choice(["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51",'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'])

#CONNECTION TEST
def test():
    print(f"{cy}[T] Testing your connection")
    s=time.time()
    r.get("http://sg-speedtest.fast.net.id.prod.hosts.ooklaserver.net:8080")
    ping=int((round(time.time() - s, 3))*1000)
    if ping < 500: print(f"{gr}[G] Your connection is good | Ping : {ping}ms , pinged from Singapore Firstmedia speedtest server")
    elif 500 <= ping < 1000: print(f"{ye}[N] Your connection is normal | Ping : {ping}ms , pinged from Singapore Firstmedia speedtest server")
    else: print(f"{re}[B] Your connection is bad | Ping : {ping}ms , pinged from Singapore Firstmedia speedtest server")

#BANNER
def banner():
    print(rf"""{de} ______ _ _         _____  _
|  ____(_) |       |  __ \| |
| |__   _| | ___   | |  | | |
|  __| | | |/ _ \  | |  | | |
| |    | | |  __/  | |__| | |____
|_|    |_|_|\___   |_____/|______|
Author : https://github.com/XniceCraft
Warning!! you can't pause download while using multithreaded
""")

#GETFILESIZE
def getsize(a):
    if a < 1024:
        v=str(a) + " Bytes"
    elif 1024 <= a < 1048576:
        v=str(round(a / 1024, 2)) + " KB"
    elif 1048576 <= a < 1073741824:
        v=str(round(a / 1048576, 2)) + " MB"
    elif a >= 1073741824:
        v=str(round(a / 1073741824, 2)) + " GB"
    return v

#START
def start():
    os.system(clear)
    banner()
    test()
    time.sleep(2)
    os.system(clear)
    banner()

#MEDIAFIRE
class dl:
    dlded=0
    pos={}
    def __init__(self, url, direct):
        self.url=url
        self.direct=direct
        self.resume=False
        self.tmpsize=0
        self.u=""
        self.name=""

    class ThreadDL(threading.Thread):
        def __init__(self, name, num, url, pos):
            threading.Thread.__init__(self)
            self.name=name
            self.num=num
            self.url=url
            self.pos=pos

        def run(self):
            while True:
                data=r.Session().get(self.url,headers={"User-Agent":ua(),"Range":f"bytes={self.pos['start']}-{self.pos['end']}"},stream=True)
                if data.headers["Content-Type"] == "text/html": pass
                else: break
            dlded=0
            with open(f"{tmp}/{self.name}-{self.num}","wb") as f:
                for l in data.iter_content(chunk_size=chunk*1024):
                    dlded += len(l)
                    dl.dlded += len(l)
                    f.write(l)
            f.close()
            dl.pos[self.num]["start"]=dlded
            return

    def meter(self):
        now=time.time()
        while True in [i.is_alive() for i in self.th]:
            try:
                time.sleep(1)
                speed=time.time() - (now+1)
                done=round(100 * dl.dlded / self.tmpsize,2)
                try:
                    sys.stdout.write(cy+"\r"+"> [Downloading] Progress : "+str(done)+"% | Speed: "+str(int(dl.dlded / speed / 1000)) + " KB/s")
                    sys.stdout.flush()
                except ZeroDivisionError:
                    pass
            except KeyboardInterrupt: pass
        return

    def ai(self):
        if floor(self.tmpsize/thread) <= 2: return False
        else:
            for i in range(thread):
                if i == 0: dl.pos[1]={"start":0, "end":floor(self.tmpsize/thread)}
                elif i+1 == thread: dl.pos[i+1]={"start":floor(self.tmpsize/thread)*i+1, "end":self.tmpsize}
                else: dl.pos[i+1]={"start":floor(self.tmpsize/thread)*i+1, "end":floor(self.tmpsize/thread)*(i+1)}
            return True

    def finish(self):
        with open(f"{tmp}/{self.name}","ab") as f:
            for i in range(thread):
                with open(f"{tmp}/{self.name}-{i+1}","rb") as h:
                    f.write(h.read())
                h.close()
                os.remove(f"{tmp}/{self.name}-{i+1}")
        f.close()
        shutil.move(rf'{tmp}/{self.name}',rf"{complete}/{self.name}")

    def start(self):
        size=getsize(self.tmpsize)
        print(f"""{de}> [INFO] Filename : {self.name}
         Size : {size}""")
        print(f"{ye}> [Starting] Downloading")
        self.ai()
        self.th=[dl.ThreadDL(self.name, i+1, self.u, dl.pos[i+1]) for i in range(thread)]
        [i.start() for i in self.th]
        self.meter()
        print(f"\r\n{de}> Assembling file into one solid file. Please wait!")
        self.finish()
        print(f"{gr}> [Finished] Success download {self.name}")
        
    def mediafire(self):
        try:
            self.u=fr(r.get(self.url,headers={"User-Agent":ua()}).text).xpath('//a[@id="downloadButton"]/@href')[0]
        except IndexError:
            print(f"{re}[X] File not found")
            return
        if self.direct:
            print(f"Link : {cy}{self.u}")
            return
        if self.resume:
            self.start()
        else:
            data=r.head(self.u,headers={"User-Agent":ua(),"Connection":"keep-alive"})
            self.tmpsize=int(data.headers['content-length'])
            self.name=ru.findall('filename="(.+)"',data.headers['Content-Disposition'])[0]
            self.start()

    def solidfiles(self):
        html=r.get(self.url,headers={"User-Agent":ua()}).text
        try:
            tmplh=fr(html)
            d="csrfmiddlewaretoken="+tmplh.xpath('//div[@class=\"buttons\"]/form/input[@name=\"csrfmiddlewaretoken\"]/@value')[0]+"&referrer="
            self.u=r.post("http://www.solidfiles.com"+tmplh.xpath('//div[@class=\"buttons\"]/form/@action')[0],headers={"User-Agent":ua()},data=d).text
            self.u=ru.findall('url=(.+)',fr(self.u).xpath("//meta[@http-equiv=\"refresh\"]/@content")[0])[0]
        except IndexError:
            print(f"{re}[X] File not found")
            return
        if self.direct:
            print(f"Link : {cy}{self.u}")
            return
        if self.resume:
            self.start()
        else:
            data=r.head(self.u,headers={"User-Agent":ua(),"Connection":"keep-alive"})
            self.tmpsize=int(data.headers['content-length'])
            self.name=r.utils.unquote((self.u).split('/')[-1])
            self.start()

    def tusfiles(self):
        html=r.get(self.url,headers={"User-Agent":ua()}).text
        try:
            tmplh=fr(html).xpath("//form[@method=\"POST\"]/input/@value")
            d=f"op={tmplh[0]}&id={tmplh[1]}&rand={tmplh[2]}&referer=&method_free=&method_premium=1"
            self.u=r.post(self.url,headers={"User-Agent":ua()},data=d,allow_redirects=False).headers["location"]
        except IndexError:
            print(f"{re}[X] File not found")
            return
        if self.direct:
            print(f"Link : {cy}{self.u}")
            return
        if self.resume:
            self.start()
        else:
            data=r.head(self.u,headers={"User-Agent":ua(),"Connection":"Keep-Alive"})
            self.name=(self.u).split("/")[-1]
            self.tmpsize=int(data.headers['content-length'])
            self.start()

    def anonfiles(self):
        html=r.get(self.url,headers={"User-Agent":ua()}).text
        try:
            self.u=fr(html).xpath('//a[@id=\"download-url\"]/@href')[0]
        except IndexError:
            print(f"{re}[X] File not found")
            return
        if self.direct:
            print(f"Link : {cy}{self.u}")
            return
        if self.resume:
            self.start()
        else:
            data=r.head(self.u,headers={"User-Agent":ua(),"Connection":"keep-alive"})
            self.name=ru.findall('filename="(.+)"',data.headers['Content-Disposition'])[0]
            self.tmpsize=int(data.headers['content-length'])
            self.start()

    def bayfiles(self):
        try:
            self.u=fr(r.get(self.url,headers={"User-Agent":ua()}).text).xpath('//a[@id="download-url"]/@href')[0]
        except IndexError:
            print(f"{re}[X] File not found")
            return
        if self.direct:
            print(f"Link : {cy}{self.u}")
            return
        if self.resume:
            self.start()
        else:
            data=r.head(self.u,headers={"User-Agent":ua(),"Connection":"keep-alive"})
            self.name=ru.findall('filename="(.+)"',data.headers['Content-Disposition'])[0]
            self.tmpsize=int(data.headers['content-length'])
            self.start()

    def racaty(self):
        html=r.get(self.url,headers={"User-Agent":ua()}).text
        try:
            tmplh=fr(html).xpath("//form[@id=\"getExtoken\"]/input/@value")
            d=f"op={tmplh[0]}&id={tmplh[1]}&rand={tmplh[2]}&referer=&method_free&method_premium=1"
            self.u=r.post(self.url,headers={"User-Agent":ua()},data=d).text
            self.u=fr(self.u).xpath("//a[@id='uniqueExpirylink']/@href")[0]
        except IndexError:
            print(f"{re}[X] File not found")
            return
        if self.direct:
            print(f"Link : {cy}{self.u}")
            return
        if self.resume:
            self.start()
        else:
            data=r.head(self.u,headers={"User-Agent":ua(),"Connection":"keep-alive"})
            self.name=(self.u).split("/")[-1]
            self.tmpsize=int(data.headers['content-length'])
            self.start()

    def zippyshare(self):
        html=r.get(self.url,headers={"User-Agent":ua()}).text
        try:
            self.u=fr(html).xpath("//a[@id=\"dlbutton\"]/following-sibling::script/text()")[0].splitlines()[1]
            self.u=ru.findall("= (.+);",self.u)[0]
            tmpvar="'"+str(eval(ru.findall("\\+ (.+) \\+",self.u)[0]))+"'"
            self.u="https://"+(self.url).split("/")[2]+eval(ru.sub("(\\(.+\\))",tmpvar,self.u))
        except IndexError:
            print(f"{re}[X] File not found")
            return
        if self.direct:
            print(f"Link : {cy}{self.u}")
            return
        if self.resume:
            self.start()
        else:
            data=r.Session().head(self.u,headers={"User-Agent":ua()})
            self.name=r.utils.unquote(ru.findall("UTF-8\'\'(.+)",data.headers['Content-Disposition'])[0])
            self.tmpsize=int(data.headers['content-length'])
            self.start()

    def hxfile(self):
        html=r.get(self.url,headers={"User-Agent":ua()}).text
        try:
            tmplh=fr(html).xpath("//form[@name=\"F1\"]/input/@value")
            d=f"op={tmplh[0]}&id={tmplh[1]}&rand={tmplh[2]}&referer=&method_free&method_premium=1"
            self.u=r.post(self.url,headers={"User-Agent":ua(),"content-type":"application/x-www-form-urlencoded"},data=d).text
            self.u=fr(self.u).xpath("//a[@class=\"btn btn-dow\"]/@href")[0]
        except IndexError:
            print(f"{re}[X] File not found")
            return
        if self.direct:
            print(f"Link : {cy}{self.u}")
            return
        if self.resume:
            self.start()
        else:
            data=r.head(self.u,headers={"User-Agent":ua(),"Connection":"keep-alive"})
            self.name=(self.u).split("/")[-1]
            self.tmpsize=int(data.headers['content-length'])
            self.start()

def get_setting():
    temp=[]
    with open("config.json","r") as f:
        jsonvar=json.loads(f.read())
        temp.append(jsonvar["tmp_location"])
        temp.append(jsonvar["complete_location"])
        temp.append(jsonvar["chunk_size"])
        temp.append(jsonvar["thread_count"])
    return temp

if __name__ == "__main__":
    from math import floor
    from random import choice
    from platform import system as ps
    import sys,re as ru,time,os,json,shutil # pylint: disable=multiple-imports
    try:
        from lxml.html import fromstring as fr
        import requests as r
    except ModuleNotFoundError:
        print("Install required package with 'pip install -r requirements.txt'")
        sys.exit(1)
    if sys.version_info[0] == 3: pass
    else:
        print("Run with python3!")
        sys.exit(1)

    #COLOR CODE
    if ps() == 'Windows':
        try:
            from colorama import init, Fore, Style
            init()
            re=Fore.RED + Style.BRIGHT
            gr=Fore.GREEN + Style.BRIGHT
            ye=Fore.YELLOW + Style.BRIGHT
            cy=Fore.CYAN + Style.BRIGHT
            ma=Fore.MAGENTA + Style.BRIGHT
            de=Fore.RESET + Style.BRIGHT
            clear="cls"
        except ModuleNotFoundError:
            print("Install colorama with 'pip install colorama'")
            sys.exit()
    else:
        re="\033[1;31m"
        gr="\033[1;32m"
        ye="\033[1;33m"
        ma="\033[1;35m"
        cy="\033[1;36m"
        de="\033[1;0m"
        clear="clear"

    tmp=get_setting()
    complete=tmp[1]
    chunk=tmp[2]
    thread=tmp[3]
    tmp=tmp[0]
    if not isinstance(chunk,int): raise ValueError("Chunk Size must be an integer")
    if thread == 1 or thread > 8: 
        print(f"{re}Error: {de}Please use thread value from 2 to 8")
        sys.exit()
    if tmp[-1:] == "/": tmp=tmp[:-1]
    if complete[-1:] == "/": complete=complete[:-1]
    if not os.path.isdir(tmp): os.mkdir(tmp)
    if not os.path.isdir(complete): os.mkdir(complete)

    args=sys.argv
    arg=len(sys.argv)
    if arg > 3 and sys.argv[1] == "-p":
        start()
        directdl=bool(arg > 4 and "-grabdirectlink" in args)
        try: 
            chunk=int(args[args.index("-c")+1]) if (True if "-c" in args else False) else chunk
        except IndexError: raise ValueError("You must specify the chunk size value") from None
        if args[2] == "mediafire":
            dl(args[3], directdl).mediafire()
        elif args[2] == "solidfiles":
            dl(args[3], directdl).solidfiles()
        elif args[2] == "tusfiles":
            dl(args[3], directdl).tusfiles()
        elif args[2] == "anonfiles":
            dl(args[3], directdl).anonfiles()
        elif args[2] == "bayfiles":
            dl(args[3], directdl).bayfiles()
        elif args[2] == "racaty":
            dl(args[3], directdl).racaty()
        elif args[2] == "zippyshare":
            dl(args[3], directdl).zippyshare()
        elif args[2] == "hxfile":
            dl(args[3], directdl).hxfile()
        else:
            print(f"{de}File Hosting Not Found")
    else:
        print(f'''{de}Usage : python {sys.argv[0]} [option] [url] [optional option]
  -h    Show help
  -p    mediafire, solidfiles, tusfiles, anonfiles, bayfiles, racaty, zippyshare, hxfile
  Optional options:
    -grabdirectlink  Get direct download link only
    -c [int]         Override chunk size in config''')
else:
    raise ImportError("This script can\'t be imported, because may cause an error")
