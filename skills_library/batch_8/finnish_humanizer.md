---
title: finnish-humanizer
url: https://skills.sh/github/awesome-copilot/finnish-humanizer
---

# finnish-humanizer

skills/github/awesome-copilot/finnish-humanizer
finnish-humanizer
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill finnish-humanizer
Summary

Detect and remove AI-generated patterns from Finnish text to match native speaker voice.

Identifies 26 patterns across Finnish-specific structures (passive overuse, missing particles, translation calques, genitive chains) and universal markers (hedging, filler phrases, artificial enthusiasm)
Preserves meaning, register, and technical content while replacing AI patterns with natural Finnish constructions
Includes adaptive workflow: analyzes short texts directly, flags patterns in longer documents for review before rewriting
Emphasizes Finnish voice principles: directness, brevity, particle use, and strategic understatement over AI's tendency toward formality and padding
SKILL.md
Finnish Humanizer

<finnish_voice> Ennen kuin korjaat yhtään patternia, sisäistä miten suomalainen kirjoittaja ajattelee.

Suoruus. Suomalainen sanoo asian ja siirtyy eteenpäin. Ei johdattelua, ei pehmentämistä, ei turhia kehyksiä. "Tämä ei toimi" on täysi lause.

Lyhyys on voimaa. Lyhyt virke ei ole laiska — se on täsmällinen. Pitkä virke on perusteltava.

Toisto on sallittu. Suomessa saman sanan käyttö kahdesti on normaalia. Englannin synonyymikierto ("utilize" → "employ" → "leverage") kuulostaa suomessa teennäiseltä.

Innostus epäilyttää. Suomalainen kirjoittaja ei huuda eikä hehkuta. Kuiva toteamus on vahvempi kuin huutomerkki. "Ihan hyvä" on kehu.

Hiljaisuus on tyylikeino. Se mitä jätetään sanomatta voi olla yhtä tärkeää kuin se mitä sanotaan. Älä täytä jokaista aukkoa selityksellä.

Partikkelit elävöittävät. -han/-hän, -pa/-pä, kyllä, vaan, nyt, sit — nämä tekevät tekstistä elävää ja luonnollista. AI jättää ne pois koska ne ovat "turhia". Ne eivät ole.

Esimerkki: sieluton vs. elävä

Sieluton:

Tämä on erittäin merkittävä kehitysaskel, joka tulee vaikuttamaan laajasti alan tulevaisuuteen. On syytä huomata, että kyseinen innovaatio tarjoaa lukuisia mahdollisuuksia eri sidosryhmille.

Elävä:

Iso juttu alalle. Tästä hyötyvät monet.

Persoonallisuuden lisääminen

AI-tunnusmerkkien poistaminen ei yksin riitä — teksti tarvitsee myös persoonallisuutta.

Rytmin vaihtelu. Vaihtele lyhyitä ja pitkiä virkkeitä. Monotoninen virkerakenne on AI:n tunnusmerkki.
Monimutkaisuuden tunnustaminen. Asiat voivat olla ristiriitaisia, epäselviä tai keskeneräisiä. AI yrittää ratkaista kaiken siististi.
Konkreettiset yksityiskohdat. Korvaa yleistykset yksityiskohdilla. "Monet yritykset" → "Kolme suurinta kilpailijaa".
Harkittu epätäydellisyys. Sivujuonteet, ajatuksen kehittyminen kesken tekstin, itsekorjaus — nämä ovat ihmisen kirjoittamisen merkkejä. </finnish_voice>
Tunnista — Lue teksti ja merkitse AI-patternit
Uudelleenkirjoita — Korvaa patternit luonnollisilla rakenteilla
Säilytä merkitys — Älä muuta asiasisältöä
Säilytä rekisteri — Jos alkuperäinen on virallista, pidä virallisena
Lisää persoonallisuutta — Tuo kirjoittajan ääni esiin
Adaptiivinen workflow

Lyhyt teksti (alle 500 sanaa): Käsittele suoraan. Palauta luonnollistettu teksti + muutosyhteenveto.

Pitkä teksti (yli 500 sanaa):

Analysoi ensin — listaa löydetyt AI-patternit ja niiden esiintymät
Esitä löydökset käyttäjälle
Kysy epäselvistä tapauksista (onko piirre AI-pattern vai tietoinen valinta?)
Toteuta luonnollistaminen

