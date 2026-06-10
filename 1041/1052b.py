mes = int(input())

nome_mes = ""

match mes:
    case 1:
        nome_mes = "January"
    case 2:
        nome_mes = "February"
    case 3:
        nome_mes = "March"
    case 4:
        nome_mes = "April"
    case 5:
        nome_mes = "May"
    case 6:
        nome_mes = "June"
    case 7:
        nome_mes = "July"
    case 8:
        nome_mes = "August"
    case 9:
        nome_mes = "September"
    case 10:
        nome_mes = "October"
    case 11:
        nome_mes = "November"
    case 12:
        nome_mes = "December"
    case _:
        nome_mes = "Mês inválido"

print(nome_mes)
