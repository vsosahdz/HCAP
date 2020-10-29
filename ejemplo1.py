import cv2

imagen = cv2.imread('imagen.jpg')
imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
print(imagen.shape)
print(imagen[0][0][0])
imagen = cv2.resize(imagen,(256,256))

cv2.imwrite('resizeimagen.jpg',imagen)
#Only native linux and Mac
cv2.imshow('image',imagen)
cv2.waitKey(0)


