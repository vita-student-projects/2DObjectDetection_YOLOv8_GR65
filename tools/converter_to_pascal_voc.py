import os

def convert_kitti_to_voc(kitti_file_path, voc_file_path):
    with open(kitti_file_path, 'r') as kitti_file:
        data = kitti_file.readlines()

    objects = []
    for line in data:
        line = line.strip().split(' ')
        obj_name = line[0]
        if obj_name == 'DontCare':
            continue
        xmin = int(float(line[4]))
        ymin = int(float(line[5]))
        xmax = int(float(line[6]))
        ymax = int(float(line[7]))
        objects.append((obj_name, xmin, ymin, xmax, ymax))

    with open(voc_file_path, 'w') as voc_file:
        voc_file.write('<annotation>\n')
        voc_file.write('<folder>mydata-voc</folder>\n')
        voc_file.write(f'<filename>{os.path.basename(kitti_file_path).replace(".txt", ".png")}</filename>\n')
        voc_file.write('<source>\n')
        voc_file.write('<database>Unknown</database>\n')
        voc_file.write('</source>\n')
        voc_file.write('<size>\n')
        voc_file.write('<width>1242</width>\n')
        voc_file.write('<height>375</height>\n')
        voc_file.write('<depth>3</depth>\n')
        voc_file.write('</size>\n')
        voc_file.write('<segmented>0</segmented>\n')
        for obj in objects:
            voc_file.write('<object>\n')
            voc_file.write(f'<name>{obj[0]}</name>\n')
            voc_file.write('<pose>Unspecified</pose>\n')
            voc_file.write('<truncated>0</truncated>\n')
            voc_file.write('<difficult>0</difficult>\n')
            voc_file.write('<bndbox>\n')
            voc_file.write(f'<xmin>{obj[1]}</xmin>\n')
            voc_file.write(f'<ymin>{obj[2]}</ymin>\n')
            voc_file.write(f'<xmax>{obj[3]}</xmax>\n')
            voc_file.write(f'<ymax>{obj[4]}</ymax>\n')
            voc_file.write('</bndbox>\n')
            voc_file.write('</object>\n')
        voc_file.write('</annotation>\n')

if __name__ == '__main__':
    kitti_dir = 'data_object_label_2/training/label_2'
    voc_dir = 'data_object_label_2/training/label_VOC'
    for kitti_file in os.listdir(kitti_dir):
        if kitti_file.endswith('.txt'):
            kitti_file_path = os.path.join(kitti_dir, kitti_file)
            voc_file_path = os.path.join(voc_dir, kitti_file.replace('.txt', '.xml'))
            convert_kitti_to_voc(kitti_file_path, voc_file_path)
