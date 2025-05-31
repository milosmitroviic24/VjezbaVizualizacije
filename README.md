# Titanic Dataset Analiza (Univarijantna, Bivarijantna i Multivarijantna)

Ovaj Python skript vrši osnovnu eksploratornu analizu (EDA) nad **Titanic** skupom podataka koristeći biblioteke `pandas`, `matplotlib` i `seaborn`. Analiza uključuje univarijantne, bivarijantne i multivarijantne vizualizacije, koje pomažu u boljem razumevanju strukture podataka i odnosa između atributa.

---

## 📊 Sadržaj analize

### 1. Univarijantna analiza
- Histogram raspodele godina (`Age`)
- Bar grafici za:
  - Klase (`Pclass`)
  - Pol (`Sex`)
  - Luka ukrcavanja (`Embarked`)

### 2. Bivarijantna analiza
- Boxplot: raspodela godina po statusu preživljavanja (`Survived`)
- Countplot: preživljavanje po polu (`Sex`)
- Barplot: prosečna cena karte (`Fare`) po klasi (`Pclass`)

### 3. Multivarijantna analiza
- Heatmap korelacije numeričkih kolona
- Scatterplot: `Age` naspram `Fare`, obojen po vrednosti `Survived`

---

## 🛠️ Potrebne biblioteke

Pre pokretanja, uveri se da imaš instalirane sledeće biblioteke:

```bash
pip install pandas matplotlib seaborn
