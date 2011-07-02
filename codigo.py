def caixa_eletronico(dinheiro):
    notas_disponiveis = [20, 10, 5]
    if dinheiro in notas_disponiveis:
        notas = [dinheiro,]
    else:
        if dinheiro == 15:
            notas = [ 5, 10 ]
        else:
            notas = [ 5, 20 ]
        
    saque = []

    for nota in notas:
       saque.append("1 nota %s reais" % nota)
    return ", ".join(saque) 
    
