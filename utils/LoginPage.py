
from selenium import webdriver
from selenium.webdriver.common.by import By

def login(driver):
    # Funcion para loguearse con parametros correctos.
    driver.get("https://www.saucedemo.com/")

    # Ingresa usuario.
    usuario = driver.find_element(By.ID,"user-name")
    usuario.send_keys("standard_user")

    # Ingresar contraseña. 
    password = driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")

    # Click en boton.
    boton = driver.find_element(By.ID, "login-button").click()
