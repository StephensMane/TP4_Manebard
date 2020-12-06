chiffres_romains = [ "M", "CM", "D", "CD", "C", "XC","L", "VL", "XL", "X", "IX", "V", "IV", "I" ]

chiffres_arabes = [ 1000, 900, 500, 400, 100, 90, 50, 45, 40, 10, 9, 5, 4, 1 ]

# Test des conversion chiffres romains vers chiffres arabes

def test_conversion_r_cas_1():
  assert conversion_chiffres_romains('I') == 1

def test_conversion_r_cas_2():
  assert conversion_chiffres_romains('V') == 5

def test_conversion_r_cas_3():
  assert conversion_chiffres_romains('II') == 2

def test_conversion_r_cas_4():
  assert conversion_chiffres_romains('MM') == 2000

def test_conversion_r_cas_5():
  assert conversion_chiffres_romains('MMCCXXII') == 2222

def test_conversion_r_cas_6():
  assert conversion_chiffres_romains('IV') == 4



# Test des conversion chiffres arabes vers chiffres romains

def test_conversion_a_cas_1():
  assert conversion_chiffres_arabes(1) == 'I'

def test_conversion_a_cas_2():
  assert conversion_chiffres_arabes(5) == 'V'

def test_conversion_a_cas_3():
  assert conversion_chiffres_arabes(2) =='II'

def test_conversion_a_cas_4():
  assert conversion_chiffres_arabes(2000) == 'MM'

def test_conversion_a_cas_5():
  assert conversion_chiffres_arabes(2222) == 'MMCCXXII'

def test_conversion_a_cas_6():
  assert conversion_chiffres_arabes(4) == 'IV'


#Definition de test de la calculatrice

def test_calculatrice_cas_1():
  assert calculatrice('X','+','X') == 'XX'

def test_calculatrice_cas_2():
  assert calculatrice('I','-','I') == 0

def test_calculatrice_cas_3():
  assert calculatrice('IV','*','X') == 'XL'

def test_calculatrice_cas_4():
  assert calculatrice('M','/','IV') == 'CCL'

def test_calculatrice_cas_5():
  assert calculatrice('MM','+','MMM') == 5000

#Definition fonction runtest

def runtest():
  test_conversion_a_cas_1()
  test_conversion_a_cas_2()
  test_conversion_a_cas_3()
  test_conversion_a_cas_4()
  test_conversion_a_cas_5()
  test_conversion_a_cas_6()
  print("conversion arabe vers romain OK")
  test_conversion_r_cas_1()
  test_conversion_r_cas_2()
  test_conversion_r_cas_3()
  test_conversion_r_cas_4()
  test_conversion_r_cas_5()
  test_conversion_r_cas_6()
  print("conversion romain vers arabe OK")
  test_calculatrice_cas_1()
  test_calculatrice_cas_2()
  test_calculatrice_cas_3()
  test_calculatrice_cas_4()
  test_calculatrice_cas_5()
  print("calculatrice OK")

# Definition conversion chiffres arabes vers romain

def conversion_chiffres_arabes(val):
    remainder=val
    s=''
    if val<1 or val>3999: return "ERROR"
    for i in range(len(chiffres_arabes)):
      while remainder>=chiffres_arabes[i]:
          s+=chiffres_romains[i]
          remainder -= chiffres_arabes[i]
    return s


# Definition conversion chiffres romains vers arabes

def conversion_chiffres_romains(ch_r):

  j = 1
  indice_ch_r = 0
  indice_liste_ch_r = 0
  nombre_converti = 0

  while indice_ch_r < len(ch_r):

    if ch_r[indice_ch_r] == 'I':

      if indice_ch_r + 1 < len(ch_r) and ch_r[indice_ch_r+1] == 'X':

        indice_ch_r+=1
        nombre_converti += chiffres_arabes[10]*j

      elif indice_ch_r + 1 < len(ch_r) and ch_r[indice_ch_r+1] == 'V':

        indice_ch_r+=1
        nombre_converti += chiffres_arabes[12]*j

      else:
        while indice_ch_r+1 < len(ch_r) and ch_r[indice_ch_r] == ch_r[indice_ch_r+1]:

          j+=1
          indice_ch_r+=1

        while ch_r[indice_ch_r] != chiffres_romains[indice_liste_ch_r]:

          indice_liste_ch_r+=1

        nombre_converti += chiffres_arabes[indice_liste_ch_r]*j

    else :

      while indice_ch_r+1 < len(ch_r) and ch_r[indice_ch_r] == ch_r[indice_ch_r+1]:

        j+=1
        indice_ch_r+=1

      while ch_r[indice_ch_r] != chiffres_romains[indice_liste_ch_r]:

        indice_liste_ch_r+=1

      nombre_converti += chiffres_arabes[indice_liste_ch_r]*j

    j=1
    indice_ch_r+=1


  return nombre_converti

#Definition fonctio calculatrice

def calculatrice(nb1,operateur,nb2):

  nb1 = conversion_chiffres_romains(nb1)
  nb2 = conversion_chiffres_romains(nb2)
  resultat = 0

  if operateur == '+':

    resultat = nb1 + nb2

  if operateur == '-':

    resultat = nb1 - nb2

  if operateur == '*':

    resultat = nb1 * nb2

  if operateur == '/':

    resultat = nb1 / nb2


  if resultat == 0:
    return resultat

  elif resultat <= 4000:
    return conversion_chiffres_arabes(resultat)

  else:
    print("Le résultat est supérieur à 4000 et ne peut être affiché en chiffres romains")
    return resultat


runtest()
