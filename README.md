# From Promises to Accountability: Comparative AI Modeling and Visualization of Electoral Commitments in Nepali Political Texts

**Status:** Under review at *Natural Language Processing* (Cambridge University Press)

This repository contains the dataset, annotation materials, source code, and experiments for our study on **Election Commitment Mining** - a task that identifies and structures political commitments made by electoral candidates and parties in Nepali political texts. We benchmark machine learning, deep learning, and large language models to automatically classify statements as **Commitment (C)** or **Non-Commitment (NC)**.

## Repository Structure

```
.
├── annotators/       # Annotation guidelines and reviewer sheets
├── dataset/          # Train and test splits (.xlsx)
├── mcnemar-test/     # Source code for McNemar's mid-p statistical significance test
├── notebooks/        # ML, DL, and LLM experiment notebooks
├── predictions/      # Model prediction outputs (.npy) used for significance testing
├── requirements.txt  # Python dependencies
└── README.md
```

### `annotators/`
Contains the annotation guidelines used to define and label political commitments, along with the sheets from the three reviewers involved in the annotation and adjudication process.

### `dataset/`
Contains the gold-standard dataset split into **train** and **test** sets, provided in `.xlsx` format. Each instance is a sentence extracted from Nepali political texts, labeled as either Commitment (C) or Non-Commitment (NC).

Inside the `train-split/` subfolder, there are two versions of the train set:
- **`-aug`** - training data with augmentation (synthetic NC instances added to address class imbalance)
- **without `-aug`** - original training data, no augmentation applied

### `mcnemar-test/`
Contains the source code for running the **McNemar mid-p test**, used to statistically compare the performance of pairs of models (e.g., Model A vs. Model B) on the test set. The script consumes prediction files from `predictions/` and outputs the discordant pair counts and mid-p significance value for a given model pair.

### `notebooks/`
Contains experiment notebooks organized into three subfolders, covering both training/fine-tuning and evaluation of models on the Commitment vs. Non-Commitment classification task:
- `ml/` - Classical machine learning models
- `dl/` - Deep learning models
- `llm/` - Large language model experiments (zero-shot and few-shot)

### `predictions/`
Contains `.npy` files with model predictions on the held-out test set. Labels are encoded as:
- `0` - Commitment (C)
- `1` - Non-Commitment (NC)

These files are consumed by the script in `mcnemar-test/` to compute pairwise statistical significance between models.

## Setup

**Requirements:** Python 3.13.11 (as used in the reported experiments). No additional GPU/CUDA or OCR tool installation is required to reproduce the statistical testing pipeline in this repository.

```bash
pip install -r requirements.txt
```

## Reproducibility

This repository currently provides the **running mechanism** for training, evaluation, and statistical testing (code + prediction files) rather than the full set of reported scores/tables, as the paper is under peer review. The complete set of results will be added upon acceptance.

### Training and Evaluation (ML / DL / LLM)

Notebooks for training and evaluating each model family are organized under `notebooks/`:

```bash
notebooks/
├── ml/     # Classical machine learning models (LR, DT, RF, SVM, NB, KNN)
├── dl/     # Deep learning models (SRN, LSTM, GRU, CNN, mBERT, XLM-R)
└── llm/    # LLM zero-shot and few-shot experiments (Qwen3-8B, Llama-3.1-8B-Instruct, Gemma-4-E4B-it)
```

To reproduce training/evaluation for a given model family, open the relevant notebook in `notebooks/<ml|dl|llm>/` and run it against the train/test splits in `dataset/`. Each notebook follows the same general workflow: load the train/test split → preprocess/vectorize (or tokenize) → train (or prompt, for LLMs) → evaluate on the held-out test set → save predictions as `.npy` to `predictions/`.

Each notebook reads its train/test split from `dataset/` and writes its resulting predictions to `predictions/<model_name>.npy`, which can then be used directly by the McNemar test in the next step.



### Statistical Significance Testing (McNemar's mid-p test)

To run the McNemar mid-p test between two models using their saved predictions:

```bash
cd mcnemar-test
python mcnemar-test.py 
```


## License

- **Code** (scripts, notebooks): [MIT License](https://opensource.org/licenses/MIT)
- **Dataset and annotation materials** (`dataset/`, `annotators/`): [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) - sharing and adaptation permitted with attribution, for **non-commercial use only**, under the same license.

## Authors

Prakash Poudyal, Nischal Karki, Amrit Dahal, Rajani Chulyadyo, Sameer Tamrakar, and Bal Krishna Bal
Information and Language Processing Research Lab, Kathmandu University, Nepal

## Acknowledgments

This research was funded by Kathmandu University Research, Development, and Innovation (KU RDI). We thank our student team members and expert advisors, as well as our data annotators and the ILPRL lab team for their support throughout this research.
