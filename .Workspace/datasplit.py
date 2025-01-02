# Denis Ameti, December 2024, denis.ameti@stud.hslu.ch, https://github.com/LeMagiD

from sklearn.model_selection import train_test_split
from my_libs.arger import argHandler_datasplit
from tqdm import tqdm
import pathlib
import shutil
import glob
import os

''' 
File description:
    Import Data from ".all" Folder of the respective Dataset to their train/test/val folder
'''

# paths for images from different sources
PARENT = pathlib.Path(__file__).parent.absolute()
PATH = f'{PARENT}\\data'
POSSIBLE_DATASETS = ["TUC-A", "TUC-B", "TUC-C", "roboflow", "ICARUS", "coco"]
LIST_TXT = ["train", "test", "val"]

def reset_folder(folderpath: str, filetype: str = "jpg"):

    for d in POSSIBLE_DATASETS:
        f = glob.glob(f"{folderpath}\\{d}\\images\\*")
        img_folder = [file for file in f if os.path.isdir(file) and not os.path.basename(file).startswith(".")]
        if img_folder == []:
            continue

        la = glob.glob(f"{folderpath}\\{d}\\labels\\*")
        lab_folder = [file for file in la if os.path.isdir(file) and not os.path.basename(file).startswith(".")]
        
        folders = [img_folder, lab_folder]
        fn = ["images", "labels"]

        for i, folder in enumerate(folders):
            print(f"\n\tremoving folder {d} \u2192 {fn[i]}")
            for f in tqdm(folder):
                shutil.rmtree(f)


def create_workspace(project: str, random_state: int = 44, datasets: list = None, percent: list = [], img_type: str = "jpg", create_new_folder: bool = True) -> None:
    """
    Creates a Workspace, which is compatible with the data.yaml file.
    It works as follows:
    1. Delets all local train/test/val Folders and creates new ones (empty)
    2. Splits images as follows: 0.48 train, 0.32 val & 0.2 test
    3. imports splited images to the local train/test/val Folder
    4. writes a .txt file to ./data/constellations/ with the current split of the images
    parameter:
        project: name of project for this specific dataset
        random_state: random seed which is used for the train/test/val split
        datasets: the datasets that are to be used, one or multiple of ["TUC-A", "TUC-B", "TUC-C", "roboflow", "ICARUS"]
        percent: percentages of datasets to be used (in decimal). list of floats without brackets, for example: "0.18,0.22,0.85"
        img_type: type of image to be used
    returns:
        None
    """

    reset_folder(PATH)
    if create_new_folder:
        create_yaml(PARENT, project, datasets)

    # Gets all the images from the used dataset folders and splits them into train, test and validation
    for idx, dataset in enumerate(datasets):
        dataset_path = f'{PATH}\\{dataset}'
        if dataset in ["TUC-A", "TUC-B", "TUC-C"]:
            img_type = "png"
        else:
            img_type = "jpg"
        
        images = [img for img in glob.glob(f"{dataset_path}\\images\\.all\\*.{img_type}")]
        
        if percent == []:   # if no percentages given, use 100% of every dataset
            for i in len(datasets):
                percent.append(1.0)
        elif type(percent[0]) != float:
            percent = percentages_to_float(percent)
        print(f"Debugging:\npercent: {percent} \npercent[idx]: {percent[idx]} \nlen(images): {len(images)}")
        images = images[0:int(percent[idx]*len(images))]

        # Split all Img into train/val & test (80/20)
        train_img_tot, test_img = train_test_split(images, test_size=0.2, random_state=random_state)
        # Split remaining 80% into train & val (60/40)
        train_img, val_img = train_test_split(train_img_tot, test_size=0.4, random_state=random_state)

        img_list = [train_img, test_img, val_img]

        os.makedirs(f"{dataset_path}\\images\\train", exist_ok=True) #exist_ok not really needed as the folder are removed with reset_folder()
        os.makedirs(f"{dataset_path}\\images\\val", exist_ok=True)
        os.makedirs(f"{dataset_path}\\images\\test", exist_ok=True)

        print(f"\n\tcopying images to {dataset}'s train, test and val folder...")
        for i, IMG in  enumerate(tqdm(img_list)):
            for img in IMG:
                shutil.copy(img, f"{dataset_path}\\images\\{LIST_TXT[i]}")
        writer(img_list, LIST_TXT, project, dataset, random_state)

        # D:/HSLU/.Workspace/data/TUC/images
        train_label = [f"{dataset_path}\\labels\\.all\\{label[len(f'{dataset_path}\\images\\.all')+1:-len(img_type)]}txt" for label in train_img]
        val_label = [f"{dataset_path}\\labels\\.all\\{label[len(f'{dataset_path}\\images\\.all')+1:-len(img_type)]}txt" for label in val_img]
        test_label = [f"{dataset_path}\\labels\\.all\\{label[len(f'{dataset_path}\\images\\.all')+1:-len(img_type)]}txt" for label in test_img]
        
        os.makedirs(f"{dataset_path}\\labels\\train", exist_ok=True)
        os.makedirs(f"{dataset_path}\\labels\\val", exist_ok=True)
        os.makedirs(f"{dataset_path}\\labels\\test", exist_ok=True)

        lab_list = [train_label, test_label, val_label]
        print(f"\n\tcopying labels to {dataset}'s train, test and val folder")
        for i, LAB in enumerate(tqdm(lab_list)):
            for  lab in LAB:
                shutil.copy(lab, f"{dataset_path}\\labels\\{LIST_TXT[i]}")


