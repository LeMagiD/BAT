import sys
sys.path.append(f"G:\\HSLU\\.Workspace")    # Dies global (in __init__ oder so) halten 
from my_libs.arger import argHandler_copyAndRename
from tqdm import tqdm
import pathlib
import shutil
# import glob
# import os

TESTFILE = "G:\\HSLU\\.Workspace\\P4_matri4x4\\val\\used_test_images.txt"
DEST = "G:\\HSLU\\.Workspace\\P4_matri4x4\\val\\.TUC_comparison"

def copy_and_rename(src_path, dest_path, new_name):
	
    # create new empty file
    new_path = f"{dest_path}/{new_name}"
    
    # Copy the file
    shutil.copyfile(src_path, new_path)

    
def main():
    args = argHandler_copyAndRename()
    parent = pathlib.Path(__file__).parent.absolute()
    
    copy_and_rename(args.source,args.destination,args.name)
    
    
    
if __name__=="__main__":
    # main()
    print("this file was not used")