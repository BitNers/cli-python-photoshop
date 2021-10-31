import menu
import sys
import os.path
import cv2



class Image:
    
    def __init__(self):
        self.imageBytes    = None
        self.newImageBytes = None


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
        
        
    def SaveProcessedImage(self):
        return True


    def ExitProgram(self):
        if self.newImageBytes is not None:
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
            




def main():
    img = Image()
    while True:
        opt = menu.main()
        print(opt)
        
        if opt == "<SaveProcessedImage>":
            img. SaveProcessedImage()
        
        if opt == "<LoadImage>":
            img.LoadImage()
        
        if opt == "<ExitProgram>":
            img.ExitProgram()
    
if __name__ == '__main__':
    # Definindo codificação UTF-8 para o projeto
    main()

