class SzyfrException(Exception):
    pass


def zrob_slownik(text):
    text_raw = ''.join(text.split('-'))
    if len(text_raw) != len(list(set(text_raw))):
        raise SzyfrException('Szyfr nie jest jednoznaczny!')
    text_low = text.lower().split('-')
    slownik = dict()
    for i in range(ord('a'), ord('z') + 1):
        slownik[chr(i)] = chr(i)
        slownik[chr(i - (abs(ord('A') - ord('a'))))] = chr(i - (abs(ord('A') - ord('a'))))
    for sylabs in text_low:
        if len(sylabs) > 2:
            raise SzyfrException('Szyfr nie jest jednoznaczny!')
        slownik[sylabs[0]] = sylabs[1:]
        slownik[sylabs[1:]] = sylabs[0]

        slownik[chr(ord(sylabs[0]) - 32)] = chr(ord(sylabs[1:]) - 32)
        slownik[chr(ord(sylabs[1:]) - 32)] = chr(ord(sylabs[0]) - 32)
    return slownik


def szyfruj(szyfr, text):
    slownik = zrob_slownik(szyfr)
    text = list(map(lambda x: slownik[x] if x in slownik.keys() else x, text))
    text = ''.join(text)
    return text


if __name__ == '__main__':
    szyfry = ('GA-DE-RY-PO-LU-KI', 'PO-LI-TY-KA-RE-NU')
    while True:
        szyfr = input(f'Z którego szyfru chcesz skorzystać? \n'
                      f'{szyfry[0]} - 0 \n'
                      f'{szyfry[1]} - 1 \n'
                      f'własny szyfr - 2 \n')
        szyfr = int(szyfr)

        if szyfr in (0,1):
            text = input('Podaj tekst do zaszyfrowania: ')
            szyfr = szyfry[szyfr]
            zaszyfrowane = szyfruj(szyfr, text)
            print(zaszyfrowane)
        else:
            szyfr = input(f'Podaj swój własny szyfr w takim formacie {szyfry[0]}: ')
            try:
                text = input('Podaj tekst do zaszyfrowania: ')
                zaszyfrowane = szyfruj(szyfr, text)
                print(zaszyfrowane)
            except SzyfrException as e:
                print(e, 'Moze sprobujemy jeszcze raz?')

        co_teraz = input('Co teraz? \n'
                         'Jeszcze raz - 1 \n'
                         'Wychodze - 2 \n')
        co_teraz = int(co_teraz)
        if co_teraz == 2:
            break
