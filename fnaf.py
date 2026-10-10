mport os
import time
import sys

mapa = [
     "##################################################################################################################",
     "#             $$$     #                                             ===========           ##                     #",
     "#                  $$$#                   #              #                                ##  G                F #",
     "#             #########               #########  ##########         $$$     $$$           ##                     #",
     "#                                     #                   #                               ##000000000000000000000#",
     "@                                     #   $$$   $$$  $$$  #         $$$     $$$           ##                     #",
     "@                                                         #                               ##                     #",
     "#      ######                             $$$   $$$  $$$            $$$     $$$   ##########                     #",
     "#                                                                                                                #",
     "#                                         $$$   $$$  $$$                                                         #",
     "#                                     #                                                                          #",
     "#####                                 #   $$$   $$$  $$$  #                       ##########                     #",
     "#                                     #                   #                                #                     #",
     "#                                     #                   #                                #                     #",
     "#                                     #      #    #       #                                #                     #",
     "########################0000##################    ##############                ############                     #",
     "#          #                                 #    #                                        #                     #",
     "#          0                                                                                                     #",
     "#       $$$#                   $$$                                                                               #",
     "##################################################################################################################",
]

sandbox = [
     "##################################################################################################################",
     "#             $$$     #                                             ===========           ##                     #",
     "#                  $$$#                   #              #                                ##  G                F #",
     "#             #########               #########  ##########         $$$     $$$           ##                     #",
     "#                                     #                   #                               ##000000000000000000000#",
     "@                                     #   $$$   $$$  $$$  #         $$$     $$$           ##                     #",
     "@                                                         #                               ##                     #",
     "#      ######                             $$$   $$$  $$$            $$$     $$$   ##########                     #",
     "#                                                                                                                #",
     "#                                         $$$   $$$  $$$                                                         #",
     "#                                     #                                                                          #",
     "#####                                 #   $$$   $$$  $$$  #                       ##########                     #",
     "#                                     #                   #                                #                     #",
     "#                                     #                   #                                #                     #",
     "#                                     #      #    #       #                                #                     #",
     "########################0000##################    ##############                ############                     #",
     "#          #                                 #    #                                        #                     #",
     "#          0                                                                                                     #",
     "#       $$$#                   $$$                                                                               #",
     "##################################################################################################################",
]

começo = [
    "                                                        ",
    "                    @@@@@@@@@@@@@@@@@@@@@               ",
    "                    @@@@ P y B i t e @@@@               ",
    "                    @@@@@@@@@@@@@@@@@@@@@               ",
    "   #################@@@@@@@@@@@@@@@@@@@@@############## ",
    "   #################################################### ",
    "   #################################################### ",
    "   ###################@@@@@@@@%@@@@@@@################# ",
    "   ###################@----@@@%@@----@################# ",
    "   ###################@----@@@%@@----@################# ",
    "   ###################@@@@@@@@%@@@@@@@################# ",
    "   ###################@@@@@@@@%@@@@@@@################# ",
    "   ###################@@@@@@@@%@@@@@@@################# ",
    "   ###################@@@@@@@@%@@@@@@@################# ",
]

morrer = [
    "#################################################################",
    "#####| / #######0 ######################| ###########| ##########",
    "#####|/  #######| ######################| ###########| ##########",
    "#####|l  #######| ######################| ###########| ##########",
    "#####| l #######| ######################|_____#######|_____######",
    "#################################################################",
]

jumpscare0 = [
    "              ___           ",
    "   $$$       ||/     $$$    ",
    "   $  $$ ########## $$  $   ",
    "    $  ##          ##  $    ",
    "     $$#  --      -- #$$    ",
    "       #  (0)    ($) #      ",
    "    ###_______________###   ",
    "   #==       [O]       ==#  ",
    "    ###    -------    ###   ",
    "      #    |_____|    #     ",
    "       #             #      ",
    "        #############       ",
    "          #     #           ",
]

jumpscare1 = [
    "              ___           ",
    "   $$$       ||/     $$$    ",
    "   $  $$ ########## $$  $   ",
    "    $  ##          ##  $    ",
    "     $$#  --      -- #$$    ",
    "     #  ( 0 )    ( $ ) #    ",
    "    ###_______________###   ",
    "   #==       [O]       ==#  ",
    "    ###    -------    ###   ",
    "      #    |_____|    #     ",
    "       #             #      ",
    "        #############       ",
    "          #     #           ",
]

