import langextract as lx
import textwrap

# 1. Define the prompt and extraction rules
prompt = textwrap.dedent("""\
        Extract technical parameters from cars for sale.
        Parameters are:
                - car name
                - power
                - fuel type
                - place of sale
                - mileage in kilometers
                - price
                - gearbox
                - year""")

# 2. Provide a high-quality example to guide the model
examples = [
    lx.data.ExampleData(
        text=""" Jak pozycjonowane są ogłoszenia?
Możliwość finansowania

Stan

Stan uszkodzeń
Ford Focus 1.6 TDCi Gold X (Edition Start)

1560 cm3 • 115 KM • 1.6 TDCI * 115KM*Oryginał Lak* Niemcy*Oplacona

    142 000 km
    Diesel
    Manualna
    2013

    Brzozów (Podkarpackie)

    Prywatny sprzedawca • Opublikowano 6 godzin temu

19 500

PLN

Poniżej średniej
Sprawdź możliwości finansowania
""",
        extractions=[
            lx.data.Extraction(
                extraction_class="car",
                extraction_text="Ford Focus 1.6 TDCi Gold X (Edition Start)",
            ),
            lx.data.Extraction(
                extraction_class="power",
                extraction_text="115 KM",
                attributes={"parameter_type": "power"}
            ),
            lx.data.Extraction(
                extraction_class="fuel",
                extraction_text="Diesel",
                attributes={"parameter_type": "fuel_type"}
            ),
             lx.data.Extraction(
                extraction_class="place",
                extraction_text="Brzozów (Podkarpackie)",
                attributes={"parameter_type": "place_of_sale"}
            ),
            lx.data.Extraction(
                extraction_class="mileage",
                extraction_text="142 000 km",
                attributes={"parameter_type": "mileage"}
            ),
            lx.data.Extraction(
                extraction_class="price",
                extraction_text="19 500 PLN",
                attributes={"parameter_type": "price"}
            ),
            lx.data.Extraction(
                extraction_class="year",
                extraction_text="2013",
                attributes={"parameter_type": "year_of_production"}
            ),
            lx.data.Extraction(
                extraction_class="gearbox",
                extraction_text="Manualna",
                attributes={"parameter_type": "gearbox"}
            ),
        ]
    )
]

import sys
input_text = ''.join(sys.stdin.readlines())


result = lx.extract(
    text_or_documents=input_text,
    prompt_description=prompt,
    examples=examples,
    model_id="gemini-2.5-flash",
)

# car,power,fuel_type,place_of_sale,mileage,price,year_of_production,gearbox
extractions = []

for extraction in result.extractions:
    eclass = extraction.extraction_class
    etext = extraction.extraction_text

    if eclass == 'car':
        extractions.append({'car': etext})
    else:
        extractions[len(extractions)-1][eclass] = etext


import json
output_file_path = sys.argv[1]
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(extractions, f, indent=True, ensure_ascii=False)