import sys
sys.path.append(f"G:\\HSLU\\.Workspace")    # Dies global (in __init__ oder so) halten 
from my_libs.arger import argHandler_train
from ultralytics import YOLO
import pathlib


def main() -> None:
    args = argHandler_train()

    parent = pathlib.Path(__file__).parent.absolute()
    pparent = parent.parent
    
    saveto = f'{str(parent)}\\runs\\{args.name}'
    
    model = YOLO(f"{str(pparent)}\\data\\{args.model}")
    data = f"{str(parent)}\\data.yaml"
    
    freeze_N = 53 # Anzahl Layer des Backbone, gemäss Masterarbeit die beste Anz. für Freeze
    print(f'Starting Training with following arguments:\nGPU: {args.gpu}\nEpochs: {args.epochs}\nBatchsize: {args.batch}\nWorkers: {args.workers}\n saving to: {saveto}')

    results = model.train(data = data, epochs = int(args.epochs), imgsz = 640, freeze = range(freeze_N), batch = int(args.batch), workers = int(args.workers), device = int(args.gpu), project = parent, name = saveto)

if __name__ == "__main__":
    main()