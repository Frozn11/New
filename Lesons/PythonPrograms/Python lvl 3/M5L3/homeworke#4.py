import cv2

cap = cv2.VideoCapture('Dancing_Pirate.mp4') # <-- можно и .mov

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))

width = int(cap.get(3))
height = int(cap.get(4))

writer = cv2.VideoWriter('Output.mp4',fourcc, fps, (width,height))

while True:
    success, frame = cap.read()

    if frame is None:
        break

    cv2.imshow('Video',frame)
    cv2.waitKey(30)

    writer.write(frame)

cap.release()
cv2.destroyAllWindows()