def writer(l: list, ln: list, project: str, dataset: str, randomState: int, dest: str = f'{PARENT}\\data\\constellations') -> None:
    # Write current image (train/test/val split) constellation to file to be able to recreate training
    filename = f"constellation_{dataset}.txt"
    c = 0
    # TODO Name der Bilder in txt ohne ganzen Pfad hineinschreiben
    if not os.path.exists(f'{dest}/{project}'):
        os.makedirs(f'{dest}/{project}', exist_ok=True)

    while os.path.exists(f'{dest}/{project}/{filename}'):
        c += 1
        filename = f'constellation_{dataset}{c}.txt'

    print(f"\n\twriting constellation to file \"{filename}\"")
    with open(f'{dest}\\{project}\\{filename}', "w") as f:
        f.write(f'Random state: {randomState}\n')
        for i, IMG in enumerate(tqdm(l)): 
            f.write(f'{ln[i]}:\n')
            for item in (IMG):
                f.write(f'\t{item[len(f"{PARENT}\\{dataset}\\images\\.all\\"):]}\n')
            

def check_datasets(datasets) -> tuple[list, int]: # could be left out if type=list is used in arger.argHandler_datasplit(), to lazy to change now
    try:
        sets = datasets.split(",")
        for i, s in enumerate(sets):
            print(f"set {i+1}: \"{s}\"")
            if s not in POSSIBLE_DATASETS:
                return [], 2
    except:
        return [], 1
    return sets, 0
 
def create_yaml(path, name, datasets):
'''
Creates a new project Folder with prefix Px_name with x being a number not used yet and
creates the data.yaml file with the corresponding datasets
'''
    prefix = f'P1_'
    c = 1
    dir = glob.glob(f'{path}/{prefix}*')

    if dir == []: # empty dir does not work with os.path.isdir(dir[0]) check, could be resolved with try-except
        dir = ['placeHolderSoItWorks']

    while os.path.isdir(dir[0]) and os.path.basename(dir[0]).startswith(prefix):
        c += 1
        prefix = f'P{c}_'
        dir = glob.glob(f'{path}/{prefix}*')

        if dir == []:
            dir = ['placeHolderSoItWorks']
            continue

    set_tr = [f"data/{d}/images/train" for d in datasets]
    set_va = [f"data/{d}/images/val" for d in datasets]
    set_te = [f"data/{d}/images/test" for d in datasets]

    if not os.path.exists(f'{path}\\{prefix}{name}'):
        os.makedirs(f'{path}\\{prefix}{name}')

    with open(f'{path}\\{prefix}{name}\\data.yaml', "w") as f:
        f.write(f'''# train and val data as 1) directory: path/images/, 2) file: path/images.txt, or 3) list: [path1/images/, path2/images/] 
path:  {path}
train: {set_tr}
val: {set_va}
test: {set_te}

# Keypoints
kpt_shape: [17,3]

# Wird  verwendet, falls das Bild gespiegelt wird. Dann ist zB elbowLeft gespiegelt = elbowRight
flip_idx: [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]

# Class Dict
names:
    0: person
''')
            
def percentages_to_float(percent:str):
    percentages = []
    percent = percent.split(",")
    for p in percent:
        percentages.append(float(p))
    return percentages
    
    

def main() -> None:
    args = argHandler_datasplit()
    d, d_ok = check_datasets(args.dataset)
    if d_ok != 0:
        return f"failed dataset selection, error [{d_ok}]"

    create_workspace(args.project, random_state=args.randomstate, datasets=d, percent = args.datasetpercentages)
    return "success"


if __name__ == "__main__":
    print(main())
