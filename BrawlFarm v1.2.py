import pyautogui as pg
import time
import random
import pygetwindow as gw
import threading
import tkinter as tk
#final beta version
def create_window():
    # Vytvoření okna
    wn = tk.Tk()
    # Nastavení názvu okna
    wn.title("Bot Farm Aming Fov")
    # Nastavení rozměrů okna
    wn.geometry("500x500")
    # Zakázání možnosti změny velikosti okna
    wn.resizable(False, False)
    #transparent
    wn.attributes("-alpha", 0.5)
    # Výpočet souřadnic pro umístění křížku (střed okna)
    x_center = 500 // 2
    y_center = 500 // 2
    # Vytvoření křížku na canvasu
    canvas = tk.Canvas(wn, width=500, height=500)
    canvas.pack()
    # Vykreslení horizontální a vertikální čáry pro křížek
    canvas.create_line(0, y_center, 500, y_center, fill="black")
    canvas.create_line(x_center, 0, x_center, 500, fill="black")

    # Nastavení pozice okna do středu obrazovky
    screen_width = wn.winfo_screenwidth()
    screen_height = wn.winfo_screenheight()
    x_position = (screen_width - 500) // 2
    y_position = (screen_height - 500) // 2
    wn.geometry(f"+{x_position}+{y_position}")

    # run onec
    wn.mainloop()


def Main():
    print("Afk Bot working...")    # Zobrazení dialogového okna s tlačítkem OK
    create_window()
    pg.alert("Klick OK to start the bot.")

    while True:
        # Spuštění funkce
        run_functions_concurrently()


def run_functions_concurrently():
    # Vytvoření vláken pro funkce 'stupid_shoot' a 'afk_stupid'
    thread1 = threading.Thread(target=stupid_shoot)
    thread2 = threading.Thread(target=afk_stupid)
    thread3 = threading.Thread(target=accept)

    # Spuštění vláken
    thread1.start()
    thread2.start()
    thread3.start()

    # Počkání na dokončení obou vláken
    thread1.join()
    thread2.join()

def get_resolution():
    # Získání rozlišení obrazovky
    width, height = pg.size()
    print(f"Rozlišení obrazovky: {width}x{height}")
    return width, height

def rand(x,y):
    return random.randint(x,y)

def stupid_shoot():
    # Definice souřadnic a rozměrů čtvercové oblasti (FOV)
    fov_x = 960  # X souřadnice středu oblasti
    fov_y = 540  # Y souřadnice středu oblasti
    fov_size = 500  # Velikost oblasti (šířka a výška čtverce)

    # Očekávaná barva pixelu, kterou chcete kontrolovat uvnitř FOV
    expected_color = (233, 22, 47)

    # Tolerance pro porovnání barev
    tolerance = 60

    # Získání snímku celé oblasti FOV
    fov_screen = pg.screenshot(region=(fov_x - fov_size // 2, fov_y - fov_size // 2, fov_size, fov_size))

    # Procházení každého pixelu uvnitř FOV a kontrola barvy
    for x in range(fov_size):
        for y in range(fov_size):
            # Získání barvy pixelu
            pixel_color = fov_screen.getpixel((x, y))

            # Kontrola, zda je rozdíl mezi každou složkou (R, G, B) očekávané barvy a skutečné barvy pixelu menší nebo roven toleranci
            if all(abs(expected - actual) <= tolerance for expected, actual in zip(expected_color, pixel_color)):
                # Pokud ano, stiskněte tlačítko 'f'
                pg.keyDown('f')
                time.sleep(0.2)  # Počkejte krátkou dobu, než uvolníte tlačítko 'f'
                pg.keyUp('f')  # Uvolnění tlačítka 'f'
                return  # Ukončení funkce po prvním nalezení požadované barvy

def press_key(x, y, expected_color, tolerance, key):
    # Získání barvy pixelu na zadaných souřadnicích
    pixel_color = pg.pixel(x, y)

    # Kontrola, zda je rozdíl mezi každou složkou (R, G, B) očekávané barvy a skutečné barvy pixelu menší nebo roven toleranci
    if all(abs(expected - actual) <= tolerance for expected, actual in zip(expected_color, pixel_color)):
        # Pokud ano, stiskněte klávesu 'f'
        pg.press(key)

def accept():
    press_key(1470,723, (224,186,8), 40, 'f')
    press_key(1289,726, (239,198,9), 30, 'f')
    press_key(1289, 726, (35, 115, 255), 10, 'f')
    press_key(1362,728, (33,108,239), 10, 'f')

def afk_stupid():
    pg.keyDown('w')
    time.sleep(rand(1,3))
    pg.keyUp("w")
    pg.keyDown('a')
    time.sleep(rand(1,1))
    pg.keyUp("a")
    pg.keyDown('d')
    time.sleep(rand(1,3))
    pg.keyUp("d")
    pg.keyDown('s')
    time.sleep(rand(1, 3))
    pg.keyUp("s")

Main()  # Spustit hlavní funkci při spuštění skriptu

