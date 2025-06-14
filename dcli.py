# dCLI
# CLI kernel / builder
# by evr4, open license

import os

class CLI:
    def __init__(self, clmode: bool = False):
        self.handlers = {}
        self.clmode = clmode
    
    def handle(self):

        while True:
            command = input(self.promptfunc())
            
            if not command: continue

            if ' | ' in command:
                command = command.split(' | ')
                if command[0].split()[0] in self.handlers:
                    ret = self.handlers[command[0].split()[0]](command[0])
                else:
                    ret = self.handlers['$'](command[0])
                del command[0]

                for i in command:
                    if i.split()[0] in self.handlers:
                        ret = self.handlers[i.split()[0]](i + ' ' + ret)
                    else:
                        ret = self.handlers['$'](i + ' ' + ret)
            else:
                if command.split()[0] in self.handlers:
                    ret = self.handlers[command.split()[0]](command)
                else:
                    ret = self.handlers['$'](command)

            if self.clmode:
                os.system('clear')
                if hasattr(self, 'indfunc'):
                    print(self.indfunc())
            
            if ret:
                print(ret)

            print()

    def handler(self, command):
        '''Decorator for handling commands. $ for handle unknown commands.'''

        def f(func):
            self.handlers[command] = func
            return func
        return f
    
    def prompt(self):
        '''Decorator function returns prompt'''

        def f(func):
            self.promptfunc = func
            return func
        return f
    
    def ind(self):
        def f(func):
            self.indfunc = func
            return func
        return f