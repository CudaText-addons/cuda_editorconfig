import sys
import os
from cudatext import *
import cudatext_cmd as cmds
from .editorconfig import get_properties, EditorConfigError

class Command:

    def on_open(self, ed_self):

        fn = ed_self.get_filename()
        try:
            c = get_properties(fn)
            if c:
                self.apply(ed_self, c)
        except EditorConfigError:
            print('Error getting EditorConfig properties: '+fn)


    def on_save_pre(self, ed_self):

        if app_api_version()>='1.0.280':
            s = ed_self.get_prop(PROP_TAG, 'newline:')
            if s:
                prev = ed_self.get_prop(PROP_NEWLINE, '')
                if prev!=s:
                    ed_self.set_prop(PROP_NEWLINE, s)
                    print('EditorConfig: saving with line ends "%s"'%s)

    def apply(self, ed, c):

        #print('EditorConfig:', c)

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
                ed.set_prop(PROP_INDENT_SIZE, n)
            except:
                pass

        opt = c.get('tab_width')
        if opt:
            try:
                n = int(opt)
                ed.set_prop(PROP_TAB_SIZE, n)
            except:
                pass

        if app_api_version()>='1.0.280':
            opt = c.get('end_of_line')
            if opt:
                # don't change now, change in on_save_pre
                ed.set_prop(PROP_TAG, 'newline:'+opt)

        if app_api_version()>='1.0.279':
            opt = c.get('charset')
            if opt=='latin1':
                app_proc(PROC_CONFIG_NEWDOC_ENC_SET, 'iso88591')
            elif opt=='utf-8':
                app_proc(PROC_CONFIG_NEWDOC_ENC_SET, 'utf8')
            elif opt=='utf-8-bom':
                app_proc(PROC_CONFIG_NEWDOC_ENC_SET, 'utf8_bom')
            elif opt=='utf-16be':
                app_proc(PROC_CONFIG_NEWDOC_ENC_SET, 'utf16be_bom')
            elif opt=='utf-16le':
                app_proc(PROC_CONFIG_NEWDOC_ENC_SET, 'utf16le_bom')

        if app_api_version()>='1.0.278':
            opt = c.get('trim_trailing_whitespace')
            if opt=='true':
                ed.set_prop(PROP_SAVING_TRIM_SPACES, True)
            elif opt=='false':
                ed.set_prop(PROP_SAVING_TRIM_SPACES, False)

            opt = c.get('insert_final_newline')
            if opt=='true':
                ed.set_prop(PROP_SAVING_FORCE_FINAL_EOL, True)
            elif opt=='false':
                ed.set_prop(PROP_SAVING_FORCE_FINAL_EOL, False)
