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
