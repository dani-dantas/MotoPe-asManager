# src/main.py

from gerenciador_estoque import atualizar_estoque, verificar_estoque
from sistema_alerta import enviar_alerta_estoque
from leitor_qr_code import ler_qr_code

def main():
    # Simulação de leitura de QR Code
    codigo_produto = ler_qr_code('data/sample_images/qr_code_example.png')
    
    if codigo_produto:
        # Atualiza o estoque
        atualizar_estoque(codigo_produto, quantidade_vendida=1)
        
        # Verifica o estoque atual e envia alerta se estiver baixo
        quantidade_atual = verificar_estoque(codigo_produto)
        if quantidade_atual < 10:
            enviar_alerta_estoque(codigo_produto, quantidade_atual)

if __name__ == "__main__":
    main()
