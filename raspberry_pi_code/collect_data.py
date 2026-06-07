import cv2
import mediapipe as mp
import csv
import time

URL = "http://10.231.90.30:5000/video"
cap = cv2.VideoCapture(URL)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# 🎯 Ask user which gesture to record
label = input("Enter gesture label (HELLO/YES/NO/THANKYOU/HELP): ")

# 📁 CSV file
file = open("isl_dataset.csv", "a", newline="")
writer = csv.writer(file)

with mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0
) as hands:

    print("Press S to start collecting samples")

    collecting = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 360))
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # 🧠 Extract 63 features
                row = [label]
                for lm in hand_landmarks.landmark:
                    row += [lm.x, lm.y, lm.z]

                # 🔥 Save only when collecting
                if collecting:
                    writer.writerow(row)
                    print("Saved:", label)

        cv2.putText(frame,
                    "Press S=start, Q=quit",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0), 2)

        cv2.imshow("DATA COLLECTION", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            collecting = True
            print("Recording started...")

        if key == ord('q'):
            break

cap.release()
file.close()
cv2.destroyAllWindows()