jumpscare2 = [
    "              ___           ",
    "   $$$       ||/     $$$    ",
    "   $  $$ ########## $$  $   ",
    "    $  ##          ##  $    ",
    "     $$#  --      -- #$$    ",
    "     #  ( 0 )    ( $ ) #    ",
    "    ###_______________###   ",
    "   #==       [O]       ==#  ",
    "    ###    -------    ###   ",
    "      #    |     |    #     ",
    "       #   |_____/   #      ",
    "        #############       ",
    "          #     #           ",
]

secret0 = [
    "                            ",
    "   $$$               $$$    ",
    "   $  $$ ########## $$  $   ",
    "    $  ##          ##  $    ",
    "     $$#  --    ____ #$$    ",
    "       #  (-)  /    | #      ",
    "    ###______ |     |  ###    ",
    "   #==       [______/   ==#   ",
    "    ###    -------     ###   ",
    "      #    |     |     #     ",
    "       #   |_____/     #      ",
    "        #             #       ",
    "        #############       ",
    "          #     #           ",
]

secret1 = [
        "                            ",
    "   $$$               $$$    ",
    "   $  $$ ########## $$  $   ",
    "    $  ##          ##  $    ",
    "     $$#  --    ____ #$$    ",
    "       #  (0)  / *  | #      ",
    "    ###______ |     |  ###    ",
    "   #==       [______/   ==#   ",
    "    ###    -------     ###   ",
    "      #    |     |     #     ",
    "       #   | ====|     #     ",
    "        #  |_____/    #       ",
    "        #############       ",
    "          #     #           ",
]

secret2 = [
    "                            ",
    "   $$$               $$$    ",
    "   $  $$ ########## $$  $   ",
    "    $  ##          ##  $    ",
    "     $$#  --    ____ #$$    ",
    "       #  (0)  / *  | #      ",
    "    ###______ |     |  ###    ",
    "   #==       [______/   ==#   ",
    "    ###     ------     ###   ",
    "      #    /     |_____#     ",
    "       #   |L=====/          ",
    "        #   \=====           ",
    "        ####|             ",
    "          #     #         ",
    ]

fundy = ["🐺"]
fundy = [2, 18]

estranho = ["🤖"]
estranho = [18, 1]

guarda = ["👮"]
guarda = [5, 1]

nova_linha = guarda[0]
nova_coluna = guarda[1]

def poder_andar(linha, coluna):
    if linha < 0 or linha >= len(mapa):
        return False

    if coluna < 0 or coluna >= len(mapa[linha]):
        return False

    if mapa[linha][coluna] in "#&@$":
        return False

    return True

def desenhar_mapa():
    for linha in range(len(mapa)):
        texto = ""

        for coluna in range(len(mapa[linha])):
            if [linha, coluna] == guarda:
                texto += "👮"

            elif [linha, coluna] == fundy:
                texto += "🐺"

            elif [linha, coluna] == estranho:
                  texto += "🤖"

            else:
                texto += mapa[linha][coluna]

        print(texto)

def desenhar_sand():
    for linha in range(len(sandbox)):
        texto = ""

        for coluna in range(len(sandbox[linha])):
            if [linha, coluna] == guarda:
                texto += "👮"

            elif [linha, coluna] == fundy:
                texto += "🐺"

            elif [linha, coluna] == estranho:
                  texto += "🤖"

            else:
                texto += sandbox[linha][coluna]

        print(texto)

def jumpscare():
    os.system("clear")
    for linhas in jumpscare0:
        print(linhas)
        time.sleep(0.1)

    time.sleep(1)
    os.system("clear")

    for linhas in jumpscare1:
        print(linhas)
        time.sleep(0.2)

    time.sleep(2)
    os.system("clear")

    for linhas in jumpscare2:
        print(linhas)
        time.sleep(0.1)
        os.system("clear")

    morte()

def secret():
    os.system("clear")
    for linhas in secret0:
        print(linhas)
        time.sleep(0.1)

    time.sleep(1)
    os.system("clear")

    for linhas in secret1:
        print(linhas)
        time.sleep(0.2)

    time.sleep(2)
    os.system("clear")

    for linhas in secret2:
        print(linhas)
        time.sleep(0.1)

    morte()

def morte():
    time.sleep(1)
    os.system("clear")
    print("\033[91m")
    for linhas in morrer:
        print(linhas)
    print("\033[0m")

def inicio():
    os.system("clear")
    for linhas in começo:
        print(linhas)
        time.sleep(0.1)

