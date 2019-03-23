# from autopep8 import fix_code
# from autopep8 import fix_file
import subprocess


# Jin
class Pep8Formatter:
    @staticmethod
    def pep8_format(line):
        # print(fix_code('x=       123\n'))
        # print(fix_file(line))
        try:
            # bash = "autopep8 --in-place --aggressive --aggressive " + line
            # import subprocess
            # process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
            # output, error = process.communicate()
            # print(output)
            subprocess.call("autopep8 --in-place --aggressive --aggressive " + line)
        except FileNotFoundError:
            print("Requested file is not available")
        except Exception as e:
            print(e)
