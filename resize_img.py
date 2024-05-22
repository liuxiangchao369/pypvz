import cv2

if __name__=="__main__":
    path="./resources/graphics/Cards/card_kuangtu.png"
    img=cv2.imread(path)
    img=cv2.resize(img,(100,140))
    cv2.imwrite(path,img)