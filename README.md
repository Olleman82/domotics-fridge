# Domotics Fridge

Ett Python-projekt för att styra en Vevor kylbox via Bluetooth med en Raspberry Pi.

## Installation

### Systemberoenden
```bash
sudo apt-get update
sudo apt-get install -y python3-dev python3-pip libdbus-1-dev
```

### Python-installation
1. Skapa en virtuell miljö:
```bash
python3 -m venv venv
source venv/bin/activate  # På Linux/Mac
# eller
.\venv\Scripts\activate  # På Windows
```

2. Installera Python-paket:
```bash
pip install -r requirements.txt
```

## Användning
1. Aktivera den virtuella miljön om den inte redan är aktiverad
2. Kör programmet:
```bash
python test_fridge.py
```

## Funktioner
- Bluetooth-anslutning till Vevor kylbox
- Temperaturkontroll
- Strömhantering

## Bidrag
Känner du att du vill bidra? Skapa en pull request!