import shutil
from pathlib import Path
import os


dir_path = os.path.join('my_project', 'settings')
if not os.path.exists(dir_path):
  os.makedirs(dir_path)

dir_path = os.path.join('my_project', 'mainapp', 'templates', 'mainapp')
if not os.path.exists(dir_path):
  os.makedirs(dir_path)

dir_path = os.path.join('my_project', 'authapp', 'templates', 'authapp')
if not os.path.exists(dir_path):
  os.makedirs(dir_path)


dir_path = os.path.join('my_project_copy')
if not os.path.exists(dir_path):
  os.makedirs(dir_path)

shutil.copytree('my_project/authapp', 'my_project_copy',  dirs_exist_ok=True)

shutil.copytree('my_project/mainapp', 'my_project_copy',  dirs_exist_ok=True)