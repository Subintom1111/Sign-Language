import os
import cv2

# Directory to save the collected data
DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Number of classes and dataset size
number_of_classes = 3
dataset_size = 100

# Camera index
camera_index = 0  # Change this if necessary

# Initialize the camera
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    # Wait for user input to start collecting data for the current class
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.putText(frame, 'Ready? Press "S" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) == ord('S'):
            break

    # Collect the dataset for the current class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)

        # Save the frame as an image file
        image_path = os.path.join(class_dir, '{}.jpg'.format(counter))
        cv2.imwrite(image_path, frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
