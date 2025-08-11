# Tennis Tournament Draw Generator

A Python tool for generating tennis tournament draws from player lists, supporting seeded/unseeded players, custom field mapping, and data extraction utilities.

## 🚀 Features

- **Tournament Draw Generation**: Create single-elimination tournament brackets
- **Seeding Support**: Customizable number of seeded players (`n_seeded`)
- **Flexible Data Mapping**: JSON-to-class field mapping with computed values
- **Data Extraction Tools**: 
  - Parse official tournament PDFs
  - Scrape data from tennisabstract.com and wimbledon.com
  - Prototyping utilities for quick testing

## 📁 Repository Structure

```
tennis-draw/
├── player/         # Player model and utilities
├── match/          # Match and draw generation logic
├── sandbox/        # Example scripts and experiments
├── data/           # Raw, processed & scraped data + parsing scripts
├── _misc/          # Archived helper scripts
└── PoC/            # Proof-of-concept experiments
```

## 🏗️ Core Components

### Player Management (`player/`)
- Player model definition
- Data validation and utilities
- Custom field mapping from JSON sources

### Draw Generation (`match/`)
- Single-elimination bracket creation
- Seeding logic and placement
- Match pairing algorithms

### Data Processing (`data/`)
- PDF parsing for tournament entry lists
- Web scraping utilities
- Data transformation scripts

## 🧪 Development & Testing

- **`sandbox/`**: Quick prototyping and testing scripts
- **`PoC/`**: Proof-of-concept implementations
- **`_misc/`**: Legacy and helper utilities

## 🎾 Usage

The main functionality centers around generating tournament draws with proper seeding and player placement