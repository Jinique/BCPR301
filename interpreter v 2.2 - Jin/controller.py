from module_builder.interpreter import Interpreter
import sys
import cmd
import re  # Jin
import shutil # Jin
import datetime # Jin
from module_builder.validator import Pep8Formatter # Jin


class Controller(cmd.Cmd):
    """Plant UML to Python Interpreter"""

    prompt = ">>> "

    root = None
    source = None

    def cmdloop(self, intro="PlantUML to Python Convertor"):
        return cmd.Cmd.cmdloop(self, intro)

    def do_interpret(self, line):
        """
            ***
            Translates your SOURCE plantUML file to a python file
            in the ROOT directory provided
            Update ROOT directory: root [file_location]
            Update SOURCE file: source [source_file]
            ***
        """
        if self.root is None:
            print("Please enter the directory to write files to : root xxxx")
        elif self.source is None:
            print("Please enter the source file : source xxxx")
        else:
            x = Interpreter()
            x.add_file(self.source, self.root)
            x.write_modules()
            if len(x.all_my_errors) > 0:
                for an_error in x.all_my_errors:
                    print(an_error)
            print("Interpreting complete")

    def do_root(self, line):
        """Change the root directory"""
        self.root = line
        print(f"Root directory to write files is:  {line}")

    def do_source(self, line):
        """Change the source file"""
        self.source = line
        print(f"Source file to interpret is: {line}")

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        self.do_EOF(line)

    # Jin
    def do_quit(self):
        self.do_EOF()

    # Jin
    def help_quit(self):
        print("""
            ***
            Terminates current program.
            NOTE : Using "end of file" command.
            Usage : quit or q
            ***
        """)

    def help_interpret(self, line):
        print("""***
                Translates your SOURCE plantUML file to a python file
                 in the ROOT directory provided
                 Update ROOT directory: root [file_location]
                 Update SOURCE file: source [source_file]
                 ***
            """)

    # Jin
    def file_path(self, line):
        path = []
        for a_path in line.split(' '):
            striped_path = re.sub(' ', '', a_path).strip()
            if striped_path != '':
                path.append(striped_path)
                # print(striped_path)
        return path

    # Jin
    def do_convert(self, line):
        arg = self.file_path(line)
        if len(arg) == 2:
            converter = Interpreter()
            self.source = arg[0]
            self.root = arg[1]
            converter.add_file(self.source, self.root)
            converter.write_modules()
            if len(converter.all_my_errors) > 0:
                for an_error in converter.all_my_errors:
                    print(an_error)
            print("Interpreting complete")
        else:
            print('invalid command. please use "help convert" for examples')

    # Jin
    def help_convert(self):
        print("""
            ***
            Interprets plantUML file to a python code file.                
            Syntax : convert <source file> <target folder>                
            Example : convert test_uml ./output
            ***
        """)

    # Jin
    def do_pep8(self, line):
        arg = self.file_path(line)
        if len(arg) == 1:
            formatter = Pep8Formatter()
            source = arg[0]
            dest = source + ".bak"
            shutil.copy(source, dest)
            formatter.pep8_format(source)
            print("Autopep8 complete! original file has been saved to "
                  + dest)
        else:
            print('invalid command. please use "help pep8" for examples')

    # Jin
    def help_pep8(self):
        print("""
            ***
            Fix target file with PEP8 standard. (re:pycodestyle)
            NOTE : original file will be automatically back up to
                   filename.extension.bak                
            Syntax : pep8 <source file>                
            Example : pep8 test_format.py
            ***            
        """)

    # Jin
    def do_greet(self, line):
        arg = self.file_path(line)
        if line:
            if len(arg) == 1:
                name = arg[0]
                print("Hello", name, ". How are you today?")
                print(datetime.datetime.now())
            else:
                print('invalid command. please use "help greet" for examples')
        else:
            print("You should tell me your name first \n"
                  "Example : >>> greet <your name>")

    # Jin
    def help_greet(self):
        print("""
            ***
            Welcoming user to the program and displays current time and date
            Syntax : greet <name>                
            Example : greet Jin
            ***            
        """)

    def help_source(self):
        print("""***
                 Update SOURCE file: source [source_file]
                 This file will be interpreted
                 ***
            """)

    def help_root(self, line):
        print("""***
                 Update ROOT directory: root [file_location]
                 Files will be created here
                 ***
            """)

    def postloop(self):
        print

    # Jin short cuts
    do_c = do_convert
    do_p = do_pep8
    do_g = do_greet
    do_q = do_quit


if __name__ == '__main__':

    if len(sys.argv) > 1:
        root_directory = sys.argv[1]
        source_file = sys.argv[2]
        x = Interpreter()
        x.add_file(source_file, root_directory)
        x.write_modules()
        print(f"Python files created in {root_directory}")
    else:
        Controller().cmdloop()
