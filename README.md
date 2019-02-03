<div align="center">
    <img src="marketing/logo-rect.png" alt="CV-Livestock Protection"/>
  <br>
</div>

## Problem Solved
Thousands of sheep, cattle, and horses are mutilated every year due to the poor means of monitoring. Unfortunately, there is no known feasible and financially viable way to get immediate notice of it and farmers get alerted only after the damage has already been done. The solution was applying Computer Vision and AI to alert farmers at a moments notice.  This software detects when a predator is present in the frame and sends a text message to the farmer using the Twilio API.

> Kaczensky, Petra. “Large Carnivore Depredation on Livestock in Europe.” Ursus, vol. 11, 1999, pp. 59–71. JSTOR, www.jstor.org/stable/3872986.

## Who is this for?
Farmers who don't have the financial resources to invest in complex infrastructure.

## Challenges & Roadmap
- One challenge we experienced during the development of this software was creating/finding a model that accurately could identify livestock.
- Given the limited computational capacities of recording devices, we hope to move the execution of the program on the cloud
- Use it for monitoring the wildlife and give an ability to the researchers to get immediate notice when an event of interest to them takes place.
- Train the model further in classifying objects that are of interest to us.
- Develop a much more extensive front-end that shows past information/threats along with adding location input.

## Technologies
* <p><a href = "https://www.twilio.com/"><b>Twilio API</b></a> - REST for Text Messages, with custom number.</p>

* <p><a href = "https://pjreddie.com/darknet/yolo/"><b>YOLOv3</b></a> - Real Time Object Detection</p>

* <p> <a href = "https://www.tensorflow.org/"><b>TensorFlow</b></a> - An open source ML framework for everyone</p>
