import menu
import sys
import os
from os.path import exists
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pprint import pprint



class Image:
    
    def __init__(self):
        self.imageBytes    = None# cv2.imread(".\\aaa.png", cv2.IMREAD_UNCHANGED) #None <- Voltar pra None quando finalizar.
        self.newImageBytes = None
        self.savedImage = False


    def UndoImage(self):
        if self.newImageBytes is not None:
            print("\t [!!!] Cuidado, você deseja desfazer todo o procedimento  (Isto apagará todo o progresso e retornará a imagem original)?")
            opt = ""
            while True:
                print("Escolha (Y\\N): ", end="")
                opt = str(input())
                if(opt.lower() == 'y'):
                    self.newImageBytes = None
                    break
                if(opt.lower() == 'n'):
                    return
        else:
            print("\t [!] Não há alterações recentes para que seja necessário desfazer.")
            return




    def LoadImage(self):
        if self.imageBytes is not None:
            print("\t [!!!] Você já tem uma imagem carregada, deseja sobrescrever a imagem? (Isto apagará a imagem original e a alterada da memória)")
            opt = ""
            while True:
                print("Escolha (Y\\N): ", end="")
                opt = str(input())
                if(opt.lower() == 'y'):
                    imageBytes = None
                    newImageBytes = None
                    break
                if(opt.lower() == 'n'):
                    return
            
            
        print("\n\t [!] Digite o caminho absoluto local para sua imagem: ")
        path = ""
        while True:
            print("Caminho: ", end="")
            path = str(input())
            if os.path.exists(path) is True:
                break
            else:
                print("\n\tCaminho incorreto ou arquivo inexistente.\n")
        
        print("[!] Carregando imagem original a memória.")
        self.imageBytes = cv2.imread(path)
        
    


    def BinarizeImage(self):
        if self.imageBytes is None:
            print("[!] Carregue uma imagem antes de prosseguir.")
            return
       
        
        min_th_value = -1
        max_th_value = -1

        while ((min_th_value < 0) or (max_th_value < 0) or (min_th_value > 255) or (max_th_value > 255)):
            min_th_value = int(input("Mínimo valor de Binarização: "))
            max_th_value = int(input("Máximo valor de Binarização: "))

        im_gray = None
        
        if self.newImageBytes is None:
            im_gray = cv2.cvtColor(self.imageBytes, cv2.COLOR_BGR2GRAY)
        else:
            if len(np.shape(self.newImageBytes)) == 2:
                im_gray = cv2.cvtColor(self.newImageBytes, cv2.COLOR_GRAY2BGR)
            else:
                im_gray = cv2.cvtColor(self.newImageBytes, cv2.COLOR_BGR2GRAY)
                

        (th, im_bw) = cv2.threshold(im_gray, min_th_value, max_th_value, cv2.THRESH_BINARY)
        self.newImageBytes = im_bw


        print("[!] Imagem binarizada.")
        return



    def DetectBorder(self):
        if self.imageBytes is not None:
        
            min_th_value = -1
            max_th_value = -1

            while ((min_th_value < 0) or (max_th_value < 0) or (min_th_value > 255) or (max_th_value > 255)):
                min_th_value = int(input("Mínimo valor de Threshold: "))
                max_th_value = int(input("Máximo valor de Threshold: "))

            
            dt_border = None
            if self.newImageBytes is None:
                dt_border = cv2.cvtColor(self.imageBytes, cv2.COLOR_BGR2GRAY)
            else:
                dt_border = cv2.cvtColor(self.newImageBytes, cv2.COLOR_BGR2GRAY)

            im_bd = cv2.Canny(dt_border, min_th_value, max_th_value)
            self.newImageBytes = im_bd

            print("[!] Bordas detectadas.")
            return

        else:
            print("\t[!] Você deve carregar uma imagem primeiro.")
        return
    

    def ChangeColorPalletes(self):
        if self.imageBytes is None:
            print("\t[!] Imagem nao carregada.")
            return

        os.system("cls || clear") # Limpa-tela
        print("\t [*]Escolha uma opção de paleta de cores: ")
        print("\t\t 1 -- Tons de Cinza")
        print("\t\t 2 -- HSV")
        print("\t\t 3 -- HSL")
        print("\t\t 4 -- YCbrCb")
        print("\t\t 5 -- Sair")

        opt = -1
        while ((opt < 0) or (opt > 5)):
            print("Escolha: ", end="")
            opt = int(input())
            cg_colors = None

            if(opt == 1):
                if self.newImageBytes is None:
                    cg_colors = cv2.cvtColor(self.imageBytes, cv2.COLOR_BGR2GRAY)
                else:
                    if len(np.shape(self.newImageBytes)) == 2:
                        cg_colors = cv2.cvtColor(self.newImageBytes, cv2.COLOR_GRAY2BGR)
                    else:
                        cg_colors = cv2.cvtColor(self.newImageBytes, cv2.COLOR_BGR2GRAY)
                
                print("\t[!] Mudando as cores para Tons de Cinza.")
                self.newImageBytes = cg_colors
                break
            
            if (opt == 2):
                if self.newImageBytes is None:      
                    cg_colors = cv2.cvtColor(self.imageBytes, cv2.COLOR_BGR2HSV)
                else:
                    if len(np.shape(self.newImageBytes)) == 2:
                        cg_colors = cv2.cvtColor(self.newImageBytes, cv2.COLOR_GRAY2BGR)
                        cg_colors = cv2.cvtColor(cg_colors, cv2.COLOR_BGR2HSV)
                    else:
                        cg_colors = cv2.cvtColor(self.newImageBytes, cv2.COLOR_BGR2HSV)
                
                print("\t[!] Mudando as cores para HSV.")
                self.newImageBytes = cg_colors


                break

            if (opt == 3):
                if self.newImageBytes is None:      
                    cg_colors = cv2.cvtColor(self.imageBytes, cv2.COLOR_BGR2HLS_FULL)
                else:
                    if len(np.shape(self.newImageBytes)) == 2:
                        cg_colors = cv2.cvtColor(self.newImageBytes, cv2.COLOR_GRAY2BGR)
                        cg_colors = cv2.cvtColor(cg_colors, cv2.COLOR_BGR2HLS_FULL)
                    else:
                        cg_colors = cv2.cvtColor(self.newImageBytes, cv2.COLOR_BGR2HLS_FULL)
                
                print("\t[!] Mudando as cores para HSL.")
                self.newImageBytes = cg_colors

                break
            
            if (opt == 4):
                if self.newImageBytes is None:      
                    cg_colors = cv2.cvtColor(self.imageBytes, cv2.COLOR_BGR2YCrCb)
                else:
                    if len(np.shape(self.newImageBytes)) == 2:
                        cg_colors = cv2.cvtColor(self.newImageBytes, cv2.COLOR_GRAY2BGR)
                        cg_colors = cv2.cvtColor(cg_colors, cv2.COLOR_BGR2YCrCb)
                    else:
                        cg_colors = cv2.cvtColor(self.newImageBytes, cv2.COLOR_BGR2YCrCb)
                
                print("\t[!] Mudando as cores para YCbrCb.")
                self.newImageBytes = cg_colors
                break

            if (opt == 5):
                print("\t [*] Saindo das paletas de cores.")
                break
        return



    def FilterImage(self):
        if self.imageBytes is None:
            print("\t[!] Imagem não carregada.")
            return

        os.system("cls || clear") # Limpa-tela MEAN, MEDIAN, SOBEL, GAUSSIAN, LAPLACIAN
        print("\t [*]Escolha uma opção de filtro: ")
        print("\t\t 1 -- Média")
        print("\t\t 2 -- Mediana")
        print("\t\t 3 -- Sobel")
        print("\t\t 4 -- Gaussiano")
        print("\t\t 5 -- Laplaciano")
        print("\t\t 6 -- Sair")

        opt = -1
        while ((opt < 0) or (opt > 6)):
            print("Escolha: ", end="")
            opt = int(input())
            cg_colors = None
            min_th_value = -1
            max_th_value = -1

            if(opt == 1):
                while ((min_th_value < 0) or (max_th_value < 0) or (min_th_value > 255) or (max_th_value > 255)):
                    min_th_value = int(input("Mínimo valor de Threshold: "))
                    max_th_value = int(input("Máximo valor de Threshold: "))

                if self.newImageBytes is None:
                    cg_colors = cv2.blur(self.imageBytes, (min_th_value,max_th_value))
                else:
                    cg_colors = cv2.blur(self.newImageBytes, (min_th_value,max_th_value))
                
                print("\t[!] Aplicando efeito de filtro Médio.")
                self.newImageBytes = cg_colors
                break
            
            if (opt == 2):
                while ((max_th_value < 0) or (max_th_value > 9)):
                    max_th_value = int(input("Máximo valor de Threshold (0-9): "))

                if self.newImageBytes is None:
                    cg_colors = cv2.medianBlur(self.imageBytes, max_th_value)
                else:
                    cg_colors = cv2.medianBlur(self.newImageBytes, max_th_value)
                
                print("\t[!] Aplicando efeito de filtro Mediana.")
                self.newImageBytes = cg_colors
                break


            if (opt == 3):
                while ((max_th_value < 0) or (max_th_value > 9) or (max_th_value % 2 == 0)):
                    max_th_value = int(input("Máximo valor de Threshold (0-31) (Apenas números ímpares): "))

                if self.newImageBytes is None:
                    im_gauss = cv2.GaussianBlur(self.imageBytes, (3,3), cv2.BORDER_DEFAULT)
                    cg_colors = cv2.Sobel(im_gauss, ddepth=cv2.CV_64F, dx=1, dy=1, ksize = max_th_value)
                else:
                    im_gauss = cv2.GaussianBlur(self.newImageBytes, (3,3), cv2.BORDER_DEFAULT)
                    cg_colors = cv2.Sobel(im_gauss, ddepth=cv2.CV_64F, dx=1, dy=1, ksize = max_th_value)
                

                print("\t[!] Aplicando efeito de filtro Sobel.")
                self.newImageBytes = cg_colors
                break


            
            if (opt == 4):
                while ((min_th_value < 0) or (max_th_value < 0) or (min_th_value > 10) or (max_th_value > 10)):
                    min_th_value = int(input("Mínimo valor de Threshold (0-10): "))
                    max_th_value = int(input("Máximo valor de Threshold (0-10): "))

                if self.newImageBytes is None:
                    cg_colors = cv2.GaussianBlur(self.imageBytes, (min_th_value,max_th_value), cv2.BORDER_DEFAULT)
                else:
                    cg_colors = cv2.GaussianBlur(self.newImageBytes, (min_th_value,max_th_value), cv2.BORDER_DEFAULT)
                
                print("\t[!] Aplicando efeito de filtro Gaussiano.")
                self.newImageBytes = cg_colors
                break




            if (opt == 5):
                kernel = -1
                while ((min_th_value < 0) or (kernel < 0)or (kernel >64) or (max_th_value < 0) or (min_th_value > 10) or (max_th_value > 10)):
                    min_th_value = int(input("Mínimo valor de Threshold (0-10): "))
                    max_th_value = int(input("Máximo valor de Threshold (0-10): "))
                    kernel = int(input("Máximo valor do Kernel (0-64): "))

                if self.newImageBytes is None:
                    im_gauss = cv2.GaussianBlur(self.imageBytes, (min_th_value, max_th_value), cv2.BORDER_DEFAULT)
                    cg_colors = cv2.Laplacian(im_gauss, ddepth= cv2.CV_64F)
                else:
                    im_gauss = cv2.GaussianBlur(self.imageBytes, (min_th_value, max_th_value), cv2.BORDER_DEFAULT)
                    cg_colors = cv2.Laplacian(im_gauss, ddepth= cv2.CV_64F)
                
                print("\t[!] Aplicando efeito de filtro Laplaciano.")
                self.newImageBytes = cg_colors
                break


            if (opt == 6):
                print("\t [*] Saindo dos filtros.")
                break




    def ShowHistogram(self):
        if self.imageBytes is None:
            print("\t[!] Imagem não carregada.")
            return

        os.system("cls || clear") # Limpa-tela 
        print("\t [*]Escolha uma opção de Hisograma: ")
        print("\t\t 1 -- RGB")
        print("\t\t 2 -- Monocromático")
        print("\t\t 3 -- Sair")

        opt = -1
        while ((opt < 0) or (opt > 3)):
            print("Escolha: ", end="")
            opt = int(input())
            hist = None
            min_th_value = -1
            max_th_value = -1

            if(opt == 1):

                if self.newImageBytes is None:
                    hist = cv2.calcHist(self.imageBytes, channels=[0], mask=None, histSize=[256], ranges=[0,256])
                else:
                    hist = cv2.calcHist(self.newImageBytes, channels=[0], mask=None, histSize=[256], ranges=[0,256])
                
                print("\t[!] Visualizando Histograma.")
                
                hist /= hist.sum() # Normaliza-se o Histograma.
                plt.figure()
                plt.title("Histograma (Normalizado)")
                plt.xlabel("Binários")
                plt.ylabel("% \\de pixels")
                plt.plot(hist)
                plt.xlim([0,256])
                plt.show()
                break
            
            if(opt == 2):
                
                # Irá transformar a imagem em Preto e Branco para realizar o histograma monocromático.
                if self.newImageBytes is None:
                    bw_img = cv2.cvtColor(self.imageBytes, cv2.COLOR_RGB2GRAY)
                    hist = cv2.calcHist(bw_img, channels=[0], mask=None, histSize=[256], ranges=[0,256])
                else:
                    bw_img = cv2.cvtColor(self.imageBytes, cv2.COLOR_RGB2GRAY)
                    hist = cv2.calcHist(bw_img, channels=[0], mask=None, histSize=[256], ranges=[0,256])
                
                print("\t[!] Visualizando Histograma.")
                
                hist /= hist.sum() # Normaliza-se o Histograma.
                plt.figure()
                plt.title("Histograma Preto e Branco(Normalizado)")
                plt.xlabel("Binários")
                plt.ylabel("% \\de pixels")
                plt.plot(hist)
                plt.xlim([0,256])
                plt.show()
                break
                
            
            
            if(opt == 3):
                print("\t[*] Saindo do modo Histograma.")
                break
        return





    def SaveProcessedImage(self):
        if self.newImageBytes is not None: 
            filename = ""
            while filename == "":
                filename = str(input("Digite o nome do arquivo: "))

            file_already_exists = exists(filename)
            if file_already_exists:
                print("\t [!!!] Arquivo já existente, deseja sobrescrever?")
                opt = ""
                while True:
                    print("Escolha (Y\\N): ", end="")
                    opt = str(input())
                    if(opt.lower() == 'y'):
                        os.remove(filename)
                        break
                    if(opt.lower() == 'n'):
                        return
            
            print(f"\t\n[!!!] Imagem salva em {str(os.path.abspath('.'))}\\{filename}.png")
            cv2.imwrite(filename+'.png', self.newImageBytes)
            self.savedImage = True
            return

        else:
            print("\t[!] Não há imagem processada para ser salva.")
        
        return






    def ShowFinalImage(self):
        if self.newImageBytes is None:
            print("\t[!] Não há imagem para mostrar.")
            return

        cv2.imshow('Imagem processada',self.newImageBytes)
        cv2.waitKey(0)
        return






    def ExitProgram(self):
        if self.savedImage is False:
            print("\t[!!] Você ainda não salvou alterações desta imagem, deseja mesmo encerrar o programa? ")
            opt = ""
            while True:
                print("Escolha (Y\\N): ", end="")
                opt = str(input())
                if(opt.lower() == 'y'):
                    sys.exit(0)
                if(opt.lower() == 'n'):
                    break
        else:
            sys.exit(0)
            


 # =================================================== #



def main():
    img = Image()
    while True:
        opt = menu.main()
        
        if opt == "<ChangeColorPalletes>":
            img.ChangeColorPalletes()

        if opt == "<SaveProcessedImage>":
            img.SaveProcessedImage()
            
        if opt == "<ShowHistogram>":
            img.ShowHistogram()   
        
        if opt == "<BinarizeImage>":
            img.BinarizeImage()

        if opt == "<LoadImage>":
            img.LoadImage()
        
        if opt == "<ApplyFilters>":
            img.FilterImage() 

        if opt == "<UndoImage>":
            img.UndoImage()

        if opt == "<DetectBorderCanny>":
            img.DetectBorder()

        if opt == "<ShowFinalImage>":
            img.ShowFinalImage()

        if opt == "<ExitProgram>":
            img.ExitProgram()

            
    
if __name__ == '__main__':
    os.system("cls || clear")
    main()

