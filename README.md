# SlovakEuroPronouncer
Z číselnej ceny v eurách získa číslovku ako slovo.

Prevedie číslo na slovnú číslovku spojenú s vyskloňovaným eurom.

Pre funkciu `pronounce` je vstupom maximálne šesťciferné celé číslo.

Pre funkciu `pronounce_with_cents` je vstupom číslo Decimal, kde počet cifier naľavo od desatinnej bodky
je maximálne 6 a počet cifier naľavo od desatinnej bodky je maximálne 2.

Tento nástroj je vhodný napríklad pre tvorbu zmlúv.

## Inštalácia
```
pip install git+git://github.com/simeonborko/SlovakEuroPronouncer.git
```

## Použitie
```
from SlovakEuroPronouncer import pronounce, pronounce_with_cents
from decimal import Decimal
pronounce(105)  # stopäť eur
pronounce_with_cents(Decimal('10.20'))  # desať eur a 20 centov
```
