import pandas as pd
from pathlib import Path

PROTEIN_PATH = Path(__file__).parent.parent.parent / "data/train_proteins.csv"
PEPTIDE_PATH = Path(__file__).parent.parent.parent / "data/train_peptides.csv"
CLINICAL_PATH = Path(__file__).parent.parent.parent / "data/train_clinical_data.csv"

def prepare_training_data(protein_path: Path = PROTEIN_PATH,
                          peptide_path: Path = PEPTIDE_PATH,
                          clinical_path: Path = CLINICAL_PATH) -> pd.DataFrame:

    df_proteins = pd.read_csv(protein_path)
    df_peptides = pd.read_csv(peptide_path)
    df_clinical = pd.read_csv(clinical_path)

    df_proteins_peptides = df_proteins.merge(df_peptides, how='inner', on = ['visit_id', 'visit_month', 'patient_id', 'UniProt'])
    df_train = df_proteins_peptides.merge(df_clinical, how='left', on=['visit_id', 'visit_month', 'patient_id'])
