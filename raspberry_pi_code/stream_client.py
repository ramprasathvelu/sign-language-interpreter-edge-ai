import cv2

# YOUR LAPTOP IP IS INSERTED HERE
URL = "http://10.231.90.30:5000/video"

cap = cv2.VideoCapture(URL)

if not cap.isOpened():
    print("❌ Cannot connect to laptop stream")
    exit()

print("✅ Connected to laptop webcam stream")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Frame not received")
        break

    cv2.imshow("EDGE AI - Laptop Webcam Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
