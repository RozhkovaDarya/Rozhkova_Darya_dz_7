import os
from pathlib import Path



dir_ = os.path.abspath(os.curdir)


p = Path(f'{dir_}/text2/text3/text4/text5/text6')


p.mkdir(parents=True, exist_ok=True)


def rec():
    for i in os.listdir():
        if Path(i).is_file():
            print('file-',i)
        else:
            print('dir-',i)
            os.chdir(i)
            rec()
    os.chdir('..')
    return

#rec()


for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('path', dirpath)
    print('dirs', dirnames)
    print('filenames', filenames)
    print()