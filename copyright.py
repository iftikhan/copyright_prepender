import os
import sys
from typing import List
import re


def main():
    args: List[str] = sys.argv[1:]
    supported_ext = ['.tf', '.yaml', '.hcl', '.css', '.py', '.yml']

    if not args:
        print('usage: python copyright.py <dir> --file-extension <.ext>')
        print('To insert copyright in files.')
        sys.exit(1)

    directory = args[0]

    if len(args) != 3:
        print("Please provide all required param i.e copyright.py <dir> --file-extension <.ext>")
        sys.exit(1)

    if args[1] != '--file-extension':
        print("Please provide all required param i.e copyright.py <dir> --file-extension <.ext>")
        sys.exit(1)

    # Get extension
    ext = args[2]

    if ext not in supported_ext:
        print(f"{ext} extension is not supported yet. Supported ext are {supported_ext}.")
        sys.exit(1)

    # get the content of directory.
    files = os.listdir(directory)

    if len(files) == 0:
        print(f"No file found with provided extension {ext}")
        sys.exit(1)

    if not os.path.isdir(directory):
        print('Not a valid directory!!!')
        print('usage: python copyright.py <dir> --file-extension <.tf>')
        sys.exit(1)
    
    # TODO: Plase update the regex as per new copytight content
    pattern = re.compile("^/?#+\n+#+ Copyright \(c\) [0-9]{4}-[0-9]{4} by Cisco Systems, Inc\.")
    try:

        fp = open('copyright.txt', 'r')
        copyright_text = ''.join(fp.readlines())
        fp.close()
        add_copyright(directory, ext, pattern, copyright_text)
    except Exception as ex:
        print("Please add 'copyright.txt' file with Copyright content in it.")
        sys.exit(1)


def add_copyright(directory, ext, pattern, copyright_text):
    obj = os.listdir(directory)
    for f in obj:
        if os.path.isdir(directory + '/' + f):
            add_copyright(directory + '/' + f, ext, pattern, copyright_text)
        # operate only files
        if os.path.isfile(directory + '/' + f) and f.endswith(ext):
            fp = open(directory + '/' + f, 'r')
            lines = fp.readlines()
            fp.close()
            if not pattern.match(''.join(lines)):
                lines.insert(0, ''.join(copyright_text) + '\n')
                fp = open(directory + '/' + f, 'r+')
                fp.writelines(lines)
                fp.close()
                print(f'Copyright added in {f}')
            else:
                print(f"Copyright already exist in {directory + '/' + f}")


if __name__ == '__main__':
    main()
