from multiprocessing import Process,Pool
import argparse
import subprocess
import socket
import json
import IPy
import os
import sys
from multiprocessing.dummy import Pool as ThreadPool

parser = argparse.ArgumentParser(description='Scan whether the IP is open or\
     whether the  port is open')
parser.add_argument('-n','--nums',help='Concurrent quantity',required=True,type=int)
parser.add_argument('-f','--type',help='ping test or tcp port test',required=True)
parser.add_argument('-ip',help='ip',required=True)
parser.add_argument('-w',help='results files',required=True)
parser.add_argument('-m',help='proc|thread',required=True)
parser.add_argument('-v',help='scan time')
args = parser.parse_args()
DATA_PATH='E:\\testcode\\.vscode\\week03'
MAX_PORT = 3

# 判断IP地址
def is_ip(address):
  try:
    IPy.IP(address)
    return True
  except Exception:
    return False

# 解析参数IP
def parse_ip(ip_str):
    if '-' in ip_str and (is_ip(ip) for ip in ip_str.split('-')):
        ip_pre = ".".join(ip_str.split('-')[0].split('.')[0:3])
        ip_start = ip_str.split('-')[0].split('.')[3]
        ip_end = ip_str.split('-')[1].split('.')[3]
        ip = [ip_pre + '.' + str(x) for x in range(int(ip_start), int(ip_end) + 1)]
        return ip
    elif is_ip(ip_str):
        return [ip_str]
    else:
        print('请输入正确的IP')
        sys.exit()

# ping IP
def ping_ip(ip):
    print('ping {}...'.format(ip))
    command = str("ping -n 1 -w 10 {}".format(ip))
    ret = subprocess.call(command,stdout=subprocess.PIPE,shell=True)
    if ret == 0:
        print('{} ping通'.format(ip))
        return '{} ping通'.format(ip)
    else:
        print('{} 不通'.format(ip))
        return '{} 不通'.format(ip)
    

# port test
def test_port(port,ip=args.ip):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(20)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        print('%s:%d is open' % (ip,port))
        return 'open'
        
    except:
        print('%s:%d is close' % (ip,port))
        return 'close'

def process_scan():
    p = Pool(args.nums)
    ips = parse_ip(args.ip)
    result_dict = {}
    if args.type == 'ping':
        for ip in ips: 
            result_dict[ip] = p.apply_async(ping_ip,args=(ip,)).get()
    elif args.type == 'tcp':
        result_dict['ip'] = args.ip
        info = []
        info_dict = {}
        for port in range(1,MAX_PORT+1):
            info_dict['port'] = port
            info_dict['status'] = p.apply_async(test_port,args=(port,)).get()
            info.append(info_dict.copy())
        result_dict['info'] = info
    p.close()
    p.join()
    return result_dict

def thread_scan():
    result_dict={}
    p = ThreadPool(args.nums)
    ips = parse_ip(args.ip)
    if args.type == 'ping': 
        result = p.map(ping_ip,ips)
        result_dict = dict(zip(list(ips),result))
    elif args.type == 'tcp':
        result_dict['ip'] = args.ip
        port_list = [port for port in range(1,MAX_PORT+1)]
        print(port_list)
        status_list = p.map(test_port,port_list)
        print(status_list)
        result_dict['status-info'] = dict(zip(port_list,status_list))
        print(result_dict)
    p.close()
    p.join()
    return result_dict


if __name__ == "__main__":

    if args.m == 'proc':
        result = process_scan()
    elif args.m == 'thread':
        result = thread_scan()
    else:
        result = None

    data = json.dumps(result,ensure_ascii=False,indent=1)
    path = os.path.join(DATA_PATH,args.w)
    with open(path,'w',encoding='utf8') as f:
        f.write(data)
    




    


