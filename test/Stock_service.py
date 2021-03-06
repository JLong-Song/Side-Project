import win32serviceutil
import win32serviceutil
import win32event


class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = "StockLINE"
    _svc_display_name_ = "Stock LINE"
    _svc_description_ = "Check price everyday"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
        self.start()

    def SvcStop(self):
        self.stop()


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(Service)
