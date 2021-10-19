# Deep_Learning_Based_Safty_Light_Curtain

This project aims to increase the safety level when the Industrial Robots are operating. This deep learning-based safety light curtain is a kind of safety device for the industrial robot that can form a virtual protection scene to avoid danger. Creating an object detection that detects the human which across the virtual protection point and surroundings to protect people and machines from damage.

**1. Demo and Layout**
---------------------------
# 1.1. Environment Configuration
![image](https://github.com/Summer-Lo/Deep_Learning_Based_Safty_Light_Curtain/blob/main/images/environment_configuration_v1.jpeg)

In this project, the hardware device is a combination of Nvidia Jetson Nano and CSI camera.

# 1.2. Object Detection Performance
![image](https://github.com/Summer-Lo/Deep_Learning_Based_Safty_Light_Curtain/blob/main/video/Light_curtain_demo.gif)

**2. Project Workflow**
---------------------------
![image](https://github.com/Summer-Lo/Deep_Learning_Based_Safty_Light_Curtain/blob/main/images/flowchart.png)

This project involves SSD-MobileNet version 1 to achieve the object detection. Mobilenet is the base network for feature extraction. Meanwhile, SSD was used to perform classification and boundary box regression. Moreover, TensorRT is used to speed up the operation. If the "human" is detected, the program return "Danger!!!" to remain the workers for avoiding accident.


**3. Deep Learning (object detection) Integration**
---------------------------
# 3.1. Tensorboard Training Evaluation
![image](https://github.com/Summer-Lo/Deep_Learning_Based_Safty_Light_Curtain/blob/main/images/learning_rate.png)

![image](https://github.com/Summer-Lo/Deep_Learning_Based_Safty_Light_Curtain/blob/main/images/losses_smoothing.png)

![image](https://github.com/Summer-Lo/Deep_Learning_Based_Safty_Light_Curtain/blob/main/images/losses_nonsmoothing.png)

**4. Help **
---------------------------
### 4.1 Usage of scripts
1. camera_checker.sh: it is a script for you to check whether the python can receive gazebo virutal camera image or not. It will display the raw image from ros topic

2. cv_lane_detector.sh: it is a script to perform lane detection using the virutal camera as a source but it is not compatible for tensorflow (py3)

3. dataset_prepare.sh: it is a script that keep on taking saving pictures in order to help you prepare object detection dataset.

4. fake_velocity.sh: it is a script to publish twist message to control the robot directly.

5. run_gazebo.sh: it is a script to start gazebo and load the world

6. simple_controller.sh: it is a script to allow manual control of the robot.

7. visualize_nodes.sh: it is a script to generate ros graph

8. camera_publish.sh: it is a script to publish the image as a jpg from python2 opencv

9. camera_subscriber.sh: it is a script to show published image and perform lane detection (testing)

10. TensorRT-ROS-Bridge.sh: it is a script which does not belong to ROS. It loads published image and perform AI object detection and other image processsing.

11. vision_control.sh: it is a script to perform PID control based on vision and deep learning.

### 4.2 Startup Procedures
1. ./run_gazebo.sh (load the world) [ROS]
2. ./camera_publish.sh (publish the image) [ROS]
3. ./TensorRT-ROS-Bridge.sh (enable AI and vision processing module) [NOT ROS]
4. ./vision_control.sh [ROS]

**Remeber to put correct models to ~/.gazebo/models, otherwise the world cannnot be loaded. Also, put budiling_editor_models under ~/

**5. Reference **
---------------------------
TensorRT Object Detection Program Framework -> https://github.com/jkjung-avt/tf_trt_models
