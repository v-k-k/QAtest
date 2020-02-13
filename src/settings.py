from pathlib import Path
import os


"""
Defining the operating system and current path to the project
"""

PROJECT_PATH = str(Path(os.getcwd()).parents[0])
DRIVERS_PATH = os.path.join(PROJECT_PATH, 'drivers')
SYSTEM = os.name

FireFoxDriver = ChromeDriver = ''

if SYSTEM == 'nt':
    FireFoxDriver = os.path.join(DRIVERS_PATH, 'win\geckodriver.exe')
    ChromeDriver = os.path.join(DRIVERS_PATH, 'win\chromedriver.exe')
elif SYSTEM == 'posix':
    FireFoxDriver = os.path.join(DRIVERS_PATH, 'linux/geckodriver')
    ChromeDriver = os.path.join(DRIVERS_PATH, 'linux/chromedriver')

