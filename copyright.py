################################################################################
# Copyright (c) 2019-2020 by My Systems, Inc.
#
# Restricted Rights Legend
#
# Use, duplication, or disclosure is subject to restrictions as set forth in
# subparagraph (c) of the Commercial Computer Software - Restricted Rights
# clause at FAR sec. 52.227-19 and subparagraph (c) (1) (ii) of the Rights in
# Technical Data and Computer Software clause at DFARS sec. 252.227-7013.
#
# My Systems, Inc.
# 170 West Tasman Drive
# San Jose, California 95134-1706
#
################################################################################

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

    pattern = re.compile("^/?#+\n+#+ Copyright \(c\) [0-9]{4}-[0-9]{4} by My Systems, Inc\.")

    copyright_text = "################################################################################\n" \
                     "# Copyright (c) 2019-2020 by My Systems, Inc.\n" \
                     "#\n" \
                     "# Restricted Rights Legend\n" \
                     "#\n" \
                     "# Use, duplication, or disclosure is subject to restrictions as set forth in\n" \
                     "# subparagraph (c) of the Commercial Computer Software - Restricted Rights\n" \
                     "# clause at FAR sec. 52.227-19 and subparagraph (c) (1) (ii) of the Rights in\n" \
                     "# Technical Data and Computer Software clause at DFARS sec. 252.227-7013.\n" \
                     "#\n" \
                     "# My Systems, Inc.\n" \
                     "# 170 West Tasman Drive\n" \
                     "# San Jose, California 95134-1706\n" \
                     "#\n" \
                     "################################################################################\n"
    add_copyright(directory, ext, pattern, copyright_text)


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
                lines.insert(0, copyright_text + '\n')
                fp = open(directory + '/' + f, 'r+')
                fp.writelines(lines)
                fp.close()
                print(f'Copyright added in {f}')
            else:
                print(f"Copyright already exist in {directory + '/' + f}")


if __name__ == '__main__':
    main()
