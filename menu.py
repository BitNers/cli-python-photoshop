import sys


class Menu:
    def Menu_LoadImage():
        return "<LoadImage>"
        
    def Menu_BinarizeImage():
        return "<BinarizeImage>"
        
    def Menu_ChangeColorPalletes():  # TONS DE CINZA, HSV, HSL, YCrCb
        return "<ChangeColorPalletes>"
        
    def Menu_ShowHistrogram():       # MONOCROMATIC / RGB
        return "<ShowHistogram>"

    def Menu_Filters():              # MEAN, MEDIAN, SOBEL, GAUSSIAN, LAPLACIAN
        return "<ApplyFilters>"
        
    def Menu_DetectBorders():             # Using Canny Method
        return "<DetectBorderCanny>"
    
    def Menu_SaveProcessedImage():
        return "<SaveProcessedImage>"
    
    def Menu_ShowFinalImage():
        return "<ShowFinalImage>"

    def Menu_Undo():
        return "<UndoImage>"
    
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
        
        if user_input == 2:
            return Menu.Menu_ChangeColorPalletes()
        
        if user_input == 5:
            return Menu.Menu_LoadImage()
        
        if user_input == 1:
            return Menu.Menu_BinarizeImage()

        if user_input == 7:
            return Menu.Menu_ShowFinalImage()

        if user_input == 6:
            return Menu.Menu_SaveProcessedImage()

        if user_input == 8:
            return Menu.Menu_ShowHistrogram()
        
        if user_input == 4:
            return Menu.Menu_Filters()

        if user_input == 3:
            return Menu.Menu_DetectBorders()

        if user_input == 9:
            return Menu.Menu_Undo()

        if user_input == 11:
            return Menu.Exit()
            
    

    def run():
        user_input = 0
        while(user_input != 11):
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