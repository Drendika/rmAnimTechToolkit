"""
__init__.py for rmGimbalMonitor_V2
Executes before all main files.
"""
from maya import cmds
from .logger_setup import setupLogger

logger = setupLogger(__name__)

logger.info("Log file created, %s", cmds.about(ctime=True).rstrip("\r\n"))
logger.info("Maya version: %s",cmds.about(installedVersion=True))
logger.info("Qt version: %s", cmds.about(qtVersion=True))
logger.info("Connection to the Internet: %s", cmds.about(connected=True))
logger.info("Operating System: %s", cmds.about(operatingSystem=True))
