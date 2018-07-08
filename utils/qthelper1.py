import sys

from utils.icon_manager import get_icon
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction)


class PPAction(QAction):
    """Spyder QAction class wrapper to handle cross platform patches."""

    def __init__(self, *args, **kwargs):
        """Spyder QAction class wrapper to handle cross platform patches."""
        super(PPAction, self).__init__(*args, **kwargs)
        self._action_no_icon = None

        if sys.platform == 'darwin':
            self._action_no_icon = QAction(*args, **kwargs)
            self._action_no_icon.setIcon(QIcon())
            self._action_no_icon.triggered.connect(self.triggered)
            self._action_no_icon.toggled.connect(self.toggled)
            self._action_no_icon.changed.connect(self.changed)
            self._action_no_icon.hovered.connect(self.hovered)
        else:
            self._action_no_icon = self

    def __getattribute__(self, name):
        """Intercept method calls and apply to both actions, except signals."""
        attr = super(PPAction, self).__getattribute__(name)

        if hasattr(attr, '__call__') and name not in ['triggered', 'toggled',
                                                      'changed', 'hovered']:
            def newfunc(*args, **kwargs):
                result = attr(*args, **kwargs)
                if name not in ['setIcon']:
                    action_no_icon = self.__dict__['_action_no_icon']
                    attr_no_icon = super(QAction,
                                         action_no_icon).__getattribute__(name)
                    attr_no_icon(*args, **kwargs)
                return result
            return newfunc
        else:
            return attr

    @property
    def no_icon_action(self):
        """Return the action without an Icon."""
        return self._action_no_icon


def toggle_actions(actions, enable):
    """Enable/disable actions"""
    if actions is not None:
        for action in actions:
            if action is not None:
                action.setEnabled(enable)


def create_action(parent, text, shortcut=None, icon=None, tip=None,
                  toggled=None, triggered=None, data=None, menurole=None,
                  context=Qt.WindowShortcut):
    """Create a QAction"""
    action = PPAction(text, parent)
    if triggered is not None:
        action.triggered.connect(triggered)
    if toggled is not None:
        action.toggled.connect(toggled)
        action.setCheckable(True)
    if icon is not None:
        if isinstance(icon, str):
            icon = get_icon(icon)
        action.setIcon(icon)
    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)
    if data is not None:
        action.setData(data)
    if menurole is not None:
        action.setMenuRole(menurole)

    # Workround for Mac because setting context=Qt.WidgetShortcut
    # there doesn't have any effect
    if sys.platform == 'darwin':
        action._shown_shortcut = None
        if context == Qt.WidgetShortcut:
            if shortcut is not None:
                action._shown_shortcut = shortcut
            else:
                # This is going to be filled by
                # main.register_shortcut
                action._shown_shortcut = 'missing'
        else:
            if shortcut is not None:
                action.setShortcut(shortcut)
            action.setShortcutContext(context)
    else:
        if shortcut is not None:
            action.setShortcut(shortcut)
        action.setShortcutContext(context)

    return action
