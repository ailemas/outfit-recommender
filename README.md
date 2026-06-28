# outfit-recommender

Download the small version of the dataset: https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small

### Add a folder called data that contains the styles.csv and images from dataset in backend folder:
```
Structure:
backend/
    data/
        styles.csv
        images/
```

### One time setup:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run once per session:
```bash
source venv/bin/activate
```

### Step 1 — clean the dataset (run once, or if dataset changes):
```bash
python3 preprocess.py
```

### Step 2 — train the model (run once, or if preprocess changes):
```bash
python3 train.py
```

### Step 3 — start the server (run every time you work on the app):
```bash
python3 app.py
```

