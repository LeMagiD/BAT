from sklearn.model_selection import train_test_split
from xml.dom import minidom
from tqdm import tqdm
import shutil
import glob
import cv2 
import os

GET_LABEL_LIST = False


src_path_img_TUC = "C:/Users/xxx/Hochschule Luzern/Studierendenarbeiten - TM - HS2024_IET_BAT_Ameti - HS2024_IET_BAT_Ameti/Daten/TUC/001.00.300.02/7876"
src_path_img_ICA = "C:/Users/xxx/Hochschule Luzern/Studierendenarbeiten - TM - HS2024_IET_BAT_Ameti - HS2024_IET_BAT_Ameti/Daten/ICARUS/images"
dst_path_img = "./TUC/images"

src_path_labels_TUC = "./data/all_labels/7876B"
src_path_labels_ICA = ""
dst_path_labels = "./TUC/labels"


# Removes all files or only those of a certain type from a folder
def reset_folder(folderpath:str, filetype:str, rm_all:bool = False):
    if rm_all==True:
        folder = glob.glob(f"{folderpath}/*")
    elif rm_all==False:
        folder = glob.glob(f"{folderpath}/*.{filetype}")

    for file in folder:
        os.remove(file)



def create_workspace(source_img:str, source_label:str, img_type:str="png", destination:str="./mytestworkspace", random_state = 44, needLetter:bool = False, letter = "B"):
    '''
    imports image and label files from individual sources to a common destination, splits the data into train/test/val while doing so 
    parameter: 
        source_img: the source path of the image folder. images need to be in a "{i:03d}_img.png" format
        source_label: the source path of the label folder. label files need to be in a "{i:03d}_img.txt" format and use the yolov8 format
        img_type: type of image. png, jpg or whatever works with ultralytics
    returns:
        Nothing
        
    '''

    # ACHTUNG: Wenn die gleichen Bildernamen aus verschiedenen Ordnern genommen werden (zB 7876*) werden diese überschrieben!
    # Gets all the images from one folder and splits them into train, test and validation
    if needLetter == True:
        images = [img for img in glob.glob(f"{source_img}{letter}/*_img.{img_type}")]
    elif needLetter == False:
        images = [img for img in glob.glob(f"{source_img}/*.{img_type}")]

    train_img_tot, test_img = train_test_split(images, test_size = 0.2, random_state = random_state) # Split all Img into train/val & test (80/20)
    train_img, val_img = train_test_split(train_img_tot, test_size = 0.4, random_state = random_state)   # Split remaining 80% into train & val (60/40)


    os.makedirs(f"{destination}/images/train", exist_ok=True)
    os.makedirs(f"{destination}/images/val", exist_ok=True)
    os.makedirs(f"{destination}/images/test", exist_ok=True)

    print(f"copying images to train, test and val folder...")
    print("train:")
    for img in tqdm(train_img):
        shutil.copy(img, f"{destination}/images/train")
    print("val:")
    for img in tqdm(val_img):
        shutil.copy(img, f"{destination}/images/val")
    print("test:")
    for img in tqdm(test_img):
        shutil.copy(img, f"{destination}/images//test")

    
    train_label = [f"{source_label}/{label[-11:-len(img_type)]}txt" for label in train_img]
    val_label = [f"{source_label}/{label[-11:-len(img_type)]}txt" for label in val_img]
    test_label = [f"{source_label}/{label[-11:-len(img_type)]}txt" for label in test_img]

    os.makedirs(f"{destination}/labels/train", exist_ok=True)
    os.makedirs(f"{destination}/labels/val", exist_ok=True)
    os.makedirs(f"{destination}/labels/test", exist_ok=True)

    print(f"copying labels to train, test and val folder")
    print("train:")
    for label in tqdm(train_label):
        shutil.copy(label, f"{destination}/labels/train")
    print("val:")
    for label in tqdm(val_label):
        shutil.copy(label, f"{destination}/labels/val")
    print("test:")
    for label in tqdm(test_label):
        shutil.copy(label, f"{destination}/labels/test")

    shutil.copy("./yolov8m-pose.pt", f"{destination}/")



def png_to_jpg(image:str='000_img.png'):
    img = cv2.imread(image)
    cv2.imwrite('000_img.jpg', img)


def main():
    # import_img_and_labels("./data/example_images","./data/example_images") # testing 
    
    if False: # to not accidantally run this again and overwrite stuff - synthetic images
        create_workspace(src_path_img_TUC,"./data/all_labels/7876A", destination="./GPU-TUC-ICA/A", needLetter=True, letter="A")
        create_workspace(src_path_img_TUC,"./data/all_labels/7876B", destination="./GPU-TUC-ICA/B", needLetter=True, letter="B")
        create_workspace(src_path_img_TUC,"./data/all_labels/7876C", destination="./GPU-TUC-ICA/C", needLetter=True, letter="C")
    if False: # to not accidantally run this again and overwrite stuff - real images
        create_workspace(src_path_img_ICA, src_path_labels_ICA, destination = "./GPU-TUC-ICA/", img_type="jpg")

    # Nur dafür verwendet um zu kontrollieren, wieviele verschiedene labels in den xml Files waren
    if GET_LABEL_LIST:
        labels = []

        xmldoc = minidom.parse("./000_keypoints.xml")
        points = xmldoc.getElementsByTagName('points')
        for point in points:
            label = point.getAttribute('label')
            if label not in labels:
                labels.append(label)

        print(f'nr of labels: {len(labels)}')
        print(labels)

if __name__=='__main__':
    main()
