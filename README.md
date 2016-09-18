*Update*: This project won the Philips-sponsored award for the best use of human activity recognition at HackMIT 2016!

#What?!
We tried a moonshot and this repository is a binary mess of all the code we wrote to hack together our hardware project in under 24 hours. If you're _really_ interested in knowing what we actually did, please contact the contributor(s). This project uses the Google Cloud Vision API, an Arduino board, and some sensors.

#Inspiration
With the coming of the IoT age, we wanted to explore the addition of new experiences in our interactions with physical objects and facilitate crossovers from the digital to the physical world. Since paper is a ubiquitous tool in our day to day life, we decided to try to push the boundaries of how we interact with paper.

#What it does
A user places any piece of paper with text/images on it on our clipboard and they can now work with the text on the paper as if it were hyperlinks. Our (augmented) paper allows users to physically touch keywords and instantly receive Google search results. The user first needs to take a picture of the paper being interacted with and place it on our enhanced clipboard and can then go about touching pieces of text to get more information.

#How we built it
We used ultrasonic sensors with an Arduino to determine the location of the user's finger. We used the Google Cloud API to preprocess the paper contents. In order to map the physical (ultrasonic data) with the digital (vision data), we use a standardized 1x1 inch token as a 'measure of scale' of the contents of the paper.

#Challenges we ran into
So many challenges! We initially tried to use a RFID tag but later figured that SONAR works better. We struggled with Mac-Windows compatibility issues and also struggled a fair bit with the 2D location and detection of the finger on the paper. Because of the time constraint of 24 hours, we could not develop more use cases and had to resort to just one.

#What we learned
We learned to work with the Google Cloud Vision API and interface with hardware in Python. We learned that there is a LOT of work that can be done to augment paper and similar physical objects that all of us interact with in the daily world.
1. In autism and learning
2. In large-scale event management and planning
3. In note annotation and personal notes management
4. And many more!

#What's next for Augmented Paper
Add new applications to enhance the experience with paper further. Design more use cases for this kind of technology.

