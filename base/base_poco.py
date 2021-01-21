import allure
import yaml
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from datetime import datetime
import logging.handlers

# 连接设备，打开app，返回对象
def init_poco():
    connect_device('Android:///192.168.40.38:5555?cap_method=javacap&touch_method=adb')
    start_app("com.zoxun.kawxhj.hjbf")
    time.sleep(7)
    poco = UnityPoco()
    time.sleep(7)
    return poco
# 关闭应用
def quit():
    stop_app("com.zoxun.kawxhj.hjbf")
    time.sleep(3)
# 日志
def log():
    # 日志器对象
    logger = logging.getLogger("airtest")
    # 文件处理器对象
    fh = logging.handlers.TimedRotatingFileHandler("c.log",when="midnight",interval=1,backupCount=0,encoding="UTF-8")
    # 控制台处理器对象
    sh = logging.StreamHandler()
    # 格式化器对象
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 把格式化器添加到处理器
    fh.setFormatter(formatter)
    # 把处理器添加到日志器
    logger.addHandler(fh)
    logger.setLevel(logging.ERROR)
    logger.error("111")
# 截图及路径
def screenshot(text):
    file = datetime.now().strftime("../screenshot/screenshot-%Y-%m-%d %H-%M-%S.png")
    G.DEVICE.snapshot(file)
    screen = open(file, "rb").read()
    allure.attach(screen, text, allure.attachment_type.PNG)
# 测试数据解析
def analyze_file(file_path,data_key):
    with open (file_path,"r") as f:
        data = yaml.load(f)
        dict_data = data[data_key]
        list_data = []
        for i in dict_data.values():
            list_data.append(i)
        return list_data