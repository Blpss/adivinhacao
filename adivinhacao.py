import random

print("🎲 Bem-vinda ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 100...")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = input("Qual é o seu palpite? ")
    
    if not tentativa.isdigit():
        print("Por favor, digite um número válido.")
        continue

    tentativa = int(tentativa)
    tentativas += 1

    if tentativa < numero_secreto:
        print("🔼 Muito baixo. Tente novamente.")
    elif tentativa > numero_secreto:
        print("🔽 Muito alto. Tente novamente.")
    else:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
        break