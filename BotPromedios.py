from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

print("PROMEDIOS")
ciclo_prgs = input("Ciclo PRGS: ")
ciclo_cpex = input("Ciclo CPEX: ")

service = Service(executable_path="C:\ChromeDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://")

#INGRESAR AL PEOPLE
people_usuario = driver.find_element(By.XPATH,'//*[@id="userid"]')
people_usuario.send_keys("")
people_contra = driver.find_element(By.XPATH,'//*[@id="pwd"]')
people_contra.send_keys("")
people_conectar = driver.find_element(By.XPATH,'//*[@id="form"]/form/div[2]/div[4]/button')
people_conectar.click()
time.sleep(3)

#Mis favoritos
driver.find_element(By.XPATH,'//*[@id="fldra_MYFAVORITES"]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="crefli_fav_PT_QUERY_VIEWER_GBL"]/a').click()
time.sleep(1)

#Cambio de frame
driver.switch_to.frame("ptifrmtgtframe")
time.sleep(1)

def prgs():
    
    time.sleep(2)
    #Buscar Query
    buscar_query = driver.find_element(By.XPATH,'//*[@id="QRY_VIEWERS_WRK_QRYSEARCHTEXT254"]')
    buscar_query.clear()
    buscar_query.send_keys("SISE_NOTAS_PROMED_QRY_V02")
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="QRY_VIEWERS_WRK_QRYSEARCHBTN"]').click()
    time.sleep(1)

    #Programar
    driver.find_element(By.XPATH,'//*[@id="QRY_VIEWERS_WRK_QRYSCHEDULE$0"]').click()
    time.sleep(1)

    #Criterios de busqueda
    consulta_p = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_QRYVW_PRIVATE_QUERY_FLAG"]')
    consulta_p.clear()
    consulta_p.send_keys("N")
    
    nombre_consulta = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_QRYVW_QRYNAME"]')
    nombre_consulta.clear()
    nombre_consulta.send_keys("SISE_NOTAS_PROMED_QRY_V02")
    
    id_control = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_QRYVW_RUN_CNTL_ID"]')
    id_control.clear()
    id_control.send_keys("1")
    
    #Buscar
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="#ICSearch"]').click()
    time.sleep(2)

    #Parametros
    inst = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_PARM_BNDVALUE$0"]')
    inst.clear()
    inst.send_keys("SISE")

    acad = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_PARM_BNDVALUE$1"]')
    acad.clear()
    acad.send_keys("PRGS")
    
    strm = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_PARM_BNDVALUE$2"]')
    strm.clear()
    strm.send_keys(ciclo_prgs)

    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="#ICSave"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="#ICSave"]').click()
    time.sleep(2)


def cpex():
    
    time.sleep(2)
    #Buscar Query
    buscar_query = driver.find_element(By.XPATH,'//*[@id="QRY_VIEWERS_WRK_QRYSEARCHTEXT254"]')
    buscar_query.clear()
    buscar_query.send_keys("SISE_NOTAS_PROMED_QRY_V02")
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="QRY_VIEWERS_WRK_QRYSEARCHBTN"]').click()
    time.sleep(1)

    #Programar
    driver.find_element(By.XPATH,'//*[@id="QRY_VIEWERS_WRK_QRYSCHEDULE$0"]').click()
    time.sleep(1)

    #Criterios de busqueda
    consulta_p = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_QRYVW_PRIVATE_QUERY_FLAG"]')
    consulta_p.clear()
    consulta_p.send_keys("N")
    
    nombre_consulta = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_QRYVW_QRYNAME"]')
    nombre_consulta.clear()
    nombre_consulta.send_keys("SISE_NOTAS_PROMED_QRY_V02")
    
    id_control = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_QRYVW_RUN_CNTL_ID"]')
    id_control.clear()
    id_control.send_keys("SISE")
    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="#ICSearch"]').click()
    time.sleep(2)

    #Parametros
    inst = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_PARM_BNDVALUE$0"]')
    inst.clear()
    inst.send_keys("SISE")

    acad = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_PARM_BNDVALUE$1"]')
    acad.clear()
    acad.send_keys("CPEX")

    strm = driver.find_element(By.XPATH,'//*[@id="QUERY_RUN_PARM_BNDVALUE$2"]')
    strm.clear()
    strm.send_keys(ciclo_cpex)
    
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="#ICSave"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="#ICSave"]').click()
    time.sleep(2)

