# Web-Scraping & News Classification

## Scrape Links & Articles with Scrapy 
Running the scrapper will generate 2 files per desires category, one containing the links and the other with the articles.


```
cd scraper

scrapy crawl links

scrapy crawl articles
```

## News Classification

Execute the notebooks in the following order:
1. 01 - Vectorize: generate joblib files with word vectores, targets and features.
2. 02 - Evaluate - CV: runs a 5 fold cross validation with a Gradient boosting classifier, outputs the moist important token for each fold, AUC per class. At the end outputs average accuracy and confussion matrix.
3. 03 - Evaluate-Corte Agosto: separates the dataset in train/test, training with examoles up to 31/07/2021 and test with data from 01/08/2021.

## Results

Findings of this work can be found in the Results.pdf file.

### Authors
1. OTRINO, FACUNDO DAMIÁN 
2. ROJAS, MARIANO ARTURO 
3. VAILLARD, LEANDRO CARLOS