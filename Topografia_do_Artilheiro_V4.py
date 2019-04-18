from math import degrees
from math import atan

print('Olá Artilheiro!')
print('')
print('Este programa aceita somente coordenadas planas no sistema UTM')
print('')
print('Utilize pontos no lugar de vírgulas')
print('')
inicio = input('Tecle ENTER para prosseguir: \n')
def quadrado(j, k):
    return j ** k
# conversão de minutos e segundos para graus:
def conv_m_p_g(m):
    return m/60
def conv_s_p_g(s):
    return s/3600
#conversor de graus em milésimos:
def g_p_m(g):
    return (g * 160) / 9
#tangente do rumo AB
def tang(e, n):
    return e/n

x = 1
while x == 1:
    Ea = float(input('Digite o E da coordenada da Estação:'))
    print('')
    Na = float(input('Digite o N da coordenada da Estação:'))
    print('')
    Eb = float(input('Digite o E da coordenda do Ponto Visado:'))
    print('')
    Nb = float(input('Digite o N da coordenda do Ponto Visado:'))
    dE = Eb - Ea
    dN = Nb - Na
    a = quadrado(dE, 2) + quadrado(dN, 2)
    dist = quadrado(a,(1/2))
    print('A distância na carta é de: {} metros'.format('%.2f' % dist))
    print('')
    ano_carta = int(input('Digite o ano da confecção da carta topográfica:'))
    print('')
    ano_atual = int(input('Digite o ano corrente:'))
    print('')
    print('Digite abaixo a variação da Declinação magnética da carta ao ano em Graus, minutos e segundos:')
    dmg = float(input('Graus:'))
    dmm = float(input('Minutos:'))
    dms = float(input('Segundos:'))
    print('')
    print('Digite abaixo a Declinação Magnética da carta:')
    dmag = abs(float(input('Graus:')))
    dmam = abs(float(input('Minutos:')))
    dmas = abs(float(input('Segundos:')))
    print('')
    print('Digite abaixo a convergência de meridianos da carta:')
    yg = abs(float(input('Graus:')))
    ym = abs(float(input('Minutos:')))
    ys = abs(float(input('Segundos:')))
    print('')
    perg01 = input('O Norte de Quadrícula e o Norte Magnético estão em lados opostos à direção do NV? (s/n):').upper()
    print('')
    perg02 = input('O Norte Magnético está à leste do Norte de Quadrícula? (s/n): ').upper()

    # Variação da declicanação magnética por ano
    dt_ano = ano_atual - ano_carta

    # graus total da declinação magnética anual:
    dmi = dmg + conv_m_p_g(dmm) + conv_s_p_g(dms)

    # graus total da declinação magnética no ano de confecção da carta
    dma = dmag + conv_m_p_g(dmam) + conv_s_p_g(dmas)

    # dm0 é a variação da declinação anual desde a confecção da carta
    dm0 = dmi * dt_ano

    # soma da declinação magnética da carta com a declinação anual
    dm = dm0 + dma

    # convergência de meridianos = Y
    y = yg + conv_m_p_g(ym) + conv_s_p_g(ys)

    # Declinação magnética(Dm) é o ângulo formado entre o Norte Verdadeiro e o Norte Magnético
    # QM é oeste quando o NM está a oeste do NQ e leste quando o NM está a leste do NQ
    # Quando NQ e NM  estão em lados opostos do NV QM = Dm + Y
    # Quando NQ e NM estão do mesmo lado do NV QM = Dm - Y

    # cálculo do ângulo QM
    def calcular_qm(decl_mag, conv_mer):
        if perg01 == 'S' == 'SIM':
            qm = decl_mag - conv_mer
        else:
            qm = decl_mag + conv_mer
        return qm

    # cálculo do lançamento
    def calcular_az(lancamento, anguloqm):
        if perg02 == 'S' == 'SIM':
            azimute = lc - anguloqm
        else:
            azimute = lancamento + anguloqm
        return azimute

    print('QM = {}º'.format('%.2f' % calcular_qm(dm, y)))

    if dN == 0:
        a_grau = 360
        print('O Lançamento em graus é de 360º')
        print('O Lançamento em milésimos é de 6400 milésimos')

    if dE >= 0 and dN >= 0:
        print('1º Quadrante')
        print('A tangente do rumo AB é {}'.format(tang(dE, dN)))
        a_grau = degrees(atan(tang(dE, dN)))
        print('O Lançamento de AB é em graus {}º'.format('%.f' % a_grau))
        print('O lançamento de AB em milésimos é {} milésimos'.format('%.f' % g_p_m(a_grau)))
        print('0 Azimute é {}º'.format(calcular_az(a_grau, calcular_qm(dm, y))))

    if dE > 0 and dN < 0:
        print('2º Quadrante')
        print('A tangente do rumo AB é {}'.format(tang(dE, dN)))
        a_grau = degrees(atan(tang(dE, dN))) + 180
        print('O Lançamento de AB é em graus {}º'.format('%.f' % a_grau))
        print('O lançamento de AB em milésimos é {} milésimos'.format('%.f' % g_p_m(a_grau)))
        print('0 Azimute é {}º'.format(calcular_az(a_grau, calcular_qm(dm, y))))

    if dE < 0 and dN < 0:
        print('3º Quadrante')
        print('A tangente do rumo AB é {}'.format(tang(dE, dN)))
        a_grau = degrees(atan(tang(dE, dN))) + 180
        print('O Lançamento de AB é em graus {}º'.format('%.f' % a_grau))
        print('O lançamento de AB em milésimos é {} milésimos'.format('%.f' % g_p_m(a_grau)))
        print('0 Azimute é {}º'.format(calcular_az(a_grau, calcular_qm(dm, y))))

    if dE < 0 and dN > 0:
        print('4º Quadrante')
        print('A tangente do rumo AB é {}'.format(tang(dE, dN)))
        a_grau = degrees(atan(tang(dE, dN))) + 360
        print('O Lançamento de AB é em graus {}º'.format('%.f' % a_grau))
        print('O lançamento de AB em milésimos é {} milésimos'.format('%.f' % g_p_m(a_grau)))
        print('0 Azimute é {}º'.format(calcular_az(a_grau, calcular_qm(dm, y))))

    print('')
    print('Aço, Boina Preta, Brasil!')
    print('')
    x = int(input('Deseja calcular novamente? \n Tecle: \n 1 para Sim \n 2 para Não \n'))

    print('')