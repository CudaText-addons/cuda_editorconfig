import sys
import os
from cudatext import *
import cudatext_cmd as cmds
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
            try:
                n = int(opt)
                ed.set_prop(PROP_TAB_SIZE, n)
            except:
                pass

        opt = c.get('tab_width')
        if opt:
            try:
                n = int(opt)
                ed.set_prop(PROP_TAB_SIZE, n)
            except:
                pass

        opt = c.get('end_of_line')
        if opt=='lf':
            ed.cmd(cmds.cmd_LineEndUnix)
        elif opt=='crlf':
            ed.cmd(cmds.cmd_LineEndWin)
        elif opt=='cr':
            ed.cmd(cmds.cmd_LineEndMac)

        opt = c.get('charset')
        if opt=='latin1':
            ed.cmd(cmds.cmd_Encoding_iso1_NoReload)
        elif opt=='utf-8':
            ed.cmd(cmds.cmd_Encoding_utf8nobom_NoReload)
        elif opt=='utf-8-bom':
            ed.cmd(cmds.cmd_Encoding_utf8bom_NoReload)
        elif opt=='utf-16be':
            ed.cmd(cmds.cmd_Encoding_utf16be_NoReload)
        elif opt=='utf-16le':
            ed.cmd(cmds.cmd_Encoding_utf16le_NoReload)

