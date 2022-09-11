from fastapi import FastAPI, responses
from datetime import datetime
from humanize import naturalsize
import GPUtil
import requests
import os
import psutil
import uvicorn
import cpuinfo
import netifaces

LOCALHOST = '127.0.0.1'
PORT = int(os.environ.get('PORT'))

app = FastAPI()


def get_utc_time():
    return datetime.now().isoformat()


def get_local_ip_address():
    return list(
        map(
            lambda x: x[0].address, filter(
                lambda x: (x[0].family == netifaces.AF_INET)
                          & (x[0].address != LOCALHOST),
                psutil.net_if_addrs().values()
            )
        )
    )[0]


def get_external_ip_address():
    try:
        return requests.get(url="https://ident.me", timeout=10).text
    except requests.exceptions.ConnectionError:
        return "Cannot connect to ident.me"


def get_cpu_model():
    return cpuinfo.get_cpu_info()['brand_raw']


def get_cpu_cores():
    return psutil.cpu_count()


def get_gpu_type():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No GPU found"
    else:
        return gpus[0].name


def get_memory_size():
    return naturalsize(psutil.virtual_memory().total)


def get_system_info():
    separator = ''
    elements = [f'Time UTC On Server: {get_utc_time()}',
                separator,
                f'Local IP Address: {get_local_ip_address()}',
                f'External IP Address: {get_external_ip_address()}',
                separator,
                f'CPU Model: {get_cpu_model()}',
                f'CPU Cores: {get_cpu_cores()}',
                f'GPU Type: {get_gpu_type()}',
                separator,
                f'Memory Size: {get_memory_size()} '
                ]

    return '\n'.join(elements)


@app.get("/", response_class=responses.PlainTextResponse)
async def root():
    return str(get_system_info())


if __name__ == '__main__':
    uvicorn.run(app, port=PORT)
