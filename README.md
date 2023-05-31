# You Never See The Carriage (YNSTC)
## KITTI dataset
The KITTI dataset is a widely used benchmark dataset for autonomous driving research, particularly in the area of 2D object detection. It stands for "Karlsruhe Institute of Technology and Toyota Technological Institute" and was created by a collaboration between the two institutions.

![alt text](https://www.cvlibs.net/datasets/kitti/results/e110715461db375dfdbf3d2cb8c8daad73ce0022/image_2/0000000000.png)

The dataset contains diverse scenarios captured from a moving vehicle, including urban street scenes, highways, and rural areas, covering different weather conditions such as sunny, rainy, and cloudy. It comprises a large number of annotated images and point clouds, making it suitable for various computer vision tasks, including object detection, tracking, and scene understanding.

In terms of 2D object detection, the KITTI dataset provides detailed annotations for several object categories, which are: cars, pedestrians, cyclists, person_sitting, misc, truck, tram, and van. The annotations include precise bounding box coordinates around the objects of interest, as well as labels indicating the class of each object. 
The KITTI dataset annotation format for 2D object detection follows a specific structure and is represented in plain text files. Each annotation file corresponds to an image in the dataset and contains information about the objects present in the image. Here is an example of the KITTI annotation format:

"Object Type | Truncated | Occluded | Alpha | Bounding Box (2D) | Dimensions (3D) | Location (3D) | Rotation Yaw | Score"

The dataset also includes various additional information, such as camera calibration parameters, timestamps, and vehicle trajectories, which can be valuable for tasks like camera pose estimation and motion analysis.

KITTI has become a popular benchmark for evaluating the performance of 2D object detection algorithms due to its real-world nature and comprehensive annotations. Researchers and developers often use the dataset to compare the accuracy and efficiency of different detection methods, and it has contributed to significant advancements in the field of autonomous driving.

Although many Deep Learning models have been used on the KITTI dataset to evaluate its performance, YOLOv8 have not been tested on it yet.


## YOLOv8

YOLOv8 is the lastest version of You Only Look Once (YOLO). You can see the architecture below:

<img src="https://user-images.githubusercontent.com/27466624/239739723-57391d0f-1848-4388-9f30-88c2fb79233f.jpg" width="200">
## Optimization
## Final Results
## Conclusion
