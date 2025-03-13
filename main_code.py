renda_mensal = float(
    input("Digite sua renda mensal: R$")
                     )
essencial = (50 / 100) * renda_mensal
lazer = (30 / 100) * renda_mensal
economia = (20 / 100) * renda_mensal

print("================ Seus números de acordo com a regra 50/30/20 são: ================\n") 
print(
    'R${:,.2f}'.format(essencial)
      )
print(
    'R${:,.2f}'.format(lazer)
    )
print(
    'R${:,.2f}'.format(economia)
    )

print("\n==============================================================================\n")