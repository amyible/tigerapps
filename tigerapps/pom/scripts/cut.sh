#!/bin/bash

python cut.py buildings_hover.png building_metadata.csv h out/
python cut.py buildings_event_hover.png building_metadata.csv eh out/
python cut.py buildings_event.png building_metadata.csv e out/
python cut.py buildings_default.png building_metadata.csv '' out/
