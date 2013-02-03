#!/usr/bin/env python
# encoding: utf-8
"""
make_tex_macro.py


Created by Loic Matthey on 2012-07-10
Copyright (c) 2011 . All rights reserved.
"""


import sublime
import sublime_plugin

macro_template = "\\newcommand{{\\{name}}}{{{command}}}"
macro_anchor_pattern = "%New latex commands (auto)"

class MakeLatexMacroCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):

        self.selected_region = []
        self.selected_region.append(self.view.sel()[0])

        print self.selected_region

        # Verify that we have a selected region
        if not self.selected_region[0].empty():
            # New command
            self.new_command = self.view.substr(self.selected_region[0])

            # Find where to insert the macros (look for specific comment pattern)
            anchor_region = self.view.find(macro_anchor_pattern, 0, sublime.LITERAL)

            if anchor_region:
                # The anchor pattern was found, insert there.
                self.insert_macro_at = anchor_region.end()+1
            else:
                # No anchor pattern, lets insert just after the current selection
                self.insert_macro_at = self.selected_region[0].end() + 2
            
            self.view.window().show_input_panel("Macro name:", "", self.command_name_done, self.command_name_change, None)

    def command_name_done(self, value):
        
        print self.new_macro
        print self.command_name

        try:
            edit = self.view.begin_edit('make_latex_macro')

            # Replace the selected region with the new command definition
            self.view.replace(edit, self.selected_region[0], '\\' + self.command_name)

            # Insert the new command definition (for now at the end of the file)
            self.view.insert(edit, self.insert_macro_at,  self.new_macro + '\n')

            # Move cursor forward
            # new_cursor_pos = sublime.Region(self.selected_region[0].end()+2, self.selected_region[0].end()+2)
            # self.view.sel().clear()
            # self.view.sel().add(new_cursor_pos)

        except:
            pass

        finally:
            self.view.end_edit(edit)


    def command_name_change(self, value):
        '''
            The command name changes, let's update the current name and update the Statusbar with the obtained macro
        '''

        self.command_name = value
        
        self.new_macro = macro_template.format(name=self.command_name, command=self.new_command)
        sublime.active_window().active_view().set_status("latexmacro", self.new_macro)

