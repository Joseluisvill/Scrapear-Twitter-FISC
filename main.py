from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


#contador para detener la ejecucion del while
lim=int(input("Coloque el maximo de repeticiones del while> "))


op=Options()

#Para que no aparezca el error de chrome
op.add_experimental_option('excludeSwitches',['enable-logging'])

driver= webdriver.Chrome(options=op,executable_path='./chromedriver.exe')


#abre la web
driver.get('https://twitter.com/utpfisc')

#Obtengo el body para asì moverlo con el teclado
element = driver.find_element_by_tag_name('body')


def main(lim):
    cont=0
    while True:

        #selecciono el aparcado contenedor del tweet
        div=driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
        
        for d in div: 
            #Imprimo el contenido de dentro del tweet
            texto_tweet=d.find_element_by_xpath('./div[2]/div[2]/div[1]/div/span')   
            print(texto_tweet.text)

            #Imprimo la fecha correspondiente al tweet
            fecha_tweet=d.find_element_by_xpath('./div[2]/div[1]/div/div/div[1]/a')
            print(f"Fecha> {fecha_tweet.text}")

            #Obtengo la imagen del tweet

            # Una sola imagen 
            # imagen=d.find_element_by_xpath('./div[2]/div[2]/div[2]/div/div/div/div/a/div/div[2]/div/img').get_attribute("src")

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
    main(lim)
    time.sleep(5)
    driver.close()

