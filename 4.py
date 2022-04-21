import shutil
from pathlib import Path
import os


dir_ = os.path.abspath(os.curdir)

#создаем папки в папках, но начальная папка - dir_:
p = Path(f'{dir_}/text2/text3/text4/text5/text6')

p.mkdir(parents=True, exist_ok=True)

p = Path(f'{dir_}/test_copy')


p.mkdir(parents=True, exist_ok=True)


shutil.copytree('text2', 'test_copy', dirs_exist_ok=True)


shutil.copyfile('1.py', '1_copy.py')




#shutil.rmtree('text2')
