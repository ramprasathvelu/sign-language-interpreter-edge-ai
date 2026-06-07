import cv2
import mediapipe as mp
import joblib
import numpy as np
from collections import deque, Counter

# ----------------------------
# LOAD MODEL
# ----------------------------
model = joblib.load("isl_model.pkl")

# ----------------------------
# VIDEO STREAM (your laptop stream)
# ----------------------------
URL = "http://10.231.90.30:5000/video"
cap = cv2.VideoCapture(URL)

# ----------------------------
# MEDIAPIPE SETUP
# ----------------------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# ----------------------------
# BUFFER FOR STABILITY
# ----------------------------
buffer = deque(maxlen=15)  # store last 15 predictions

with mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0
) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 360))
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # ----------------------------
                # EXTRACT FEATURES (63 values)
                # ----------------------------
                features = []
                for lm in hand_landmarks.landmark:
                    features.extend([lm.x, lm.y, lm.z])

                # ----------------------------
                # PREDICT
                # ----------------------------
                prediction = model.predict([features])[0]

                # add to buffer
                buffer.append(prediction)

                # majority vote
                if len(buffer) == 15:
                    most_common = Counter(buffer).most_common(1)[0][0]
                else:
                    most_common = prediction

                # ----------------------------
                # OUTPUT
                # ----------------------------
                print("GESTURE:", most_common)

                cv2.putText(frame,
                            f"{most_common}",
                            (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            2)

        cv2.imshow("ISL Stable Prediction", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
