echo validating TUC
echo timestamp: %time%
python P6_t82\validate.py -G 1 -N TUC_t82e2 -M "runs\t82e2\weights\best.pt" -y TUC -s test
python P6_t82\validate.py -G 1 -N TUC_t82e3 -M "runs\t82e3\weights\best.pt" -y TUC -s test
python P6_t82\validate.py -G 1 -N TUC_t82e5 -M "runs\t82e5\weights\best.pt" -y TUC -s test
python P6_t82\validate.py -G 1 -N TUC_t82e7 -M "runs\t82e7\weights\best.pt" -y TUC -s test
echo validating coco
echo timestamp: %time%
python P6_t82\validate.py -G 1 -N coco_t82e2 -M "runs\t82e2\weights\best.pt" -y coco -s test
python P6_t82\validate.py -G 1 -N coco_t82e3 -M "runs\t82e3\weights\best.pt" -y coco -s test
python P6_t82\validate.py -G 1 -N coco_t82e5 -M "runs\t82e5\weights\best.pt" -y coco -s test
python P6_t82\validate.py -G 1 -N coco_t82e7 -M "runs\t82e7\weights\best.pt" -y coco -s test