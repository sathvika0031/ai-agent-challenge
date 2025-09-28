
import pandas as pd, importlib.util
from pathlib import Path
def load_parser(bank): spec = importlib.util.spec_from_file_location(f"{bank}_parser", Path(f"custom_parsers/{bank}_parser.py")); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod.parse
def test_parser_output_matches_csv():
    bank="icici"; parse=load_parser(bank)
    csv_path, pdf_path = Path(f"data/{bank}/result.csv"), Path(f"data/{bank}/sample.pdf")
    file_to_parse = csv_path if csv_path.exists() else pdf_path
    df_out = parse(str(file_to_parse)); assert not df_out.empty
    if csv_path.exists():
        df_ref = pd.read_csv(csv_path)
        for df in [df_out, df_ref]:
            for col in df.columns: df[col] = df[col].fillna(0.0) if df[col].dtype!='object' else df[col].fillna("")
        assert len(df_out)==len(df_ref)
        for col in set(df_ref.columns).intersection(df_out.columns):
            pd.testing.assert_series_equal(df_out[col].reset_index(drop=True), df_ref[col].reset_index(drop=True), check_dtype=False)
