#This is the script to install duo which is a dual factor authentication tool.
#It has been tested on RHEL 7
#Date: 2018-08-04



#!/usr/bin/python

import subprocess
import os

os.environ["http_proxy"]="http://<proxy-ip-address>:80"    #Exporting the proxy server IP since the download requires internet access
os.environ["https_proxy"]="https://<proxy-ip-address>:80"  
subprocess.call("yum -y install gcc openssl-devel pam-devel", shell=True) #Installation of Pre-requisite
subprocess.call("wget https://dl.duosecurity.com/duo_unix-latest.tar.gz", shell=True) # Download of the duo software
subprocess.call("tar zxf duo_unix-latest.tar.gz", shell=True) #Untar the downloaded package
os.chdir("duo_unix-1.10.1") #Changing the directory
subprocess.call("./configure --with-pam --prefix=/usr && make && sudo make install", shell=True) #Configure and Make Install

######Edit /etc/sshd/sshd_config file####
######Edit of /etc/duo/pam_duo.conf file###
######Edit /etc/pam.d/sshd 
#####Edit /etc/pam.d/system-auth
