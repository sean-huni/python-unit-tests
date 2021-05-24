import logging

from main.src.service.calcs.calc import Division

logging.basicConfig(format='%(asctime)s - %(levelname)s  - %(name)s - %(message)s', datefmt='%d-%b-%Y %H:%M:%S',
                    level='INFO')


# https://realpython.com/python-logging/
class Printer:
    res = Division()
    log = logging.getLogger(__name__)

    def printLog(self):
        self.log.debug('This is a debug message')
        self.log.info('This is an info message')
        self.log.warning('This is a warning message')
        self.log.error('This is an error message')
        self.log.critical('This is a critical message')

    def logException(self):
        a = 5
        b = 0

        self.log.debug('Value of a: %s', a)
        self.log.debug('Value of b: %s', b)

        try:
            c = self.res.divideBy(a, b)
            self.log.debug('Result: %s', c)
        except Exception as e:
            # Prints the Error Msg with the stacktrace....
            self.log.exception("Exception caught & logged WITH stacktrace...")
            # Prints only 1 line (Error Msg) in console without the stacktrace.
            self.log.error("Exception caught & logged WITHOUT stacktrace...")
