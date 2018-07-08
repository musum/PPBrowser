import os
import os.path as osp
import sys
import signal

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal as Signal

from utils import programs
from utils.qthelpers import DialogManager

DEV = True


class MainWindow(QMainWindow):
    """Spyder main window"""
    DOCKOPTIONS = QMainWindow.AllowTabbedDocks|QMainWindow.AllowNestedDocks
    CURSORBLINK_OSDEFAULT = QApplication.cursorFlashTime()
    DEFAULT_LAYOUTS = 4

    # Signals
    restore_scrollbar_position = Signal()
    all_actions_defined = Signal()
    sig_pythonpath_changed = Signal()
    sig_open_external_file = Signal(str)
    sig_resized = Signal("QResizeEvent")  # related to interactive tour
    sig_moved = Signal("QMoveEvent")      # related to interactive tour

    def __init__(self, options=None):
        QMainWindow.__init__(self)

        qapp = QApplication.instance()
        qapp.setAttribute(Qt.AA_UseHighDpiPixmaps)
        self.default_style = str(qapp.style().objectName())

        self.dialog_manager = DialogManager()

        self.init_workdir = options.working_directory
        self.profile = options.profile
        self.multithreaded = options.multithreaded
        self.new_instance = options.new_instance
        self.open_project = options.open_project
        self.window_title = options.window_title

        self.debug_print("Start of MainWindow constructor")

        def signal_handler(signum, frame=None):
            """Handler for signals."""
            sys.stdout.write('Handling signal: %s\n' % signum)
            sys.stdout.flush()
            QApplication.quit()

        if os.name == "nt":
            try:
                import win32api
                win32api.SetConsoleCtrlHandler(signal_handler, True)
            except ImportError:
                pass
        else:
            signal.signal(signal.SIGTERM, signal_handler)
            if not DEV:
                # Make spyder quit when presing ctrl+C in the console
                # In DEV Ctrl+C doesn't quit, because it helps to
                # capture the traceback when spyder freezes
                signal.signal(signal.SIGINT, signal_handler)

        # Use a custom Qt stylesheet
        # if sys.platform == 'darwin':
        #     spy_path = get_module_source_path('ppbrowser')
        #     img_path = osp.join(spy_path, 'images')
        #     mac_style = open(osp.join(spy_path, 'app', 'mac_stylesheet.qss')).read()
        #     mac_style = mac_style.replace('$IMAGE_PATH', img_path)
        #     self.setStyleSheet(mac_style)

        # Create our TEMPDIR
        if not osp.isdir(programs.TEMPDIR):
            os.mkdir(programs.TEMPDIR)

        # Shortcut management data
        self.shortcut_data = []

        # Loading Spyder path
        self.path = []

        # Plugins
        self.console = None

        # File switcher
        self.fileswitcher = None

        # Check for updates Thread and Worker, refereces needed to prevent
        # segfaulting
        self.check_updates_action = None
        self.thread_updates = None
        self.worker_updates = None
        self.give_updates_feedback = True
