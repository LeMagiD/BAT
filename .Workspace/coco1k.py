from pycocotools.coco import COCO
import requests
from tqdm import tqdm
import os

path = "G:\\HSLU\\.Workspace\\data\\coco\\labels\\.all_coco"
annotation_file = [f"{path}\\person_keypoints_train2017.json",f"{path}\\person_keypoints_val2017.json" ]
out_dir = "G:\\HSLU\\.Workspace\\data\\coco\\images\\.all"


def main():
    for f in annotation_file:
        coco = COCO(f)
        cat_ids = coco.getCatIds(catNms=["person"])
        img_ids = coco.getImgIds(catIds=cat_ids)
        selected_img_ids = img_ids[:1000]
        
        os.makedirs(out_dir, exist_ok=True)

        for img_id in tqdm(selected_img_ids):
            img_info = coco.loadImgs(img_id)[0]
            img_url = img_info['coco_url']
            
            # Download the image
            img_data = requests.get(img_url).content
            img_path = os.path.join(out_dir, img_info['file_name'])
            
            with open(img_path, 'wb') as f:
                f.write(img_data)
            
            print(f"Downloaded: {img_info['file_name']}")
            

if __name__=="__main__":
    main()            