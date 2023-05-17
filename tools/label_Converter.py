import os

class_map = {'Car': 0, 'Van': 1, 'Truck': 2, 'Pedestrian': 3, 'Person_sitting': 4, 'Cyclist': 5, 'Tram': 6, 'Misc': 7}


def convert_kitti_to_yolo(kitti_file_path, yolo_file_path, img_width, img_height):
    with open(kitti_file_path, 'r') as kitti_file:
        data = kitti_file.readlines()

    with open(yolo_file_path, 'w') as yolo_file:
        for line in data:
            line = line.strip().split(' ')
            obj_name = line[0]
            if obj_name == 'DontCare':
                continue
            class_id = class_map[obj_name]
            xmin = int(float(line[4]))
            ymin = int(float(line[5]))
            xmax = int(float(line[6]))
            ymax = int(float(line[7]))
            x_center = (xmin + xmax) / 2.0
            y_center = (ymin + ymax) / 2.0
            width = xmax - xmin
            height = ymax - ymin
            x_center /= img_width
            y_center /= img_height
            width /= img_width
            height /= img_height
            yolo_file.write(f'{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n')

if __name__ == '__main__':
    kitti_dir = 'data_object_label_2/training/label_2'
    yolo_dir = 'data_object_label_2/training/label_YOLO'
    img_width = 1242
    img_height = 375
    for kitti_file in os.listdir(kitti_dir):
        if kitti_file.endswith('.txt'):
            kitti_file_path = os.path.join(kitti_dir, kitti_file)
            yolo_file_path = os.path.join(yolo_dir, kitti_file.replace('.txt', '.txt'))
            convert_kitti_to_yolo(kitti_file_path, yolo_file_path, img_width, img_height)
