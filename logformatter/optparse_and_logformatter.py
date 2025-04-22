#!/usr/bin/python3

from optparse import OptionParser
import logging
import sys
from LogFormatter import LogFormatter
import traceback

def logException(errorMsg, e):
    if(hasattr(e, "message")):
        errorMsg += ": " + str(e.message)
        logging.error(errorMsg)


def mainFunction() -> None:
    processing_result : bool = True
    try:
        # user_infos = [ UserInfo("falko", "1000"), UserInfo("fstrenzke", "1001") ]
        parser = OptionParser()
        # parser.add_option("-c", "--config", dest="config_path", help="normal operation of backup_job, use the configuration file FILE (mandatory)", metavar="FILE")
        parser.add_option("-p", "--log-file-path", dest="log_file_path", default="./myname.log", help="path to the log file. A path with trainling '/' may be specified, in this case the leaf name 'backup_job.log' is automatically appended. Defaults to ./bbm.log", metavar="FILE")
        parser.add_option("-L", "--console-log-level", dest="the_console_log_level", default="info", help="log level for the console")
        parser.add_option("-l", "--logfile-log-level", dest="log_file_log_level", default="info", help="log level for the log file")
        (options, args) = parser.parse_args()
        if(options.log_file_path.endswith("/")):
            options.log_file_path += "myname.log"
        if (not LogFormatter.setup_logging(console_log_output="stdout", console_log_level=options.the_console_log_level.lower(), console_log_color=True, logfile_file=options.log_file_path, logfile_log_level=options.log_file_log_level, logfile_log_color=False, log_line_template="%(color_on)s[%(asctime)s] [%(threadName)s] [%(levelname)-8s] %(message)s%(color_off)s")):
            sys.stderr.write("Failed to setup logging, aborting.")
            sys.exit(1)

        logging.debug("application started, logging initialized")
        # if options.config_path is None:
        #     parser.error("missing --config option")
    except Exception as e:
        exc_type, exc_value, exc_tb = sys.exc_info()
        errorMsg = "an exception occured: " + str(traceback.format_exception(exc_type, exc_value, exc_tb))
        sys.stderr.write("an exception occured: " + str(traceback.format_exception(exc_type, exc_value, exc_tb)))
        logException(errorMsg, e)
        sys.exit(3)
    logging.info("app is running")


if __name__ == "__main__":
    mainFunction()
