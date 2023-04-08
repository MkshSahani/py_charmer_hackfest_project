# py_charmer_hackfest_project

### Problem statement: 
For peoples doing work from home or student studying online it has been
Observed they are more in stress and there screen time also increase, which affect Their mental and physical health, we are suppose to make a Desktop based application which detect the the stress using some facial features, there screen time, there time spent in typing, there browsing pattern( to understand what kind of content they consume, which can can help in detecting there mentality), there physical movement( using some mobile application, should be integrated with whole system), using any combination of these features, generate the report for users which can help them to detect stress level there are  going through and based on that provide them required advices to improve their work style or way of studying.

## Solution approach:
We are providing an applied AI base solution for this problem. We will provide a desktop application to users. We will detect the required attributes needed to process and send it to the server, where we will perform the required processing and send the Report and required advice to users.
	
### Stress Detection:
Face features analysis: we will we collect real time facial data of users using the webcam we will detect the features like eyebrows relative position and eye blinking rate
To detect the stress level of users, if stress levels go beyond our set threshold value we will detect and store that, later by processing this data we will generate a report, on regular intervals based on user preferences.
    
### Screen and Typing time:
A thread will always keep a track of screen time of users and how much time users spend on time, using the the screen time and typing time of users we can check
How much of the day he spends on the system. 

### Browsing Pattern:
We will keep track of browsing pattern of users, here we will not store the ip address of website user visits instead we will store the kind of website user visits like (social media, e-commerce, streaming platforms, information websites, etc), we would have already made clusters for kind of websites, and using this data we will generate the required report.


### TechStack: following are the tech stack we are using to develop the product.
1. Tkinter (Desktop application), GUI library of python
2. FastAPI( webBackEnd ), backend framework of python
3. Opencv, for collection and processing image data
4. Tensorflow and keras : for Deep Learning used in facial stress detection.
5. Mysql, mongodb: for Database 
6. Numpy, pandas, matplotlib : for performing data science related processing.
 

