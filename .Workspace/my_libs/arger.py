# Denis Ameti, December 2024, denis.ameti@stud.hslu.ch, https://github.com/LeMagiD
import argparse

def argHandler_imgImport():

    parser = argparse.ArgumentParser(
        prog='import_img.py',
        description='imports image from one spot to another ',
        epilog='end')

    parser.add_argument("-s", "--source",
                        help="image source ",
                        default=None)
    parser.add_argument("-d", "--destination",
                        help="image destination",
                        default=None)
    parser.add_argument("-i", "--imtype",
                        help="image type",
                        default="png")
    parser.add_argument("-cb", "--commonB",
                    help="common beginning in filename",
                    default="")
    parser.add_argument("-ca", "--commonA",
                    help="common ending in filename",
                    default="")

    args = parser.parse_args()
    return args


def argHandler_datasplit():

    parser = argparse.ArgumentParser(
        prog='datasplit.py',
        description='Creates a Project with the given dataset,' 
                    'with the corresponding percentages of those datasets and' 
                    'splits them into train/test/val sets',
        epilog='Default: -d None -dp [] -rs 44 -p default_project_name ')

    parser.add_argument("-d", "--dataset",
                        help="Dataset to be used, can be list or one of [TUC-A, TUC-B, TUC-C, coco, roboflow, ICARUS]",
                        default=None)
    parser.add_argument("-dp", "--datasetpercentages",
                        help="Percentage of Dataset to be used, must be a float list of size equal to dataset",
                        default=[])
    parser.add_argument("-rs", "--randomstate",
                        help="random state of training split",
                        type=int,
                        default=44)
    parser.add_argument("-p", "--project",
                        help="name of project",
                        type=str,
                        default="default_project_name")
    
    args = parser.parse_args()
    return args


def argHandler_train():

    parser = argparse.ArgumentParser(
                    prog='train.py',
                    description='Trains a model on a predetermined Dataset with the pretrained YOLO8m-pose model from ultralytics',
                    epilog='Defaults: \n -G 0 \n -E 50 \n -B 16 \n -W 8 \n -N None \n -M yolov8m-pose.pt \n -lr 0.01')

    parser.add_argument("-G", "--gpu", 
                        help = "which gpu to use, 0, 1 or cpu if no gpu",
                        type=int,
                        default = 0)
    parser.add_argument("-E", "--epochs", 
                        help = "how many epoch to train for",
                        default = 50)
    parser.add_argument("-B", "--batch", 
                        help = "batch size of training",
                        default = 16)
    parser.add_argument("-W", "--workers", 
                        help = "Number of worker threads for data loading",
                        default = 8)
    parser.add_argument("-N", "--name", 
                        help = "name of sub-directory where outputs are saved",
                        type=None,
                        default = None)
    parser.add_argument("-M", "--model", 
                        help = "type of model",
                        default = "yolov8m-pose.pt")  
    parser.add_argument("-lr", "--learnrate", 
                        help = "learnrate",
                        type=float,
                        default = 0.01)                        
    args = parser.parse_args()
    return args

def argHandler_predict():

    parser = argparse.ArgumentParser(
                    prog='predict.py',
                    description='predicts on a set of images with a specified model',
                    epilog='Defaults: -G 1 -W 4 -N None -M yolov8m-pose.pt -I .\\pred_img')

    parser.add_argument("-G", "--gpu", 
                        help = "which gpu to use, 0, 1 or cpu if no gpu",
                        type=int,
                        default = 1)
    parser.add_argument("-W", "--workers", 
                        help = "Number of worker threads for data loading",
                        default = 4)
    parser.add_argument("-N", "--name", 
                        help = "name of sub-directory where outputs are saved",
                        type=None,                        
                        default = None)
    parser.add_argument("-M", "--model", 
                        help = "type of model",
                        default = "yolov8m-pose.pt") 
    parser.add_argument("-I", "--images", 
                        help = "path to image folder",
                        default = ".\\pred_img")
                        
    args = parser.parse_args()
    return args


def argHandler_coco():

    parser = argparse.ArgumentParser(
                    prog='my_coco.py',
                    description='converts coco json annotation to yolo format',
                    epilog='end')

    parser.add_argument("-jd", "--json_dir", 
                        help = "Path to directory containing COCO dataset annotation files",
                        default = "G:\\HSLU\\.Workspace\\data\\coco\\labels\\.all_coco")
    parser.add_argument("-us", "--use_segments", 
                        help = "NO HELP" ,
                        default = False )
    parser.add_argument("-sd", "--save_dir", 
                        help = "path to directory where yolo files are saved to" ,
                        default = "G:\\HSLU\\.Workspace\\data\\coco\\labels\\.all" )
    parser.add_argument("--cls91to80", 
                        help = "NO HELP" ,
                        default = False)

                        
    args = parser.parse_args()
    return args

def argHandler_val():

    parser = argparse.ArgumentParser(
                    prog='validator.py',
                    description='validates a model on a predetermined Testset with a specific model',
                    epilog='Defaults: -G 1 -B 16 -N None -M yolov8m-pose.pt -y coco -s val')

    parser.add_argument("-G", "--gpu", 
                        help = "which gpu to use, 0, 1 or cpu if no gpu",
                        type=int,
                        default = 1)
    parser.add_argument("-B", "--batch", 
                        help = "batch size of training",
                        type=int,
                        default = 16)
    parser.add_argument("-N", "--name", 
                        help = "name of sub-directory where outputs are saved",
                        type=None,
                        default = None)
    parser.add_argument("-M", "--model", 
                        help = "type of model",
                        default = "yolov8m-pose.pt")  
    parser.add_argument("-y", "--yaml", 
                        help = "name of yaml-file that should be used, input without file ending ",
                        type=str,
                        default = "coco")  
    parser.add_argument("-s", "--split", 
                        help = "split to be used, either train, test or val",
                        type=str,
                        default = "val")                    
    args = parser.parse_args()
    return args
    
    
def argHandler_copyAndRename():

    parser = argparse.ArgumentParser(
        prog='import_img.py',
        description='imports image from one spot to another ',
        epilog='end')

    parser.add_argument("-s", "--source",
                        help="image source ",
                        type=str,
                        default=None)
    parser.add_argument("-d", "--destination",
                        help="image destination",
                        type=str,
                        default=None)
    parser.add_argument("-n", "--name",
                        help="name of new file",
                        type=str,
                        default=None)

    args = parser.parse_args()
    return args