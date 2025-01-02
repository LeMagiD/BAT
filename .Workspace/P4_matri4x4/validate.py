import sys
sys.path.append(f"G:\\HSLU\\.Workspace")    # Dies global (in __init__ oder so) halten 
from my_libs.arger import argHandler_val
from ultralytics import YOLO
import pathlib


def main() -> None:
    args = argHandler_val()

    parent = pathlib.Path(__file__).parent.absolute()
    pparent = parent.parent
    
    saveto = f'{str(parent)}\\val\\{args.name}'
    
    model = YOLO(f"{str(pparent)}\\data\\{args.model}")
    data = f"{str(parent)}\\{args.yaml}"
    
    print(f'Starting validation with following arguments:\nGPU: {args.gpu}\nBatchsize: {args.batch}\nModel: {args.model}\nData:{args.yaml}\nSaving to: {saveto}')

    results = model.val(data = data, batch = int(args.batch), device = int(args.gpu), project = parent, name = saveto)

if __name__ == "__main__":
    main()