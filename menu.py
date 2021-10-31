import sys


class Menu:
    def Menu_LoadImage():
        return "<LoadImage>"
        
    def Menu_BinarizeImage():
        print("Opção Um Selecionada")
        
    def Menu_ChangeColorPalletes():  # TONS DE CINZA, HSV, HSL, YCrCb
        print("Opção Um Selecionada")
        
    def Menu_ShowHistrogram():       # MONOCROMATIC / RGB
        print("Opção Um Selecionada")
        
    def ShowHistogramMonochromatic():
        print("Show histogram")
        
    def ShowHistogramRGB():
        print("Opção Um Selecionada")
    
    def Menu_Filters():              # MEAN, MEDIAN, SOBEL, GAUSSIAN, LAPLACIAN
        print("Opção Um Selecionada")
        
    def MeanFilter():
        print("Opção Um Selecionada")
        
    def MedianFilter():
        print("Opção Um Selecionada")
    
    def SobelFilter():
        print("Opção Um Selecionada")

    def GaussianFilter():
        print("Opção Um Selecionada")
    
    def LaplacianFilter():
        print("Opção Um Selecionada")
        
    def Menu_DetectBorders():             # Using Canny Method
        print("Opção Um Selecionada")
    
    def Menu_SaveProcessedImage():
        return "<SaveProcessedImage>"
    
    def Exit():
        return "<ExitProgram>"


    def generate_menu():
        idx = 1
        print("================================")
        do_methods = [m for m in dir(Menu) if m.startswith('Menu_')]
        for items in do_methods:
            print(f"\t {idx} -- { items.replace('Menu_', '') }")
            idx+=1
        print(f"\t {idx+1} -- Sair do programa")
        print("================================")
        print("Insira a opção a number: ", end="")


    def execute(user_input):
        
        if user_input == 5:
            return Menu.Menu_LoadImage()
        
        if user_input == 8:
            print("8")
        
        if user_input == 9:
            return Menu.Exit()
            
    

    def run():
        user_input = 0
        while(user_input != 9):
            user_input = int(input())
            if user_input is None:
                user_input = 0
            return Menu.execute(user_input)
        print("Encerrando...")




def main():
    Menu.generate_menu()
    return Menu.run()
    

if __name__ == '__main__':
    sys.os("cls || clear")
    print("\t[#] Executing Menu Python...")
    main()