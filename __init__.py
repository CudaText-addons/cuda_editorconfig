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
            if c:
                self.apply(ed_self, c)
        except EditorConfigError:
            s = 'Error getting EditorConfig properties'
            msg_status(s)
            print(s+': '+fn)
            
    def apply(self, ed, c):
        print('EditorConfig:', c)
        
        opt = c.get('indent_style')
        if opt=='space':
            ed.set_prop(PROP_TAB_SPACES, True)
        elif opt=='tab':
            ed.set_prop(PROP_TAB_SPACES, False)
        
        opt = c.get('indent_size')
        if opt:
            ed.set_prop(PROP_TAB_SIZE, int(opt))
