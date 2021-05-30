from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

op=Options()

#Para que no aparezca el error de chrome
op.add_experimental_option('excludeSwitches',['enable-logging'])

driver= webdriver.Chrome(options=op,executable_path='./chromedriver.exe')

driver.get('https://twitter.com/utpfisc')

def main():
    #selecciono el aparcado contenedor del tweet
    div=driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
    print(len(div))

    for d in div: 
        #Imprimo el contenido de dentro del tweet
        texto_tweet=d.find_element_by_xpath('./div[2]/div[2]/div[1]/div/span')   
        print(texto_tweet.text)
        
        #Obtengo la imagen del tweet
        # Una sola imagen 
        # imagen=d.find_element_by_xpath('./div[2]/div[2]/div[2]/div/div/div/div/a/div/div[2]/div/img').get_attribute("src")
        
        #Multiples Imagenes
        imagenes=d.find_elements_by_class_name("css-9pa8cd")
        tam=len(imagenes)-1
        if(tam==1):
            src=imagenes[1].get_attribute("src")
            if bool(src):
                print("Imagen> "+src)
        else:
            for a in range(1,tam+1):
                src=imagenes[a].get_attribute("src")
                if bool(src):
                    print("Imagen> "+src)
        print('********************************************************************************\n')

if __name__ == '__main__':
    main()
    time.sleep(5)
    driver.close()

