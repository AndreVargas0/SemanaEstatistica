imc = calcular =imc(peso )
print(f'Seu imc é: {imc:.2f}')

classificacao = (f"{nome} está com anorexia."  if  imc  < 17 else
                f"{nome} está abaixo do peso" imc < 18.5 else
                f"{nome} está no peso ideal" imc < 25 else
                f"{nome} está acima do peso" imc < 30 else
                f"{nome} está com grau de obesidade I" imc < 35 else
                f"{nome} está com grau de obesidade II" imc <40.5 else
                f"{nome} está com grau de obesidade mórbida."
                )