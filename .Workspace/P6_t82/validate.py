import sys
sys.path.append(f"G:\\HSLU\\.Workspace")    # Dies global (in __init__ oder so) halten 
from my_libs.arger import argHandler_val
from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionValidator
import pathlib

def main() -> None:
    args = argHandler_val()
    parent = pathlib.Path(__file__).parent.absolute()
    pparent = parent.parent
    saveto = f'{str(parent)}\\val\\{args.name}'
    
    model = YOLO(f"{str(parent)}\\{args.model}")
    data = f"{str(parent)}\\{args.yaml}.yaml"
    
    results = model.val(data=data, device = args.gpu, batch = args.batch, save_json = True, split=args.split, project = str(parent), name = saveto )

    
    # arguments = dict(model=model, data=data)
    # validator = DetectionValidator(args=arguments)
    # validator()

    
if __name__ == "__main__":
    main()