import logging
from common import CommonPanel, Singleton
import igtk

class MovePanel(CommonPanel, metaclass=Singleton):
    def __init__(self, ui, parent):
        CommonPanel.__init__(self, ui, parent)
        logging.debug("MovePanel created")
