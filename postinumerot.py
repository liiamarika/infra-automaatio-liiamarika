import http_pyynto


def ryhmittele_toimipaikoittain(numero_sanakirja: dict) -> dict:
    '''
    Palauttaa annetusta postinumerosanakirjasta uuden version, jossa avaimina toimivat toimipaikkojen nimet.
    Arvoiksi koostetaan lista niistä postinumeroista, jotka kuuluvat kyseiseen toimipaikkaan.
    
    Sanakirjan avaimissa toimipaikkojen nimet "normalisoidaan", eli niistä poistetaan välilyönnit ja väliviivat
    ja kaikki kirjaimet muutetaan isoiksi. Tämä poistaa aineistossa olevia eroja saman nimen kirjoitusasuissa.
    '''
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        nimi = normalisoi_nimi(nimi)
        if nimi not in paikat:
            paikat[nimi] = []

        paikat[nimi].append(numero)

    return paikat


def normalisoi_nimi(nimi: str) -> str:
    '''
    Yhdenmukaistaa eri toimipaikkojen nimien kirjoitusasua muuttamalla annetun nimen
    isoiksi kirjaimiksi ja poistamalla välilyönnit ja -viivat.
    '''
    return nimi.upper().strip().replace(' ', '').replace('-', '')


def etsi_postinumerot(nimi: str, toimipaikat_dict: dict):
    '''
    Etsii annetusta sanakirjasta kaikki annettua nimeä vastaavat postinumerot.
    '''
    normalisoitu = normalisoi_nimi(nimi)
    return toimipaikat_dict.get(normalisoitu, [])


def main():
    '''
    Pääohjelma, joka kysyy käyttäjältä toimipaikan nimeä ja etsii verkosta löytyvästä JSON-aineistosta
    kaikki siihen kuuluvat postinumerot.
    '''
    postinumerot = http_pyynto.hae_postinumerot()

    toimipaikat = ryhmittele_toimipaikoittain(postinumerot)

    toimipaikka = input('Kirjoita postitoimipaikka: ')

    loydetyt = etsi_postinumerot(toimipaikka, toimipaikat)

    if loydetyt:
        loydetyt = sorted(loydetyt)
        print('Postinumerot: ' + ', '.join(loydetyt))
    else:
        print('Toimipaikkaa ei löytynyt')


if __name__ == '__main__':
    main()