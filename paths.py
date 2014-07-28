'''
Created on May 17, 2014

@author: dave
'''
import sys, os

#BASE_PATH='C:\NatLink\NatLink\MacroSystem\\'
BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\"
SETTINGS_PATH = BASE_PATH + "data\\settings.json"
ELEMENT_JSON_PATH = BASE_PATH + "data\\element.json"
SAVED_CLIPBOARD_PATH = BASE_PATH + "data\\clipboard.json"

#REMOTE_DEBUGGER_PATH is the folder in which pydevd.py can be found
REMOTE_DEBUGGER_PATH ="D:\PROGRAMS\NON_install\eclipse\plugins\org.python.pydev_3.4.1.201403181715\pysrc"

NIRCMD_PATH=r"C:\NatLink\NatLink\MacroSystem\exe\nircmd\nircmd.exe"
MMT_PATH =r"C:\NatLink\NatLink\MacroSystem\exe\MultiMonitorTool\MultiMonitorTool.exe"

JAVA_CONFIG_PATH = "C:\NatLink\NatLink\MacroSystem\languages\configjava.txt"
PYTHON_CONFIG_PATH = "C:\NatLink\NatLink\MacroSystem\languages\configpython.txt"
HTML_CONFIG_PATH = "C:\NatLink\NatLink\MacroSystem\languages\confightml.txt"
PASCAL_CONFIG_PATH = "C:\NatLink\NatLink\MacroSystem\languages\configpascal.txt"
ALPHABET_CONFIG_PATH = "C:\NatLink\NatLink\MacroSystem\languages\configalphabet.txt"

MEDIA_PATH = r"C:\NatLink\NatLink\MacroSystem\media"

GRID_PATH=BASE_PATH+"exe\\custom_grid\\CustomGrid.exe"

def get_base():
    global BASE_PATH
    return BASE_PATH

def get_settings_path():
    global SETTINGS_PATH
    return SETTINGS_PATH

def get_element_json_path():
    global ELEMENT_JSON_PATH
    return ELEMENT_JSON_PATH

def get_saved_clipboard_path():
    global SAVED_CLIPBOARD_PATH
    return SAVED_CLIPBOARD_PATH

def get_nircmd():
    global NIRCMD_PATH
    return NIRCMD_PATH

def get_mmt():
    global MMT_PATH
    return MMT_PATH

def get_all_language_configs():
    global JAVA_CONFIG_PATH
    global PYTHON_CONFIG_PATH
    global HTML_CONFIG_PATH
    return [JAVA_CONFIG_PATH, PYTHON_CONFIG_PATH, HTML_CONFIG_PATH, 
            PASCAL_CONFIG_PATH, ALPHABET_CONFIG_PATH]

def get_media_path():
    global MEDIA_PATH
    return MEDIA_PATH

def get_grid():
    global GRID_PATH
    return GRID_PATH

if not REMOTE_DEBUGGER_PATH in sys.path:
    sys.path.append(REMOTE_DEBUGGER_PATH)