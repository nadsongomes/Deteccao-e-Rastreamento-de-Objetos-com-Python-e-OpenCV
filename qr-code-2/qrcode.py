import cv2
from pylibdmtx.pylibdmtx import decode #bilioteca para ler o qr code

# Lê o arquivo usando OpenCV
data = cv2.imread('Imagem3.jpg')

# Busca o qr code na imagem de entrada
decoded_data = decode(data)

# Desenha um retângulo em volta de cada qr code e escreve o conteúdo acima dele
for datamatrix in decoded_data:
    x, y, w, h = datamatrix.rect
    #Função para desenhar um retângulo em volta do qr code
    cv2.rectangle(data, (x, y), (x + w, y + h), (0, 0, 255), 3)
    # Função para escrever o conteúdo do qr code
    cv2.putText(data, datamatrix.data.decode('utf-8'), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Mostra a imagem resultante
cv2.imshow('Data', data)
cv2.waitKey(0)