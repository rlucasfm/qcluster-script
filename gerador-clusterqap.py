from pyautogui import *
import pyautogui
import time


def main():
    """ Abrir o menu de Consulta Personalizada """
    try:
        consulta_btn = pyautogui.locateCenterOnScreen('images/consulta_personalizada.png')  
    except ImageNotFoundException:
        print('Botão de "Consulta Personalizada" não encontrado')
    pyautogui.click(consulta_btn)
    time.sleep(0.5)
    
    """ Selecionar Filtros de Ano """
    while True:
        try:
            ano_proposta_btn = pyautogui.locateCenterOnScreen('images/ano_proposta.png')
            break;
        except ImageNotFoundException:
            print('Botão de "Ano Proposta" não encontrado')
    pyautogui.click(ano_proposta_btn)
    time.sleep(0.1)
    pyautogui.write('2023')
    time.sleep(1)
    pyautogui.click(370, 485)
    pyautogui.click(395, 407)
    time.sleep(0.5)
    
    """ Selecionar Filtros de Uf """
    while True:
        try:
            uf_btn = pyautogui.locateCenterOnScreen('images/uf.png')
            break;
        except ImageNotFoundException:
            print('Botão de "UF" não encontrado')
    pyautogui.click(uf_btn)
    time.sleep(0.1)
    pyautogui.write('MA')
    time.sleep(1)
    pyautogui.click(200, 618)
    pyautogui.click(395, 543)
    
    time.sleep(0.5)
    pyautogui.scroll(-150)
    time.sleep(1)
    
    """ Selecionar Dimensões """
    try:
        modalidade_dim = pyautogui.locateCenterOnScreen('images/modalidade.png')
        pyautogui.click(modalidade_dim)
        print('modalidade encontrada')
        time.sleep(0.5)
        
        orgao_concedente_dim = pyautogui.locateCenterOnScreen('images/orgao_concedente.png')
        pyautogui.click(orgao_concedente_dim)
        print('orgao concedente encontrado')
        time.sleep(0.5)
        
        uf_dim = pyautogui.locateCenterOnScreen('images/uf_dimensao.png')
        pyautogui.click(uf_dim)
        print('UF encontrado')
        time.sleep(0.5)
        
        municipio_dim = pyautogui.locateCenterOnScreen('images/municipio.png')
        pyautogui.click(municipio_dim)
        print('Municipio encontrado')
        time.sleep(0.5)
    except ImageNotFoundException:
        print('Dimensão não encontrada')
        
    time.sleep(1)
    pyautogui.click(1442, 383)
    
    """ Selecionar Métricas """
    pyautogui.moveTo(1930, 600)
    time.sleep(0.5)
    pyautogui.scroll(-1000)
    time.sleep(1)
    
    try:
        vl_emenda = pyautogui.locateCenterOnScreen('images/vl_emenda.png')
        pyautogui.click(vl_emenda)
        print('vl_emenda encontrado')
        time.sleep(0.5)
        
        qtd_medicoes = pyautogui.locateCenterOnScreen('images/qtd_medicoes.png')
        pyautogui.click(qtd_medicoes)
        print('qtd_medições')
        time.sleep(0.5)
        
        dias_sem_medicao = pyautogui.locateCenterOnScreen('images/dias_sem_medicao.png')
        pyautogui.click(dias_sem_medicao)
        print('dias_sem_medicao')
        time.sleep(0.5)
    except ImageNotFoundException:
        print('Métrica não encontrada')
        
    time.sleep(1)
    pyautogui.click(2375, 308)
    
    
if __name__ == "__main__":
    # time.sleep(2)
    main()

