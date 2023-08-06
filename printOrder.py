import win32print

def printOrder(order):
    printer = win32print.OpenPrinter('tapioca',None)
    
    win32print.StartDocPrinter(printer,1,('order',None,'RAW'))

    try:
        win32print.StartPagePrinter(printer)
        win32print.WritePrinter(printer,order)
    finally:
        win32print.EndDocPrinter(printer)
                                                        