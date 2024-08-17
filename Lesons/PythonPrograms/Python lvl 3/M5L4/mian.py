import dlib
import cv2

# Загрузка определителя лиц из dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Загрузка изображения
image = cv2.imread("face.png")

# Конвертация изображения в черно-белое
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Обнаружение лиц на изображении
faces = detector(gray)

# Цикл по всем найденным лицам
for face in faces:
    landmarks = predictor(gray, face)
    
    # Отрисовка точек лица на изображении
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

# Отображение изображения с обведенными точками лица
show(image)