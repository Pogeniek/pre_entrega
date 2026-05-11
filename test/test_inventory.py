from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver_logged(login_in_driver):
    # Guarda login_in_driver en una variable y la retorna.
    driver = login_in_driver
    return driver

def test_inventory_title(driver_logged):
    # Guarda el titulo de la pagina en una variable y lo compara con el titulo esperado.
    titulo = driver_logged.title
    assert titulo == "Swag Labs", "El titulo de la pagina a la que se accede no es correcto"

def test_productos_visibles(driver_logged):
    # Captura la lista de productos en una variable y compara que la lista sea mayor que cero.
    productos = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(productos) > 0

def test_ui_elements(driver_logged):
    # Guarda el menu "burger" y el menu "filtro" en sendas variable y verifica que sean visibles. 
    menu = driver_logged.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed(), "El icono del menu no está presente en la pagina"
    assert filtro.is_displayed(), "El filtro del catalogo no está presente en la pagina"