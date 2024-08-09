<h1 align="center">
  <img src="https://github.com/Un1xG0d/OpenTreat2/blob/master/README/Icon-full.png">
</h1>
<br>

OpenTreat allows a user to view and interact with their pets while not at home. Watch a live video stream of your pets from your smartphone or laptop, and remotely dispense treats with the push of a button.

This a complete rewrite of my original OpenTreat project found [here](https://github.com/Un1xG0d/OpenTreat).

## Overview
The treat dispenser system is built using a Raspberry Pi and 3D printed parts. When a user presses the button on the webapp, it turns the servo motor for a certain number of seconds. This spins the middle piece and dispenses a section of treats into the bowl below.

## Parts needed
* Raspberry Pi
* Raspberry Pi webcam
* LS3006 servo (any 360* servo should work)
* 3D printer

## Physical assembly
1. Download and 3D print each STL listed in the `models` folder
	1. The recommended print settings are in the Resources section below
2. Assemble the parts using super glue
3. Hook up the 3 servo wires to the Raspberry Pi’s GPIO pins

## Device setup
1. Image your Raspberry Pi with Raspbian
2. Create a new user with the username `admin`
3. Configure your WiFi network settings

## Download the code
```
git clone https://github.com/Un1xG0d/OpenTreat2.git ~/OpenTreat
cd ~/OpenTreat
```

## Install Python dependencies
```
pip3 install -r requirements.txt
```

## Automatic startup
Create a cronjob with `crontab -e` to automatically start the webapp on boot.

```
@reboot python3 /home/admin/OpenTreat/web.py
```

## Port forward the app
Make sure to change your router settings to allow a port forward of port 3000 to your Raspberry Pi. This is what makes the webapp accessible to the internet.

## View the video stream
On your smartphone or laptop, browse to your router's external IP on port 3000 to view the video stream of your pets. 
Press the bone button to drop treats into your pets' bowl.

## Resources
### Recommended print settings
> Scale: 100%  
> Infill: 10%  
> Layer Height: 0.2  
> Speed: Standard  
> Supports: None

### RPi GPIO pinout
> Red wire - Pin 1 - 3v3 power  
> Black wire - Pin 6 - ground  
> Orange wire - Pin 11 - GPIO 17  

## Screenshots & proof-of-concept
![](README/Mockup-1.png)
