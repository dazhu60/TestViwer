__author__ = 'Shawn Lee'
import os
import time
import subprocess


class ScreenCap:
    SAVEPATH = r"~/"
    FILE_NAME = "screencap"
    DEVICE_PATH = r"/sdcard/"

    def __init__(self, filename = None, savepath = None):
        if filename is not None:
            self.FILE_NAME = filename
        if savepath is not None:
            self.SAVEPATH = savepath

    def run(self):
        cur_time = time.strftime("%Y%m%d-%H%M%S");
        an_path = self.DEVICE_PATH + self.FILE_NAME + cur_time + ".png"
        an_cmd = r"adb shell screencap -p " + an_path
        pull_cmd = r"adb pull " + an_path + " " + self.SAVEPATH
        del_cmd = r"adb shell rm " + an_path
        subprocess.Popen(an_cmd,shell=True).communicate();

        if not os.path.exists(self.SAVEPATH):
            os.makedirs(self.SAVEPATH)

        subprocess.Popen(pull_cmd,shell=True).communicate();
        subprocess.Popen(del_cmd,shell=True).communicate();


if __name__ == '__main__':
    ScreenCap().run()
