import sys
sys.path.append(f"G:\\HSLU\\.Workspace")  
from my_libs.arger import argHandler_predict
from ultralytics import YOLO
import argparse
import pathlib
import glob
import os



def main():
    args = argHandler_predict()
    parent = str(pathlib.Path(__file__).parent.absolute())
    saveto = f'{parent}\\predict\\{args.name}'


    model = YOLO(f"{parent}\\{args.model}")
    img = glob.glob(f"{parent}\\pred_img\\*")
    
    results = model.predict(source = img, device = args.gpu, save = True, project = parent, name = saveto )


if __name__ == "__main__":
    main()