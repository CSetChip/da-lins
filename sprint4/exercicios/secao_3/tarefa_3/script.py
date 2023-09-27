import hashlib

def calcular_hash_sha1(entrada):
    return hashlib.sha1(entrada.encode()).hexdigest()

def main():
    while True:
        entrada = input("Digite uma string (ou 'ex' para sair): ")

        if entrada.lower() == 'ex':
            break

        sha1_hash = calcular_hash_sha1(entrada)
        print(f'O hash SHA-1 da entrada é: {sha1_hash}')

if __name__ == "__main__":
    main()
