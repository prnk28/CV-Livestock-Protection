<div align="center">
    <img src="marketing/logo-rect.png" alt="CV-Livestock Protection"/>
  <br>
</div>

## Problem Solved
We understood that there was not a feasible option for farmers to help monitor their livestock without the use of equipment that would cost a lot of money; The solution was applying Computer Vision and AI to alert farmers at a moments notice. Thousands of sheep, cattle, and horses are mutilated every year due to poor means of monitoring. This software detects when a predator is present in the frame, detects the hostility and sends a text message to the farmer using the Twilio API.

> Kaczensky, Petra. “Large Carnivore Depredation on Livestock in Europe.” Ursus, vol. 11, 1999, pp. 59–71. JSTOR, www.jstor.org/stable/3872986.

## Who is this for?
Farmers who dont have the financial resources to invest in complex equipment.

## Challenges & Roadmap
- One challenge we experienced during the development of this software was creating/finding a model that accurately could identify livestock.
- Our plan is to further train our model to correctly identify predators and use localized information to determine wether that the threat present is actually a predator in the area.
- We also plan to develop a much more extensive frontend that shows past information/threats along with adding location input.

## Technologies
* <p><a href = "https://www.twilio.com/"><b>Twilio API</b></a> - REST for Text Messages, with custom number.</p>

* <p><a href = "https://pjreddie.com/darknet/yolo/"><b>YOLOv3</b></a> - Real Time Object Detection</p>

* <p> <a href = "https://www.tensorflow.org/"><b>TensorFlow</b></a> - An open source ML framework for everyone</p>
