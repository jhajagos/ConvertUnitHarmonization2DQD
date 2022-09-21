import json
import pandas as pd
import argparse
import pathlib
import numpy as np


def main(supplemental_tables_directory):
    p_sup_tab_dir = pathlib.Path(supplemental_tables_directory)
    table_s1_csv_file = p_sup_tab_dir / "TableS1_Concept_set_members_by_Alias_Feb2022.csv"

    s1_df = pd.read_csv(table_s1_csv_file)
    print(s1_df.columns)

    table_s2_csv_file = p_sup_tab_dir / "TableS2.csv"
    s2_df = pd.read_csv(table_s2_csv_file)
    print(s2_df.columns)

    s1_s2_df = pd.merge(s1_df, s2_df, left_on="N3C codeset id", right_on="codeset_id")

    field_map = {
        "OMOP concept name": "conceptName",
        "OMOP concept id": "conceptId",
        "omop_unit_concept_id": "unitConceptId",
        "omop_unit_concept_name": "unitConceptName",
        "min_acceptable_value": "plausibleValueLow",
        "max_acceptable_value":	"plausibleValueHigh"
    }

    for field_name in field_map:
        s1_s2_df[field_map[field_name]] = s1_s2_df[field_name]

    ohdsi_field_names = [field_map[f] for f in field_map]

    s1_s2_df = s1_s2_df[ohdsi_field_names]

    s1_s2_df["cdmTableName"] = "MEASUREMENT"
    s1_s2_df["cdmFieldName"] = "MEASUREMENT_CONCEPT_ID"
    s1_s2_df["plausibleValueLowThreshold"] = 1
    s1_s2_df["plausibleValueHighThreshold"] = 1
    s1_s2_df["plausibleValueLowNotes"] = "Based on Unit Harmonization Paper"
    s1_s2_df["plausibleValueLowNotes"] = "Based on Unit Harmonization Paper"

    s1_s2_df["unitConceptId"] = s1_s2_df["unitConceptId"].fillna(0)
    s1_s2_df["unitConceptName"] = s1_s2_df["unitConceptName"].fillna("NULL")

    current_columns = list(s1_s2_df.columns)

    field_template = ["cdmTableName", "cdmFieldName", "conceptId", "conceptName", "unitConceptId", "unitConceptName",
                      "plausibleValueLow", "plausibleValueLowThreshold", "plausibleValueLowNotes", "plausibleValueHigh",
                      "plausibleValueHighThreshold", "plausibleValueHighNotes", "plausibleGender", "plausibleGenderThreshold",
                      "plausibleGenderNotes", "isTemporallyConstant", "isTemporallyConstantThreshold", "isTemporallyConstantNotes",
                      "validPrevalenceLow", "validPrevalenceLowThreshold", "validPrevalenceLowNotes", "validPrevalenceHigh",
                      "validPrevalenceHighThreshold", "validPrevalenceHighNotes"]

    for field_name in field_template:
        if field_name not in current_columns:
            s1_s2_df[field_name] = np.nan

    s1_s2_df = s1_s2_df[field_template]
    s1_s2_df.to_csv("unit_harmonization_dqd_measurement_thresholds.csv", index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main("../../data/ocac054_supplementary_data/")