26 AI-patternia on jaettu kahteen ryhmään: suomenkieliset (suomelle ominaiset rakenteet) ja universaalit (kaikissa kielissä esiintyvät, tunnistetaan ja korjataan suomeksi). Alla 7 kanonista esimerkkiä. Täysi 26 kategorian patternilista: ks. references/patterns.md

Suomenkieliset patternit

#1 Passiivin ylikäyttö AI käyttää passiivia kaikkialla välttääkseen tekijän nimeämistä.

Ennen: Sovellus on suunniteltu tarjoamaan käyttäjille mahdollisuus hallita omia tietojaan tehokkaasti. Jälkeen: Sovelluksella hallitset omat tietosi.

#4 Puuttuvat partikkelit AI ei käytä partikkeleita (-han/-hän, -pa/-pä, kyllä, vaan) koska ne ovat epämuodollisia. Suomessa ne ovat normaalia kirjoituskieltä.

Ennen: Tämä on totta. Kyse on kuitenkin siitä, että tilanne on monimutkainen. Jälkeen: Onhan se totta. Tilanne on vaan monimutkainen.

#5 Käännösrakenteet AI tuottaa suomea joka noudattaa englannin sanajärjestystä ja rakenteita.

Ennen: Tämän lisäksi, on tärkeää huomioida se tosiasia, että markkinat ovat muuttuneet. Jälkeen: Markkinatkin ovat muuttuneet.

#6 Genetiiviketjut Peräkkäiset genetiivimuodot kasautuvat kun AI yrittää ilmaista monimutkaisia suhteita yhdessä rakenteella.

Ennen: Tuotteen laadun parantamisen mahdollisuuksien arvioinnin tulokset osoittavat kehityspotentiaalia. Jälkeen: Arvioimme miten tuotteen laatua voisi parantaa. Kehityspotentiaalia löytyi.

Universaalit patternit suomeksi

#13 Merkittävyyden liioittelu AI paisuttaa kaiken "merkittäväksi", "keskeiseksi" tai "ratkaisevaksi".

Ennen: Tekoäly tulee olemaan merkittävässä ja keskeisessä roolissa tulevaisuuden ratkaisevien haasteiden ratkaisemisessa. Jälkeen: Tekoälystä tulee tärkeä työkalu moniin ongelmiin.

#15 Mielistelevä sävy AI kehuu kysyjää tai aihevalintaa. Suomessa tämä on erityisen kiusallista.

Ennen: Hyvä kysymys! Tämä on ehdottomasti yksi tärkeimmistä aiheista tällä hetkellä. Jälkeen: Aihe on ajankohtainen.

#17 Täytesanat ja -lauseet AI aloittaa tai täyttää kappaleita fraaseilla jotka eivät lisää sisältöä.

Ennen: On syytä huomata, että tässä yhteydessä on tärkeää ymmärtää alustan arkkitehtuuri ennen käyttöönottoa. Jälkeen: Ymmärrä alustan arkkitehtuuri ennen käyttöönottoa.

<output_format>

Tulostusformaatti

Kun olet luonnollistanut tekstin, palauta:

Uudelleenkirjoitettu teksti — kokonaisuudessaan
Muutosyhteenveto (valinnainen, oletuksena mukana) — lyhyt lista korjatuista patterneista

Jos käyttäjä pyytää vain tekstiä ilman selityksiä, jätä muutosyhteenveto pois. </output_format>

Älä muuta asiasisältöä. Jos alkuperäisessä on fakta, se säilyy.
Älä yksinkertaista. Luonnollistaminen ei tarkoita lapsenkielistä versiota.
Kunnioita rekisteriä. Virallinen teksti pysyy virallisena — vain AI-patternit poistetaan.
Älä lisää omaa sisältöä. Et keksi uusia väitteitä tai esimerkkejä.
Kysy epäselvissä tapauksissa. Jos et ole varma onko jokin piirre AI-pattern vai kirjoittajan tietoinen valinta, kysy käyttäjältä.
Jo luonnollinen teksti. Jos teksti on jo luonnollista, ilmoita se äläkä tee turhia muutoksia.
Koodiesimerkkit ja tekninen sanasto. Säilytä englanninkieliset koodiesimerkkit, tekniset termit ja lainaukset sellaisinaan.
Sekateksti (fi/en). Käsittele vain suomenkieliset osat. Jätä englanninkieliset osiot koskematta.
References
Full 26-pattern list with examples: references/patterns.md
Source repository: Hakku/finnish-humanizer (MIT)
Weekly Installs
8.6K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass