#!/usr/bin/env python3

import sys
import argparse

from PyQt5.QtCore import QUrl, QMarginsF
from PyQt5.QtGui import QPageLayout, QPageSize
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


class PrinterView(QWebEngineView):
    def __init__(self, url, filename, do_preview, parent=None):
        super(PrinterView, self).__init__(parent)
        self.do_preview = do_preview
        self.setUrl(QUrl(url))
        self.setZoomFactor(1)
        self.loadFinished.connect(self.load_finished)
        self.filename = filename

    def load_finished(self):
        if self.do_preview:
            self.show()
        else:
            pageLayout = QPageLayout(QPageSize(QPageSize.A5), QPageLayout.Portrait,
                                     QMarginsF(0, 0, 0, 0))
            self.page().printToPdf(self.filename, pageLayout)
            self.page().pdfPrintingFinished.connect(on_pdf_finished)


def on_pdf_finished(result):
    if result:
        print(result)
        QApplication.exit()
    else:
        QApplication.exit(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", "-i", help="Input URL (http://example.com, file:///home/user/example.html, ...)",
                        required=True)
    parser.add_argument("--output", "-o", help="Write pdf to this file", required=True)
    parser.add_argument("--preview", "-p", help="Open preview", action="store_true")
    args = parser.parse_args()
    a = PrinterView(args.url, args.output, args.preview)
    sys.exit(app.exec_())