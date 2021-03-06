# !/usr/bin/python3.4
# -*-coding:utf-8-*-
# Created by Smartdo Co.,Ltd. on 2016/10/14.
# 功能:
#  
import tool.log
import logging
from tool.jjson.basejson import *
from tool.jfile.file import *
import sys

# 日志
tool.log.setup_logging()
logger = logging.getLogger(__name__)

CONFIG = None
CONFIGSUCCESS = False


def changeconfig(name, value):
    global CONFIG
    if CONFIG == None:
        getconfig()
    CONFIG[name] = value
    return value


def getconfig():
    global CONFIG
    global CONFIGSUCCESS
    if CONFIGSUCCESS:
        return CONFIG

    # print('参数个数为:', len(sys.argv), '个参数。')
    # print('参数列表:', str(sys.argv))
    if len(sys.argv) == 2:
        local = sys.argv[1]
    else:
        local = input("远程配置选1,否则本地:")
    filepath = "config/localconfig.json"
    if local == "1":
        filepath = "config/config.json"
    configpath = tool.log.BASE_DIR + "/" + filepath
    with open(configpath, "rb") as f:
        content = f.read().decode("utf-8", "ignore")
        error, right = isRightJson(content, True)
        if not right:
            logger.error("配置错误")
            exit()
        else:
            CONFIG = stringToObject(content)
            createjia(CONFIG["datadir"])
            # TODO
            # 配置检查
            CONFIGSUCCESS = True
            return CONFIG


def copyright(info):
    us = getconfig()
    temp = {}
    temp["info"] = info
    temp["version"] = us["version"]
    temp["company"] = us["company"]
    temp["people"] = us["developer"]
    temp["time"] = us["time"]
    hehe = '''
    所属公司：{company}
    开发人员：{people}
    编译时间：{time}
    软件版本：{version}

    {info}
    '''.format_map(temp)
    return hehe


if __name__ == "__main__":
    print(getconfig())
    print(copyright("爬虫大霸王开始运行"))
