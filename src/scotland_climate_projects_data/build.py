import pandas as pd
from pathlib import Path

PACKAGES_DIR = Path("data", "packages")
PROJECTS_URL = "https://data.climateemergency.uk/media/data/projects_data.csv"


def build_projects():
    df = pd.read_csv(PROJECTS_URL).rename(
        columns={"authority_code": "local-authority-code"}
    )

    def fix_year(year: int) -> int:
        """
        some years are 2018, 2019, others are 18, 19.
        All should be 4 digit years.
        """
        if year < 100:
            return year + 2000
        return year

    df["end_year"] = df["end_year"].apply(fix_year)

    df.set_index("local-authority-code").to_csv(
        PACKAGES_DIR / "scotland_climate_emissions_projects" / "projects.csv"
    )
