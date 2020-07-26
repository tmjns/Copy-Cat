import pyperclip
import sys

class Copy:
    '''
        Python class to copy text from your clipboard into a new file.
    '''
        
    def __init__(self, filename, method):
        self.filename = open(filename, method)
        
    def __enter__(self):
        return self.filename
    
    @staticmethod
    def copy_clip():
        data = pyperclip.paste()
        pyperclip.waitForNewPaste()
        return data
    
    def __exit__(self, type, value, traceback):
        self.filename.close()


if __name__ == '__main__':
    try:
        with Copy('file.txt', 'w') as f:
            while True:
                f.write(Copy.copy_clip())
                f.write('\n' + '---' + '\n')
    except KeyboardInterrupt:
        print(sys.stderr, '\nExiting by user request.\n')
        sys.exit(0)