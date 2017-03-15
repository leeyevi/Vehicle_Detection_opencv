import cv2

#print(cv2.__version__)

cascade_src = 'cars.xml'
video_src = 'video2.avi'
# video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(video_src)

car_cascade = cv2.CascadeClassifier(cascade_src)

car_counter = 0;



while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break





    row, cols, channels = img.shape
    row_new = int(0.35*row)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.line(img,(0, row_new),(cols, row_new),(0,0,255))

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    #cv2.line(gray, (0, 0), (30, 30), (0, 0, 255),5)

    condition = False

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        '''if condition == False and row_new<= x <= row_new+1:
            car_counter+=1
            condition=True
            print(car_counter)'''






    cv2.imshow('video', img)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()

#print(ncars)


