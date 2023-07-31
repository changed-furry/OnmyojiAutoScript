# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from time import sleep
from datetime import time, datetime, timedelta

from module.logger import logger
from module.exception import TaskEnd


from tasks.RichMan.assets import RichManAssets
from tasks.RichMan.mall.mall import Mall
from tasks.RichMan.guild import Guild
from tasks.RichMan.shrine import Shrine
from tasks.RichMan.thousand_things import ThousandThings


class ScriptTask(ThousandThings, Shrine, Guild, Mall, RichManAssets):

    def run(self):
        self.execute_tt()
        self.execute_shrine()
        self.execute_guild()
        self.execute_mall()

        self.set_next_run(task='RichMan', success=True, finish=False)

        raise TaskEnd('RichMan')













if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device
    from memory_profiler import profile
    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)

