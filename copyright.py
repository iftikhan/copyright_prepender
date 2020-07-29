import os
import sys


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: python copyright.py <dir> --copyright-file <copyright.txt> --file-extension <.ext>')
        print('To insert copyright in files.')
        sys.exit(1)

    directory = args[0]

    if len(args) != 5:
        print(
            "Please provide all required param i.e "
            "copyright.py <dir> --copyright-file <copyright.txt> --file-extension <.ext>")
        sys.exit(1)

    if args[1] != '--copyright-file':
        print(
            "Please provide all required param i.e "
            "copyright.py <dir> --copyright-file <copyright.txt> --file-extension <.ext>")
        sys.exit(1)

    # Get copyright text
    copyright_file = args[2]

    if args[3] != '--file-extension':
        print(
            "Please provide all required param i.e "
            "copyright.py <dir> --copyright-file <copyright.txt> --file-extension <.ext>")
        sys.exit(1)

    # Get extension
    ext = args[4]

    # get the content of directory.
    files = os.listdir(directory)

    if len(files) == 0:
        print("No file found with extension " + ext)
        sys.exit(1)

    if not os.path.isdir(directory):
        print('Not a valid directory!!!')
        print('usage: python copyright.py <dir> --file-extension <.tf>')
        sys.exit(1)

    try:
        fp = open(copyright_file, 'r')
        copyright_text = ''.join(fp.readlines())
        fp.close()
        add_copyright(directory, ext, copyright_text)
    except FileNotFoundError as er:
        print("Please add 'copyright.txt' file with Copyright content in it.")
        sys.exit(1)


def add_copyright(directory, ext, copyright_text):
    obj = os.listdir(directory)
    for f in obj:
        if os.path.isdir(directory + '/' + f):
            add_copyright(directory + '/' + f, ext, copyright_text)
        # operate only files
        if os.path.isfile(directory + '/' + f) and f.endswith(ext):
            fp = open(directory + '/' + f, 'r')
            lines = fp.readlines()
            fp.close()
            if copyright_text not in (''.join(lines)):
                lines.insert(0, ''.join(copyright_text) + '\n')
                fp = open(directory + '/' + f, 'r+')
                fp.writelines(lines)
                fp.close()
                print("Copyright added in " + f)
            else:
                print("Copyright already exist in " + directory + "/" + f)


if __name__ == '__main__':
    main()
