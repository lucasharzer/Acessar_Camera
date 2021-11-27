import cv2
from time import sleep


print("\033[1;34mAcesso à Camera:\033[m")
camera = cv2.VideoCapture(0)

if camera.isOpened():

    print("\033[1;33m\nConectando à câmera...\033[m")
    sleep(3)
    print("\033[1;32mConectou!\033[m")
    
    # Ler câmera
    print("\033[1;34m\nInformações de pixels:\033[m")
    info = camera.read()
    print(f'\033[1;32m{info}\033[m')

    print("\033[1;34m\nPrepare para tirar uma foto:\n- Após a exibição da câmera,\n- Faça uma pose,\n- pressione a tecla ESC\nE pronto a foto será tirada!\033[m")
    sleep(3)
    while True:
        o = str(input("\033[1;33m\nPreparado para tirar a foto? [S/N] \033[m")).strip().upper()
        if o == "S":
            break

    print("\033[1;33\nmexibir video ...\033[m")
    sleep(3)
    print("\033[1;32mexibindo\033[m")

    # Exibir câmera
    validacao, frame = camera.read()
    while validacao:

        validacao, frame = camera.read()
        cv2.imshow("Video da camera", frame)

        # espera a imagem carregar e armazena ela
        key = cv2.waitKey(5)

        # Parar a exibição com a tecla ESC (número 27)
        if key == 27:
            break

    cv2.imwrite("Foto.png", frame)

print("\033[1;33m\nProcessando ...\033[m")
sleep(5)
print("\033[1;32mFoto tirada!\033[m")

camera.release()
cv2.destroyAllWindows()

print("\033[1;34mObrigado!\033[m")



