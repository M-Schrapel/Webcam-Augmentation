# Tutorial: Configuring OBS studio to create virtual cameras
After completing this tutorial you can use the python output window as a virtual camera.  

## Install OBS studio
First download OBS studio and the virtual camera plug-in

- [OBS Studio](https://obsproject.com/)
- [OBS virtual-camera-plugin](https://obsproject.com/forum/resources/obs-virtualcam.949/)

![Step 1](/Tutorial/Step_01.jpg)
Once you have selected your operating system, download and install OBS Studio first and then proceed with the virtual camera plug-in.

During the installation you will be asked to configure OSB studio.
Select the virtual camera and proceed.
![Step 2](/Tutorial/Step_02.jpg)

You only need one virtual camera device - press next.
![Step 3](/Tutorial/Step_03.jpg)

## Create Virtual Camera
After installing OBS Studio open a terminal, download the repository and start the Python program.
```sh
$ git clone https://github.com/M-Schrapel/Webcam-Augmentation.git
$ cd Webcam-Augmentation
$ python .\emoji_webcam.py
```
If you have any errors check if you have installed the right modules.
```sh
$ pip install opencv-contrib-python
$ pip install numpy
```
Your webcam should run now in a window created by python. You can stop the recording by pressing q. If you want to select a different webcam open emoji_webcam.py with a text editor and change the VIDEO_SOURCE in line 26. Now navigate to OBS studio again and press the right mouse button in the main window. To select the Python window for your virtual camera navigate to **Add → Window Capture**. 
![Step 4](/Tutorial/Step_04.jpg)

Simply press OK.
![Step 5](/Tutorial/Step_05.jpg)

A new window should appear. Select the python window as shown below and press OK.
![Step 6](/Tutorial/Step_06.jpg)

Navigate to **Tools → Virtual Camera** in the  main window of OBS Studio. If you cannot see this option, you need to install the [OBS virtual-camera-plugin](https://obsproject.com/forum/resources/obs-virtualcam.949/).
![Step 7](/Tutorial/Step_07.jpg)

A new window appears. Select the target camera OBS-Camera2 as shown below. Then, press Start and close this window.
![Step 8](/Tutorial/Step_08.jpg)

At the bottom on the main window you should see now an entry of the recorded window in Sources. Press the right mouse button and select Filters.
![Step 9](/Tutorial/Step_09.jpg)

A new window appears in which you press the + on the right bottom corner. Then select the VirtualCam.
![Step 10](/Tutorial/Step_10.jpg)

On the right of this window, you can now set up the virtual camera. Select the target camera OBS-Camera2 and press Start. You can set the number of buffered frames to zero. Press Close and your virtual camera is ready for use.
![Step 11](/Tutorial/Step_11.jpg)

Start your preferred video chat program and select the OBS-Camera.
If your program is not able to find a camera stop the Python window by pressing q, search for camera in your video chat program again, select the OBS-Camera and restart the Python script.
```sh
$ python .\emoji_webcam.py
```

Everything should work now. By bringing the Phyton window to the front you can augment the webcam stream. Use the ArUco marker with the green and black color to make movements smooth.

![ArUco Marker](ArUco_marker.jpg)


##
![HCI Group](Tutorial/Institute.png)

This repository is provided by the Human-Computer Interaction Group at the University Hannover, Germany. For inquiries, please contact maximilian.schrapel@hci.uni-hannover.de
