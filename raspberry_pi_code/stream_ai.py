import cv2
import mediapipe as mp
import time

URL = "http://10.231.90.30:5000/video"

cap = cv2.VideoCapture(URL)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# 🔥 SPEED OPTIMIZATION SETTINGS
prev_time = 0

with mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0,          # 🔥 FASTEST MODEL
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    frame_skip = 2   # 🔥 process every 2nd frame
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 🔥 RESIZE FRAME (VERY IMPORTANT)
        frame = cv2.resize(frame, (640, 360))

        frame_count += 1
        if frame_count % frame_skip != 0:
            continue

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

                # 🔥 ONLY PRINT WHEN NEEDED (NOT EVERY FRAME)
                print("Hand detected")

        # FPS CALCULATION
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time + 0.0001)
        prev_time = curr_time

        cv2.putText(frame, f"FPS: {int(fps)}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0), 2)

        cv2.imshow("ISL Edge AI (Optimized)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
