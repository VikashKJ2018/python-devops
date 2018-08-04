#This is the script to install duo which is a dual factor authentication tool.
#It has been tested on RHEL 7
#Date: 2018-08-04



#!/usr/bin/python

import subprocess
import os

os.environ["http_proxy"]="http://<proxy-ip-address>:80"
os.environ["https_proxy"]="https://<proxy-ip-address>:80"
subprocess.call("yum -y install gcc openssl-devel pam-devel", shell=True)
subprocess.call("wget https://dl.duosecurity.com/duo_unix-latest.tar.gz", shell=True)
subprocess.call("tar zxf duo_unix-latest.tar.gz", shell=True)
os.chdir("duo_unix-1.10.1")
subprocess.call("pwd", shell=True)
subprocess.call("./configure --with-pam --prefix=/usr && make && sudo make install", shell=True)

