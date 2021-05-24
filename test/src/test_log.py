import unittest

from main.src.service.writer.log import Printer


# https://realpython.com/python-testing/
class PrinterServiceTest(unittest.TestCase):
    printerService = Printer()

    '''
    printLog Service DivideBy - Positive Test
    '''
    def test_givenLogService_whenPrintLog_thenPrintLogsToConsole(self):
       self.printerService.printLog()

    '''
    logException Service DivideBy - Negative Test
    '''
    def test_givenLogService_whenLogException_thenDoNothing(self):
        self.printerService.logException()


if __name__ == '__main__':
    unittest.main()