os.system("clear")
print("\033[91m")
print("""
█▓▀▀██ █▓▀▀   █▓▀▀   █▓▀▀   █▓▀▀   █▓▀▀   █▓▀▀██ █▓▀▀  ▀▀        █▓▀▀     ▀▀█▓▀▀██ █▓     █▓ ▄▓▀▀█▄ █▓▀▀  
▓▒     ▓▒   ░ ▓▒▄▄ ░ ▓▒   ░ ▓▒   ░ ▓▒     ▓▒     ▓▒   ░   ░      ▓▒         ▓▒     ▓▒   ░ ▓▒ ▓▒   ░ ▓▒    
▒░     ▒░▀▀░▒ ▒░▀▄   ▒░  ░▒ ▒░▀▀░▒ ▒░ ▀░▒ ▒░▀    ▒░  ░▒  ░▒      ▒░▀▀░▒     ▒░     ▒░  ░▒ ▒░ ▒░  ░▒ ▒░▀▀░▒
░      ░   ▒▓ ░   ▒▓ ░   ▒▓ ░   ▒▓ ░   ▒▓ ░      ░   ▒▓  ▒▓          ▒▓     ░█     ░   ▒▓ ░  ░   ▒▓     ▒▓
  ▄▄▓█     ▓█     ▓█     ▓█     ▓█   ▄▄▓█   ▄▄▓█     ▓█  ▓█        ▄▄▓█     ██       ▄▄▓█    ▀ ▄▄▓▀   ▄▄▓█
<apresenta>
""")
print("\033[0m")
time.sleep(5)
os.system("clear")
print("""\033[93m
                                         ▐▓▓▌
▐▓▓▓▓▌▐▓▌ ▐▓▌▐▓▓▓▓▌ ▐▓▓▓▓▓▌▐▓▓▓▓▓▌▐▓▓▓▓▌▐▓▓▌▐▓▓▓▓▌
▐▓▌▐▓▌ ▐▓▐▓▌ ▐▓▌ ▐▓▌  ▐▓▌    ▐▓▌  ▐▓▌       ▐▓▌   
▐▓▓▓▓▌  ▐▓▌  ▐▓▓▓▓▓▌  ▐▓▌    ▐▓▌  ▐▓▓▓▌     ▐▓▓▓▓▌
▐▓▌     ▐▓▌  ▐▓▌ ▐▓▌  ▐▓▌    ▐▓▌  ▐▓▌          ▐▓▌
▐▓▌     ▐▓▌  ▐▓▓▓▓▌ ▐▓▓▓▓▓▌  ▐▓▌  ▐▓▓▓▓▌    ▐▓▓▓▓▌
""")

print("bem vindo ao restalrante PyBite's")
time.sleep(1)
print("vc é o novo segurança do restaurante")
time.sleep(1)
print("  ")
print("      |^| digite J para jogar")
print("      /~/ digite C para ver os créditos")
print("       !  digite E para ver os extras")
print("      ->  digite S para sair")
print("      °.° digite L para ver a lore do jogo (nem ta pronta ainda)")
print("      [$] digite P pra se você quiser apoiar o criador com 10 reais pra baixo")
print("     [<>] digite X para sandbox")
time.sleep(1)
print("   ")
escolher = input("escreva aqui: ").upper()
print("\033[0m")

if escolher == "J":
    inicio()
    time.sleep(1)

    while True:
     os.system("clear")
     desenhar_mapa()

     comando = input("Digite W/A/S/D: ").lower()

     nova_linha = guarda[0]
     nova_coluna = guarda[1]

     if comando == "w":
        nova_linha -= 1

     elif comando == "a":
        nova_coluna -= 1

     elif comando == "s":
        nova_linha += 1

     elif comando == "d":
        nova_coluna += 1

     if comando == "g":
        mapa = [linha.replace("&", "0") for linha in mapa]

     elif comando == "f":
         mapa = [linha.replace("0", "&") for linha in mapa]

     if poder_andar(nova_linha, nova_coluna):
        guarda[0] = nova_linha
        guarda[1] = nova_coluna

     if guarda == estranho:
      secret()
      break

     if guarda == fundy:
      jumpscare()
      break

elif escolher == "C":
    print("\033[96m")
    print("créditos:")
    time.sleep(1)
    print("criador: eu")
    time.sleep(1)
    print("programa feito em Python")
    time.sleep(1)
    print("meu tiktok: @carnagem1hk")
    time.sleep(1)
    print("\033[0m")
    os.system("exit")
elif escolher == "P":
    print("\033[42m")
    print("meu numero é +55 48984850927")
    time.sleep(1)
    print("não é obrigatório pagar mas se tu quiser")
    time.sleep(1)
    print("só mande menos 10 rais por que eu não gosto de prejudicar os outros")
    print("\033[0m")

