print("===================================================================================================================================")
print("                     Olá programador(a), você foi selecionado para este evento secreto📩📩📩📩📩📩 ")
print("===================================================================================================================================")
def criptografar(texto, chave):
    resultado = ""
    for caractere in texto:
        if caractere.isalpha():
            # Mantém a caixa (maiúscula ou minúscula) do caractere original
            maiuscula = caractere.isupper()
            caractere = chr((ord(caractere) + chave - ord('A' if maiuscula else 'a')) % 26 + ord('A' if maiuscula else 'a'))
        resultado += caractere
    return resultado

def descriptografar(texto, chave):
    return criptografar(texto,-chave)


def main():
    while True:
        modo = input("Você deseja: 'c' para criptografar, 'd' para descriptografar, ou 's' para sair: ").lower()

        if modo == 'c':
            # Leitura do arquivo de entrada
            nome_arquivo = input("Digite o nome do arquivo.txt (Tenha certeza de estar na mesma pasta): ")

            try:
                with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                    texto_original = arquivo.read()
            except FileNotFoundError:
                print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
                continue
            except Exception as e:
                print(f"Erro ao ler o arquivo: {e}")
                continue

            # Solicitação da chave de criptografia
            # Se quiser que o arquivo texto "texto-criptografado.txt" fique igual ao arquivo: "texto-descriptografado.txt" coloque o valor 10
            chave = int(input("Digite a chave de criptografia (um número inteiro): "))

            ### Criptografia
            texto_criptografado = criptografar(texto_original, chave)
            print(f"\nTexto Criptografado:\n{texto_criptografado}\n")

        elif modo == 'd':
            # Leitura do arquivo de entrada
            nome_arquivo = input("Digite o nome do arquivo.txt (Tenha certeza de estar na mesma pasta): ")

            try:
                with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                    texto_criptografado = arquivo.read()
            except FileNotFoundError:
                print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
                continue
            except Exception as e:
                print(f"Erro ao ler o arquivo: {e}")
                continue

            # Solicitação da chave de descriptografia
            chave = int(input("Digite a chave de descriptografia (um número inteiro negativo): "))

            ### Descriptografia
            texto_descriptografado = criptografar(texto_criptografado, chave)  # Usar a mesma chave para descriptografia
            print(f"Texto Descriptografado:\n{texto_descriptografado}")

        ###saida
        elif modo == 's':
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Por favor, escolha 'c', 'd' ou 's'.")

if __name__ == "__main__":
    main()

# ... (código posterior)
print("===================================================================================================================================")
print("👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍")
print("👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻👩🏻‍💻🖱️🧑🏻‍💻")
print("===================================================================================================================================")
