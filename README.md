# Insurance of Things

#Inspiration
Through our daily observation of bustling cities jam-packed with cars, and also the latest trends of utilizing advanced telematics in insurance, we realized that each car's data has an interesting story to unveil that could relate to how prudent and cautious the driver is. This gives us the power to tackle auto insurance fraud.

#What it does
We built a webapp which enables user inputs to be integrated with the IoT sensors to be installed in the car and our database in real time. The data is analyzed automatically after each trip and every 5 trips, the summary can be used to determine if the driver can receive additional premium discount due to their good driving habits. Users are given option to take all the discount or contribute donation to the Vision Zero initiative by Parachute Canada. We also trained a machine learning model which uses the Random Forest Classifier to identify other factors relating to driver rating with 71% accuracy.

#How we built it
We gather the inputs from user by their selections in the webapp (interface) and sensors connected to Arduino to obtain their car data. The webapp is built using HTML and CSS, and is connected using MySQL client (in AWS) to our Database. The data is collected in real-time and is automatically analyzed using Python on Django, with further statistical learning using AdaBoost Random Forest Classifier. On the IoT side, we used Ultrasonic Proximity Sensor (HC-SR04) and Gyrometer/Accelerometer (MPU 6050) for object proximity, driving speed and instanteneous hard brake data.

#Challenges we ran into
This is our first time trying to build and connect a network of IoT sensors. Unfortunately, we ran into problem for our Gyrometer sensor, and we decided to use real-time user inputs about their current driving speed. We also have not fully connect our proximity sensor data to the database although we have coded the proximity analysis.

#Accomplishments that we're proud of
Despite having a hard time in the integration, we have managed to pull out some big parts of the project together:

#Set up the proximity sensor and proximity analysis
Connected the webapp interface to the database, including the real-time clock and road condition (highway or city)
Accurately obtained the real-time inputs from webapp and store it in our database for analysis
Database and web app is updated automatically through each input
Auto-analyzed the driving speed that can be used for both real-time user and sensor inputs
Programmed the scheme analysis that compares interquartile intervals of user driving speed to the driving scheme range, and determine the driver status
Classified weightings of other possible factors relating to driver status (as determined by their speed) using Random Forest, given some driving dataset

#What's next for Insurance of Things (IoT)
Setting up the gyrometer and accelerometer to be able to obtain data directly from the sensor, including angular velocity data
Set up GPS and use Road API to automatically detect which road the user drives in
Refurnish the webapp interface and integrate it with more sensors for data collection