elif escolher == "X":
    inicio()
    time.sleep(1)

    while True:
     os.system("clear")
     desenhar_sand()

     comando = input("Digite W/A/S/D: ").lower()

     nova_linha = guarda[0]
     nova_coluna = guarda[1]

     if comando == "w":
        nova_linha -= 1

     elif comando == "a":
        nova_coluna -= 1

     elif comando == "s":
        nova_linha += 1

     elif comando == "d":
        nova_coluna += 1

     if comando == "11002":
         morte()

     elif comando == "54364":
         inicio()

     if comando == "g":
        mapa = [linha.replace("0", "&") for linha in mapa]

     elif comando == "f":
         mapa = [linha.replace("&", "0") for linha in mapa]

     if poder_andar(nova_linha, nova_coluna):
        guarda[0] = nova_linha
        guarda[1] = nova_coluna

     if guarda == estranho:
      secret()
      break

     if guarda == fundy:
      jumpscare()
      break

elif escolher == "E":
    print("extras:")
    time.sleep(1)
    print("mapa do jogo")
    time.sleep(1)
    print("""
     ################################
     #               #         #    #
     #               #         #G  F#
     #         #######         #    #
     #                         #0000#
     @              #####      #    #
     @                         #    #
     #      ######          ####    #
     #                              #
     ######                 ####    #
     #    0                         #
     ################################
""")

    print("jumpscare do animatronico")
    print("fundy")
    time.sleep(1)
    print("""
                  ___           
       $$$       ||/     $$$    
       $  $$ ########## $$  $   
        $  ##          ##  $    
         $$#  --      -- #$$    
           #  (0)    ($) #      
        ###_______________###   
       #==       [O]       ==#  
        ###    -------    ###   
          #    |_____|    #     
           #             #      
            #############       
              #     #           
""")

    print("""
              ___           
   $$$       ||/     $$$    
   $  $$ ########## $$  $   
    $  ##          ##  $    
     $$#  --      -- #$$    
     #  ( 0 )    ( $ ) #    
    ###_______________###   
   #==       [O]       ==#  
    ###    -------    ###   
      #    |_____|    #     
       #             #      
        #############       
          #     #           
""")

    print("""
                  ___           
       $$$       ||/     $$$    
       $  $$ ########## $$  $   
        $  ##          ##  $    
         $$#  --      -- #$$    
         #  ( 0 )    ( $ ) #    
        ###_______________###   
       #==       [O]       ==#  
        ###    -------    ###   
          #    |     |    #     
           #   |_____/   #      
            #############       
              #     #          
""")

    print("???")

    print("""
                                
       $$$               $$$    
       $  $$ ########## $$  $   
        $  ##          ##  $    
         $$#  --    ____ #$$    
           #  (-)  /    | #      
         ###______ |     |  ###    
       #==       [______/   ==#   
        ###    -------     ###   
          #    |     |     #     
           #   |_____/     #      
            #             #       
            #############       
              #     #           


                                    
       $$$               $$$    
       $  $$ ########## $$  $   
        $  ##          ##  $   
         $$#  --    ____ #$$    
           #  (0)  / *  | #      
        ###______ |     |  ###    
       #==       [______/   ==#   
        ###    -------     ###   
          #    |     |     #     
           #   | ====|     #     
            #  |_____/    #       
            #############       
              #     #           


                                
       $$$               $$$    
       $  $$ ########## $$  $   
        $  ##          ##  $    
         $$#  --    ____ #$$    
           #  (0)  / *  | #      
        ###______ |     |  ###    
       #==       [______/   ==#   
        ###     ------     ###   
          #    /     |_____#     
           #   |L=====/          
            #   |=====           
            ####|             
              #     #         
""")

elif escolher == "S":
    sys.exit()

elif escolher == "L":
    print("lore do jogo:")
    time.sleep(1)
    print("o jogo se passa em um restaurante de animatronicos")
    time.sleep(1)
    print("o restaurante é chamado de PyBite's")
    time.sleep(1)
    print("o restaurante foi fechado por causa de um acidente com um animatronico")
    time.sleep(1)
    print("o animatronico matou um dos funcionários do restaurante")
    time.sleep(1)
    print("o animatronico é chamado de fundy")
    time.sleep(1)
    print("mas fundy não é o único animatronico do restaurante")
    time.sleep(1)
    print("e a sua função é sobreviver a noite no restaurante e manter o restaurante seguro durante a noite")
    time.sleep(1)
    print("mas não se preucupe apenas um dos animatronicos é perigoso o outro esta desativado a anos")
    time.sleep(1)
    print("o jogo sera visto de cima e de uma forma amigavél mas não se engane pelos emogis os jumpscares são reais")
    time.sleep(1)
    print("não dão medo por que é tudo feito em caractéres")
    time.sleep(3)
    sys.exit()

else:
    print("tax tolo, tirou isso da onde?")
    time.sleep(1)
    os.system("exit")
