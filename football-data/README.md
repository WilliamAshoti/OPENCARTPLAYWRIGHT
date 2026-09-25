# StatsBomb, IMPECT en Wyscout: onderzoek naar feeds en open data

Onderzoek (september 2026) naar de vraag of StatsBomb-, IMPECT- en Wyscout-data
te scrapen is via websites die deze providers gebruiken, zoals dat bij Stats
Perform/Opta via Scoresway-widgets kan. Daarnaast een werkend script dat alle
data downloadt die deze drie providers zelf gratis vrijgeven.

## Conclusie in het kort

1. **Er bestaan geen publieke Scoresway-achtige feeds voor StatsBomb, Wyscout of
   IMPECT.** Scoresway werkt omdat Opta widgets levert aan duizenden media- en
   clubsites: de widget haalt de data in de browser op, met een sleutel die in
   de pagina zelf staat. StatsBomb, Wyscout en IMPECT verkopen zo'n
   widgetproduct niet. Hun data gaat via afgeschermde API's (inlog per klant)
   en ingelogde platforms naar clubs, bookmakers en media.
2. **Wie deze data op X laat zien, betaalt er (via iemand) voor.** Mohammad Adnan
   ([@adnaaan433](https://x.com/adnaaan433)) schrijft zelf dat hij StatsBomb
   premium data gebruikt (circa **$10.000 per jaar**) via de toegang van een
   klant, en dat hij die data niet mag delen
   ([bron](https://x.com/adnaaan433/status/2052779778479153462)). Zijn publieke
   app insight90 draait op WhoScored-data (Opta).
3. **Afgeschermde data scrapen is juridisch riskant** (zie
   [Juridisch](#juridisch-nleu)). Hudl, eigenaar van StatsBomb en Wyscout,
   verbiedt in zijn voorwaarden uitdrukkelijk bots, scrapers en crawlers.
4. **Wat wel kan:** alle drie de providers geven zelf gratis data vrij. Samen is
   dat ruim 6.000 wedstrijden met volledige event data. Het script
   [`download_open_data.py`](download_open_data.py) haalt alles op.

## Wie gebruikt welke provider, en is er een feed?

| Site / persoon | Provider | Publiek zichtbaar? | Scrapebare feed? |
|---|---|---|---|
| Mohammad Adnan (@adnaaan433) | StatsBomb premium via een klant (~$10k/jr) | Alleen de visualisaties | Nee. Zijn publieke app gebruikt WhoScored (Opta) |
| [FBref](https://fbref.com) | StatsBomb van 2018 tot oktober 2022, daarna Opta | Nee meer | Nee. Alle StatsBomb-data is in 2022 verwijderd ([bron](https://www.sports-reference.com/blog/2022/10/fbref-leagues-%F0%9F%87%B5%F0%9F%87%B9-leagues-%F0%9F%87%A7%F0%9F%87%B7-leagues-%F0%9F%87%B2%F0%9F%87%BD-expanded-womens-and-mens-data-new-data-partner/)). In januari 2026 stopte Opta ook de feed en eiste verwijdering ([bron](https://www.sports-reference.com/blog/2026/01/fbref-stathead-data-update/)) |
| [Fantasy Football Scout](https://www.fantasyfootballscout.co.uk/2024/09/07/a-guide-to-the-statsbomb-stats-in-our-premium-members-area) | StatsBomb, vijf extra tabbladen met spelerstatistieken | Alleen achter de betaalmuur (Premium Members) | Nee. Scrapen van het ledengedeelte schendt de voorwaarden |
| [StatsBomb Stats Portal](https://stats-portal.statsbomb.com/) | StatsBomb Live Data | Ja, openbaar | Alleen uitslagen en eindstatistieken voor gokmarkten (schoten, schoten op doel, assists, passes, tackles, overtredingen), pas na de controle na afloop. Geen events of coördinaten. Hudl-voorwaarden verbieden geautomatiseerde toegang |
| Bookmakers met bet builders (bijv. [Betfred](https://insights.betfred.com/education/how-does-a-bet-builder-work-statsbomb-stats-explained/)) | StatsBomb, gebruikt om weddenschappen af te rekenen | Alleen quoteringen | Nee |
| Wyscout-analisten op X (radars, scatterplots) | Wyscout met een individueel abonnement | Alleen de visualisaties | Nee. Ze exporteren zelf naar Excel via *Advanced Search → Export to Excel* ([uitleg](https://themastermindsite.com/2022/09/01/how-to-use-wyscout-for-successful-football-analysis/)) |
| [Twelve Football](https://twelve.football) | Wyscout, StatsBomb, IMPECT, Stats Perform, SkillCorner | Deels, in een betaalde app | Nee |
| IMPECT ([@impect_official](https://x.com/impect_official)) | Eigen data. Clubs en bonden (150+ clubs); sinds oktober 2025 van [Catapult](https://www.sportspro.com/news/catapult-impect-soccer-scouting-technology-acquisition-october-2025/) | Alleen rankings in social posts | Nee. Geen publieke datasite, geen widgets |

Het StatsBomb Stats Portal, Fantasy Football Scout en Betfred heb ik niet zelf
kunnen openen vanuit de onderzoeksomgeving. De beschrijving hierboven komt uit de zoekresultaten
en de gelinkte pagina's.

### Waarom er geen "Scoresway voor StatsBomb" is

- **StatsBomb (Hudl):** de API (`data.statsbomb.com`, bijvoorbeeld via
  `statsbombpy`) werkt alleen met een gebruikersnaam en wachtwoord per klant.
  Hudl zegt: *"API access is for paying customers only"*
  ([Hudl support](https://support.hudl.com/s/article/use-statsbomb-api?language=en_US)).
- **Wyscout (Hudl):** de API (`apirest.wyscout.com`) gebruikt Basic Auth per
  klant ([docs](https://apidocs.wyscout.com/),
  [auth](https://support.wyscout.com/authentication)). Het platform is
  alleen toegankelijk na inloggen.
- **IMPECT:** de API is alleen beschikbaar met een klantaccount. De tools
  `impectPy` en `impectR` vragen om inloggegevens.

Deze providers leveren aan partijen met een contract (clubs, bookmakers,
Fantasy Football Scout). Die partijen tonen alleen afgeleide cijfers, meestal
achter een login. Een open feed zoals de Opta-widgets bestaat daardoor niet.

## Juridisch (NL/EU)

- **Databankenwet** (de Nederlandse uitwerking van EU-richtlijn 96/9/EG): een
  databank waarin substantieel is geïnvesteerd, is beschermd. Het opvragen of
  hergebruiken van een substantieel deel ervan is verboden. Event data met
  ruim 3.400 handmatig verzamelde events per wedstrijd valt daar vrijwel
  zeker onder.
- **Football Dataco v Sportradar** (HvJ EU C-173/11, 2012; Court of Appeal 2013):
  het overnemen en aanbieden van live voetbaldata uit andermans databank is
  inbreuk. Sportradar en bookmaker Stan James werden mede aansprakelijk
  gehouden voor de inbreuk door gebruikers
  ([SCL](https://www.scl.org/2595-database-right-ecj-judgment-in-football-data-co-v-sportradar/)).
- **Ryanair v PR Aviation** (HvJ EU C-30/14, 2015): ook als een databank niet
  beschermd is, mogen gebruiksvoorwaarden scrapen contractueel verbieden.
- **Hudl-voorwaarden:** geautomatiseerde toegang met bots, scrapers, crawlers
  of AI-tools is verboden ([hudl.com/terms](https://www.hudl.com/terms)).
- **Inloggegevens van een ander gebruiken** (van een klant, of sleutels uit een
  app gehaald) kan onder computervredebreuk vallen (art. 138ab Sr). Dat gaat
  verder dan een contractbreuk.
- **In de praktijk handhaven de providers actief:** Opta sloot in januari 2026
  de feed van FBref af, ook al was FBref een officiële licentienemer
  ([Awful Announcing](https://awfulannouncing.com/soccer/sports-reference-pulls-advanced-data-agreement-violation-dispute.html)).

## Wat wel kan: officiële open data

| Provider | Dekking | Licentie |
|---|---|---|
| **StatsBomb** ([hudl/open-data](https://github.com/hudl/open-data)) | 80 competitie-seizoenen, **3.961 wedstrijden**, waarvan 426 met 360-freeze-frames | Gratis voor niet-commercieel gebruik. Bron vermelden en StatsBomb-logo gebruiken |
| **IMPECT** ([ImpectAPI/open-data](https://github.com/ImpectAPI/open-data)) | **Bundesliga 2023/24 volledig: 306 wedstrijden**. Events, packing/bypassed opponents, event-KPI's, speler-KPI's per wedstrijd, opstellingen | Alleen niet-commercieel, **niet herverspreiden**, IMPECT vermelden (Duits recht, zie `LICENSE.pdf`) |
| **Wyscout** ([Pappalardo et al. 2019](https://figshare.com/collections/Soccer_match_event_dataset/4415000), [GitHub-kopie](https://github.com/koenvo/wyscout-soccer-match-event-dataset)) | **1.941 wedstrijden**: PL, La Liga, Serie A, Bundesliga, Ligue 1 2017/18, WK 2018, EK 2016 | **CC BY 4.0**: ook commercieel toegestaan, met bronvermelding |

**Hoogtepunten StatsBomb open data** (geteld op 25-09-2026):

- Volledige seizoenen: Premier League, La Liga, Serie A 2015/16 (380 wedstrijden
  per competitie), Ligue 1 2015/16 (377)
- Met 360-data: WK 2022 (64), EK 2020 en EK 2024 (51 per toernooi), WK vrouwen
  2023 (64), EK vrouwen 2022 en 2025 (31 per toernooi)
- Clubfocus met 360-data: Leverkusen 2023/24 (34, het ongeslagen seizoen), PSG
  Ligue 1 2021/22 en 2022/23 (26 en 32), Barcelona 2020/21 (35), Inter Miami
  MLS 2023 (6)
- Ook: Copa América 2024 (32), Afrika Cup 2023 (52), Indian Super League 2021/22
  (115), WK 2018 (64), Messi bij Barcelona 2004/05–2020/21, Arsenal
  2003/04 ("Invincibles"), CL-finales 1971–2019
- Vrouwen: WSL, NWSL, Frauen-Bundesliga, Liga F en Serie A Women, allemaal
  2023/24 of 2023, plus eerdere WSL-seizoenen

### Betaalde routes zonder te scrapen

- **Wyscout, individueel abonnement:** vanaf ongeveer €299 per jaar (Copper) of
  €399 (Mercury), volgens [360 Scouting](https://360scouting.com/wyscout-alternatives/);
  actuele prijzen staan op [Hudl pricing](https://www.hudl.com/en_gb/products/wyscout/pricing).
  Dit is de goedkoopste legale route naar actuele Wyscout-data, via de export
  naar Excel. Controleer in de voorwaarden van je plan of je visualisaties mag
  publiceren.
- **StatsBomb:** er is geen plan voor particulieren. Toegang voor onderzoek
  loopt via [Hudl Performance Insights](https://www.hudl.com/blog/hpi-2026-research-competition):
  geaccepteerde voorstellen krijgen vijf competitie-seizoenen event- en 360-data.
  De deadline voor 2026 was 3 juli 2026; let op de ronde van 2027.
- **IMPECT:** alleen voor clubs en bonden. Neem contact op via impect.com, of
  gebruik de open data.

## Het script gebruiken

Er is alleen Python 3.9+ nodig, geen extra packages. De data komt standaard in
`football-data/data/`. Die map staat in `.gitignore`, omdat de licenties
herverspreiding verbieden.

```sh
cd football-data

# Wat is er beschikbaar?
python download_open_data.py statsbomb list
python download_open_data.py impect list
python download_open_data.py wyscout list

# StatsBomb: Leverkusen 2023/24 inclusief 360-data
python download_open_data.py statsbomb get --competition 9 --season 281
# StatsBomb: alle seizoenen van één competitie (bijv. La Liga = 11)
python download_open_data.py statsbomb get --competition 11
# StatsBomb: alles (meer dan 10 GB; --no-360 scheelt ~3 GB)
python download_open_data.py statsbomb get --all --no-360

# IMPECT: volledige Bundesliga 2023/24 (~3 GB)
python download_open_data.py impect get

# Wyscout: één competitie, of alles
python download_open_data.py wyscout get --competition England
python download_open_data.py wyscout get
# Wyscout: de originele zips van figshare
python download_open_data.py wyscout get --raw
```

Gemeenschappelijke opties voor `get`:

- `--limit N`: maximaal N wedstrijden per seizoen (handig om te testen)
- `--out MAP`: andere doelmap
- `--workers N`: aantal parallelle downloads
- `--overwrite`: bestaande bestanden opnieuw downloaden

Bestanden die al bestaan, worden overgeslagen. Een afgebroken download kun je
dus gewoon opnieuw starten.

### Inladen met kloppy

[kloppy](https://kloppy.pysport.org) zet alle drie de formaten om naar één
model. Getest met kloppy 3.19:

```python
from kloppy import statsbomb, impect, wyscout

d = "data"
sb = statsbomb.load(
    event_data=f"{d}/statsbomb/events/3895292.json",
    lineup_data=f"{d}/statsbomb/lineups/3895292.json",
    three_sixty_data=f"{d}/statsbomb/three-sixty/3895292.json",
)
im = impect.load(
    event_data=f"{d}/impect/events/events_122838.json",
    lineup_data=f"{d}/impect/lineups/lineups_122838.json",
    squads_data=f"{d}/impect/squads/squads_743.json",
    players_data=f"{d}/impect/players/players_743.json",
)
wy = wyscout.load(event_data=f"{d}/wyscout/matches/England/2499719.json")

df = sb.to_df()  # pandas DataFrame, klaar voor mplsoccer
```

Voor pitch-plots, radars en pass networks werkt
[mplsoccer](https://github.com/andrewRowlinson/mplsoccer) direct met de
StatsBomb-data.

## Testnotities

- De opdrachten `list` en `get --limit 2` zijn getest voor StatsBomb, IMPECT en
  Wyscout (GitHub-kopie). Per provider is één wedstrijd met kloppy ingeladen:
  StatsBomb 3.953 events, IMPECT 3.057 events, Wyscout 1.809 events.
- `wyscout get --raw` (figshare) is **niet getest**, omdat figshare in de
  testomgeving geblokkeerd was. De URL's komen uit de README van de
  GitHub-kopie.

## Bronnen

- [hudl/open-data](https://github.com/hudl/open-data) ·
  [Hudl StatsBomb vrije data Women's Euro 2025](https://www.hudl.com/blog/hudl-statsbomb-free-euro-2025-data) ·
  [vijf vrouwencompetities](https://www.hudl.com/blog/statsbomb-free-womens-data-wsl-ligaf-bundesliga-seriea-nwsl)
- [ImpectAPI/open-data](https://github.com/ImpectAPI/open-data)
- [Pappalardo et al., *A public data set of spatio-temporal match events in soccer competitions*, Sci Data 2019](https://doi.org/10.1038/s41597-019-0247-7)
- [withqwerty/open-football](https://github.com/withqwerty/open-football): overzicht van open voetbaldata
- [FBref & Stathead Data Update (jan 2026)](https://www.sports-reference.com/blog/2026/01/fbref-stathead-data-update/)
- [Use the StatsBomb API, Hudl Support](https://support.hudl.com/s/article/use-statsbomb-api?language=en_US) ·
  [Hudl Terms](https://www.hudl.com/terms) ·
  [Wyscout API docs](https://apidocs.wyscout.com/)
- [Catapult neemt IMPECT over (SportsPro)](https://www.sportspro.com/news/catapult-impect-soccer-scouting-technology-acquisition-october-2025/)
