import pandas as pd
from pathlib import Path

PROTEIN_PATH = Path(__file__).parent.parent.parent / "data/train_proteins.csv"
PEPTIDE_PATH = Path(__file__).parent.parent.parent / "data/train_peptides.csv"
CLINICAL_PATH = Path(__file__).parent.parent.parent / "data/train_clinical_data.csv"

def prepare_training_data(protein_path: Path = PROTEIN_PATH,
                          peptide_path: Path = PEPTIDE_PATH,
                          clinical_path: Path = CLINICAL_PATH) -> pd.DataFrame:

    df = pd.read_csv(file_path)
