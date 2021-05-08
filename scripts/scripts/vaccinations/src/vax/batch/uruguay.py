import os

import pandas as pd


def main(paths):
    df = pd.read_csv(
        "https://raw.githubusercontent.com/3dgiordano/covid-19-uy-vacc-data/main/data/Uruguay.csv",
        usecols=[
            "location",
            "date",
            "vaccine",
            "source_url",
            "total_vaccinations",
            "people_vaccinated",
            "people_fully_vaccinated",
        ]
    )
    df.to_csv(paths.out_tmp("Uruguay"), index=False)


if __name__ == "__main__":
    main()
