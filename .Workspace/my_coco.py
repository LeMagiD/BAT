from my_libs.general_json2yolo import convert_coco_json
from my_libs.converter_ULcoco import convert_coco
from my_libs.arger import argHandler_coco

def main():
    args = argHandler_coco()
    # convert_coco_json(json_dir=args.json_dir, save_to_dir=args.save_dir)
    convert_coco(labels_dir="G:\\HSLU\\.Workspace\\data\\coco\\labels\\.all_coco",
                save_dir="G:\\HSLU\\.Workspace\\data\\coco\\labels\\.all",
                use_keypoints=True)


if __name__ == "__main__":
    main()
    