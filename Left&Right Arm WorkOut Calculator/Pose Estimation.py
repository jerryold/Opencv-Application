#!/usr/bin/env python
# coding: utf-8

# # Import Dependency

# In[1]:


import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# In[2]:


# VIDEO FEED
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('Mediapipe Feed', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()


# # Make Detections

# In[3]:


cap = cv2.VideoCapture(0)
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
                
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 
                                 
                                 )
      

        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# In[4]:


get_ipython().run_line_magic('pinfo2', 'mp_drawing.DrawingSpec')


# # 2. Determining Joints
# ![68747470733a2f2f692e696d6775722e636f6d2f336a38425064632e706e67.png](attachment:68747470733a2f2f692e696d6775722e636f6d2f336a38425064632e706e67.png)
# 

# In[5]:


cap = cv2.VideoCapture(0)
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
                
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # Make detection
        results = pose.process(image)
        
        
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract Landmark
        try:
            landmarks=results.pose_landmarks.landmark
            print(landmarks)
        except:
            pass
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 
                                 
                                 )
      

        cv2.imshow('Body Detect Demo', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# In[6]:


len(landmarks)


# In[7]:


for ldmarks in mp_pose.PoseLandmark:
    print(ldmarks)


# In[8]:


landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]


# In[9]:


landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]


# In[10]:


landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]


# # 3.Calculate Angles

# In[11]:


def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])#arctan2 function can calculate the angle
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle


# In[12]:


shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]


# In[13]:


shoulder, elbow, wrist


# In[15]:


calculate_angle(shoulder, elbow, wrist)


# In[16]:


tuple(np.multiply(elbow, [640, 480]).astype(int))


# In[18]:


cap = cv2.VideoCapture(0)
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
                
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # Make detection
        results = pose.process(image)
        
        
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract Landmark
        try:
            landmarks=results.pose_landmarks.landmark
            # Get the cordinates
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            # Calculate angle
            angle=calculate_angle(shoulder, elbow, wrist)
            
            #Visualize angle
            cv2.putText(image,str(angle),
                           tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2, cv2.LINE_AA
                       )
            print(landmarks)
        except:
            pass
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 
                                 
                                 )
      

        cv2.imshow('Calculate Angles Test', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# # 4.Curl Counter

# In[73]:


cap = cv2.VideoCapture(0)
# Curl counter varibles
left_counter=0
right_counter=0
left_stage=None
right_stage=None


## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
                
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # Make detection
        results = pose.process(image)
        
        
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract Landmark
        try:
            landmarks=results.pose_landmarks.landmark
            # Get the left cordinates
            left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            # Get the Right cordinates
            right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            # Calculate angle
            angle=calculate_angle(left_shoulder, left_elbow, left_wrist)
            angle1=calculate_angle(right_shoulder,  right_elbow,  right_wrist)
            #Visualize angle
            cv2.putText(image,str(angle),
                           tuple(np.multiply(left_elbow, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2, cv2.LINE_AA
                       )
            #Visualize angle1
            cv2.putText(image,str(angle1),
                           tuple(np.multiply(right_elbow, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 100, 255), 2, cv2.LINE_AA
                       )
            #Curl counter logic
            if angle>160:
                left_stage="down"
                
            if angle<30 and left_stage=="down":
                left_stage="up"
                left_counter+=1
                print(left_counter)
            if angle1>160:
                right_stage="down"
                
            if angle1<30 and right_stage=="down":
                right_stage="up"
                right_counter+=1
                print(right_counter)
                
        
            
        except:
            pass
        #Render curl counter
        #Setup status box
        cv2.rectangle(image, (0,0), (500,100), (165,217,255), -1)
        
        
        #Left_Rep data
        cv2.putText(image, 'Left_REPS', (15,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (213,128,145), 1, cv2.LINE_AA)
        cv2.putText(image, str(left_counter), 
                    (40,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (20,20,115), 5, cv2.LINE_AA)
        #Left_Stage data
        cv2.putText(image, 'Left STAGE', (130,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (213,128,145), 1, cv2.LINE_AA)
        cv2.putText(image, left_stage, 
                    (100,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (20,20,115), 5, cv2.LINE_AA)
        #Right_Rep data
        cv2.putText(image, 'RIGHT_REPS', (250,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (213,128,145), 1, cv2.LINE_AA)
        cv2.putText(image, str(right_counter), 
                    (280,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (20,20,115), 5, cv2.LINE_AA)
        #Right_Stage data
        cv2.putText(image, 'RIGHT STAGE', (380,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (213,128,145), 1, cv2.LINE_AA)
        cv2.putText(image, right_stage, 
                    (380,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (20,20,115), 5, cv2.LINE_AA)
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 
                                 
                                 )
      

        cv2.imshow('Left&Right Arm WorkOut Calculator Demo', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