contador = 0

if ciclo_prgs != "":
    prgs()
    contador = contador + 1

if ciclo_cpex != "":
    cpex()
    contador = contador + 1

time.sleep(2)

#Frame principal
driver.switch_to.default_content()
driver.find_element(By.XPATH,'//*[@id="crefli_fav_PT_PROCESSMONITOR_GBL"]/a').click()

#iFrame
time.sleep(1)
driver.switch_to.frame("ptifrmtgtframe")

#Verificacion correcto y enviado

if contador >= 1:
    while True:
        time.sleep(10)
        driver.find_element(By.XPATH,'//*[@id="REFRESH_BTN"]').click()
        time.sleep(5)
        if driver.find_element(By.XPATH,'//*[@id="PMN_PRCSLIST_RUNSTATUSDESCR$0"]').text == "Correcto" and driver.find_element(By.XPATH,'//*[@id="PMN_PRCSLIST_DISTSTATUS$0"]').text == "Enviado":
            break
    if contador >= 2:
        while True:
           time.sleep(5)
           driver.find_element(By.XPATH,'//*[@id="REFRESH_BTN"]').click()
           time.sleep(5)
           if driver.find_element(By.XPATH,'//*[@id="PMN_PRCSLIST_RUNSTATUSDESCR$1"]').text == "Correcto" and driver.find_element(By.XPATH,'//*[@id="PMN_PRCSLIST_DISTSTATUS$1"]').text == "Enviado":
               break
    

if contador >= 1:
   #Descargar querys
   time.sleep(2)
   driver.find_element(By.XPATH,'//*[@id="PRCSDETAIL_BTN$0"]').click()
   time.sleep(2)
   driver.find_element(By.XPATH,'//*[@id="PMN_DERIVED_INDEX_BTN"]').click()
   time.sleep(1)
   driver.find_element(By.XPATH,'//*[@id="URL$1"]').click()
   time.sleep(1)
   driver.find_element(By.XPATH,'//*[@id="#ICCancel"]').click()
   time.sleep(1)
   driver.find_element(By.XPATH,'//*[@id="#ICCancel"]').click()
   
   if contador >= 2:
       #Descargar querys
       time.sleep(2)
       driver.find_element(By.XPATH,'//*[@id="PRCSDETAIL_BTN$1"]').click()
       time.sleep(2)
       driver.find_element(By.XPATH,'//*[@id="PMN_DERIVED_INDEX_BTN"]').click()
       time.sleep(1)
       driver.find_element(By.XPATH,'//*[@id="URL$1"]').click()
       time.sleep(1)
       driver.find_element(By.XPATH,'//*[@id="#ICCancel"]').click()
       time.sleep(1)
       driver.find_element(By.XPATH,'//*[@id="#ICCancel"]').click()

time.sleep(16)

driver.close()

#Cambio de nombre de archivo
direccion = r"C:\Users\lcardoso\Downloads"

lista_archivos = os.listdir(direccion)
# Ordenar la lista de archivos por fecha de modificación
lista_archivos_ordenados = sorted(lista_archivos, key=lambda x: os.path.getmtime(os.path.join(direccion, x)))

ultimo_archivo = lista_archivos_ordenados[-1]
penultimo_archivo = lista_archivos_ordenados[-2]

ult_nuevo_nombre = f"SISE_NOTAS_PROMED_QRY_V02-PRGS-{ciclo_prgs}.csv"
pult_nuevo_nombre = f"SISE_NOTAS_PROMED_QRY_V02-CPEX-{ciclo_cpex}.csv"

ruta_original = os.path.join(direccion, ultimo_archivo)
nueva_ruta = os.path.join(direccion,ult_nuevo_nombre)
os.rename(os.path.join(direccion, ultimo_archivo), nueva_ruta)

ruta_original2 = os.path.join(direccion, penultimo_archivo)
nueva_ruta2 = os.path.join(direccion,pult_nuevo_nombre)
os.rename(os.path.join(direccion, penultimo_archivo), nueva_ruta2)
