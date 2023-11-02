## Using a gamepad to move cleanbot in simulation:

- Finding your gamepad:
````
ls /dev/input/
````

- If you are using either a PS3 or Xbox One gamepad, you can run the following:

````
ros2 launch teleop_twist_joy teleop-launch.py joy_dev:='/dev/input/<gamepad-name>' joy_config:='<ps3 or xbox>'
````

- If you are using anything else, it is ideal to make a config for your gamepad first, find the axis and button ID's for your gamepad 
  - jstest can be used for this:

````
sudo apt install joystick jstest-gtk evtest
````
````
jstest /dev/input/<name>
````
- for a gui version of the same tool:
````
jstest-gtk
````
- Using `xbox_360_config.yaml` as a template:
  - Change `axis_linear.x` to the up/down axis of the joystick
  - Change `axis_angular.yaw` to the left/right axis of the joystick
  - Set `enable_button` and `enable_turbo_button` to buttons comfortable to hold

- To use a custom config:
````
ros2 launch teleop_twist_joy teleop-launch.py joy_dev:='/dev/input/<gamepad-name>' config_filepath:='<path-to-cleanbot-pkg>/cleanbot_package/config/<gamepad-config>.yaml'
````