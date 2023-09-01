import cv2
from pylibdmtx.pylibdmtx import decode #bilioteca para ler o qr code
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()

    # Busca o qr code no frame
    decoded_data = decode(frame)
    # Desenha um retângulo em volta de cada qr code e escreve o conteúdo acima dele
    for datamatrix in decoded_data:
        x, y, w, h = datamatrix.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.putText(frame, datamatrix.data.decode('utf-8'), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
