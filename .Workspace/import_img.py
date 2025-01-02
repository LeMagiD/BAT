from my_libs.arger import argHandler_imgImport
from tqdm import tqdm
import shutil
import glob


def import_img():
    args = argHandler_imgImport()
    source, imtype, dest, commonB, commonA = args.source, args.imtype, args.destination, args.commonB,args.commonA

    images = [img for img in glob.glob(f"{source}/{commonB}*{commonA}.{imtype}")]

    if source == None or dest == None:
        return "no source and/or destination! use -s and -d respectively, or -h for help if in a terminal"

    for img in tqdm(images):
        shutil.copy(img, f"{dest}")
    return "success"


def main():
    print(import_img())


if __name__ == "__main__":
    main()