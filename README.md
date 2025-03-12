Lähdin selvittämään, kuinka paljon dataa teiltä on saatavilla rajapintojen kautta. Esimerkiksi yrityshakemistoista voi hakea yrityksiä kunnittain, ja rajapinta palauttaa myös niiden verkkosivut, mikäli ne on lisätty järjestelmään.

Tämä skripti käy läpi kaikki (yritys).yrityshakemistot.fi/Api/Companies, ja se palauttaa JSON-responsen, jossa on runsaasti teidän tuottamaa tietoa sekä yrityksen verkkosivut.

Yksi idea olisi myös parantaa hakukonetta siten, että jos tietoja, kuten verkkosivuja, ei löydy, järjestelmä voisi vinkata listatuille yrityksille puuttuvasta tiedosta. Lisäksi voitaisiin tarjota heille tekoälyn luoma lyhyt tiivistelmä yrityksestä ja muita hyödyllisiä tietoja.


Huomaa tulokset.json teidostossa on "Ei toimi - ei JSON-vastausta" johtuu siitä että joko rajapintarakenne on erilainen tai osoite oli vain tyhjä joissakin sivuissa ja niitä oli muutama mitä löysin ( pystytään silti soveltamaan ).

