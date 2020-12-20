"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    x = float(input("Digite o primeiro número:"))
    y = float(input("Digite o segundo número:"))
    z = float(input("Digite o terceiro número:"))

    if x >= y and x >= z:
      maior = x
    elif y >= x and y >= z:
      maior = y
    else:
      maior = z

    print(f"{maior}")      

if __name__ == '__main__':
    main()
