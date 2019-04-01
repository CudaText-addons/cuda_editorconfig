import sys
import os
from cudatext import *
from .editorconfig import get_properties, EditorConfigError

def str2bool(s):
    return s=='true'

class Command:
    
    def on_open(self, ed_self):

        fn = ed_self.get_filename()
        try:
            c = get_properties(fn)
        except EditorConfigError:
            s = 'Error getting EditorConfig props: '+fn
            print(s)
            msg_status(s)
            return
            
        if not c: return
        print('EditorConfig:', c)
