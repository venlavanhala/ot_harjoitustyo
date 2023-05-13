
## Testausdokumentti

Ohjelmaa testataan unittest-testien avulla. Testit keskittyvät note- ja user-repository-luokkiin.

### Testaus

- Repositorio-luokkia testataan tyhjentämällä ensin tietokantatiedosto, ja testaamalla sitten toimintoja.
- Luokat TestNoteTools ja TestUserTools testaavat repositorio-luokkia.
- Sovelluslogiikan testaamiseen on luotu omat repositorioluokat: FakeNoteRepository ja FakeUserRepository

### Testauskattavuus

<img src="covergae.png"
	alt="Coverage" />

