import cv2

# Захват видеопотока с первой камеры
cap = cv2.VideoCapture(0)  

# Проверка на успешный захват видеопотока
if not cap.isOpened():
    print("Ошибка: Не удалось открыть видеопоток.")
else:
    while True:
        ret, frame = cap.read()  # Чтение кадра

        # Проверка успешности чтения кадра
        if not ret:
            print("Ошибка: Не удалось прочитать кадр.")
            break

        # mirrored_ftame = cv2.flip(frame,1)
        # cv2.imshow('Video', mirrored_ftame)
        cv2.imshow('Video', frame)  # Отображение видеопотока
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Выход при нажатии клавиши 'q'
            break

    cap.release()  # Освобождение видеопотока
    cv2.destroyAllWindows()  # Закрытие всех окон