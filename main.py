from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
import time


#Eleccion de Navegador
def tipoNavegador():
    opc=int(input("Escoja el número del navegador:\n1.Chrome\n2.Edge\nOpcion>"))
    if opc<1 or opc>2:
        tipoNavegador()
    return opc

def navegador(opc):
    if opc==1:
        op=Options()
        #Para que no aparezca el error de chrome
        op.add_experimental_option('excludeSwitches',['enable-logging'])

        driver= webdriver.Chrome(options=op,executable_path='drivers/chromedriver.exe')
    elif opc==2:
        options=EdgeOptions()
        #para no abrir el navegador
        #options.add_argument("headless") 

        options.add_argument("disable-gpu")
        options.use_chromium=True

        driver=Edge(options=options,executable_path='drivers/msedgedriver.exe')

    return driver



def tweet(d):

    #Imprimo el contenido de dentro del tweet
    texto_tweet=d.find_element_by_xpath('./div[2]/div[2]/div[1]/div/span')
    print(f"\n {texto_tweet.text}")

    #Imprimo la fecha correspondiente al tweet
    fecha_tweet=d.find_element_by_xpath('./div[2]/div[1]/div/div/div[1]/a')
    print(f"Fecha> {fecha_tweet.text}\n")

    #Obtengo la imagen del tweet
    # Una sola imagen 
    # imagen=d.find_element_by_xpath('./div[2]/div[2]/div[2]/div/div/div/div/a/div/div[2]/div/img').get_attribute("src
   
   
    #Multiples Imagenes
    imagenes=d.find_elements_by_class_name("css-9pa8cd")
    tam=len(imagenes)-1
    if(tam==1):
        src=imagenes[1].get_attribute("src")
        if bool(src):
            print(f"Imagen> {src}")
    else:
        for a in range(1,tam+1):
            src=imagenes[a].get_attribute("src")
            if bool(src):
                print(f"Imagen> {src}")
    print('**********************************************************************************************************\n')




def main(lim,text):
    cont=0
    while True:

        #selecciono el aparcado contenedor del tweet
        div=driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
        for d in div: 
            #Imprimo el contenido de dentro del tweet
            texto_tweet=d.find_element_by_xpath('./div[2]/div[2]/div[1]/div/span')
            texto=texto_tweet.text
            #print(texto,end=f"\n ***{d}***")
            for t in range(len(text)):
                if text[t] in texto.lower():
                    tweet(d)
                elif text[t]=="todos":
                    tweet(d)


        #Para hacer la cantidad de scrolls en la web
        #Realizo 7 para que no se repita los tweets 
        for a in range(7):
            #Muevo uno hacia abajo
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            
        cont+=1
        if cont==lim:
            break
    

    
if __name__ == '__main__':
    #contador para detener la ejecucion del while
    lim=int(input("Coloque el maximo de repeticiones del while> "))

    #Para buscar por palabra
    text=input("Coloque palabra para buscar en los tweets> ").split()

    opc=tipoNavegador()

    driver=navegador(opc)

    #Hace la petición
    driver.get('https://twitter.com/utpfisc')

    #Obtengo el body para asì moverlo con el teclado
    element = driver.find_element_by_tag_name('body')
    main(lim,text)
    time.sleep(3)

    #Cierro el navegador
    driver.close()

