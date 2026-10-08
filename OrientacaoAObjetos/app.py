from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Arthur', 10)
restaurante_praca.receber_avaliacao('Andre', 10)




def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()