# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

import logging,time

logging.basicConfig(format='%(asctime)s - %(funcName)s - ThreadID:%(thread)d - ThreadName:%(threadName)s - ProcessID:%(process)d - %(pathname)s [line:%(lineno)d] - %(levelname)s: %(message)s',level=logging.DEBUG)


logo = """
     __
     /          /             /     ,
----/-----__---/-__----------/__------_/_----__-
   /    /   ) /(    | /| /  /   ) /   /    /___)
 _/_ __/___/_/___\__|/_|/__/___/_/___(_ __(___ _

"""
logo1 = """
  ___       _              _     _ _
 |_ _|_ __ | | ____      _| |__ (_) |_ ___
  | || '_ \| |/ /\ \ /\ / / '_ \| | __/ _ \
  | || | | |   <  \ V  V /| | | | | ||  __/
 |___|_| |_|_|\_\  \_/\_/ |_| |_|_|\__\___|
"""
print(logo)

time.sleep(1)
logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")