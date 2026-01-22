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
                extraction_class="parameter",
                extraction_text="115 KM",
                attributes={"parameter_type": "power"}
            ),
            lx.data.Extraction(
                extraction_class="parameter",
                extraction_text="Diesel",
                attributes={"parameter_type": "fuel_type"}
            ),
             lx.data.Extraction(
                extraction_class="parameter",
                extraction_text="Brzozów (Podkarpackie)",
                attributes={"parameter_type": "place_of_sale"}
            ),
            lx.data.Extraction(
                extraction_class="parameter",
                extraction_text="142 000 km",
                attributes={"parameter_type": "mileage"}
            ),
            lx.data.Extraction(
                extraction_class="parameter",
                extraction_text="19 500 PLN",
                attributes={"parameter_type": "price"}
            ),
            lx.data.Extraction(
                extraction_class="parameter",
                extraction_text="2013",
                attributes={"parameter_type": "year_of_production"}
            ),
            lx.data.Extraction(
                extraction_class="parameter",
                extraction_text="Manualna",
                attributes={"parameter_type": "gearbox"}
            ),
        ]
    )
]

input_text = """Jak pozycjonowane są ogłoszenia?
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

    Prywatny sprzedawca • Opublikowano 7 godzin temu

19 500

PLN

Poniżej średniej
Sprawdź możliwości finansowania
Volkswagen Golf 1.4 Edition

1390 cm3 • 80 KM

    168 000 km
    Benzyna
    Manualna
    2012

    Majdan Golczański (Podkarpackie)

    Prywatny sprzedawca • Opublikowano 5 dni temu

17 500

PLN
Sprawdź możliwości fi"""

# Run the extraction
result = lx.extract(
    text_or_documents=input_text,
    prompt_description=prompt,
    examples=examples,
    model_id="gemini-2.5-flash",
)


for extraction in result.extractions:
    print(f"{extraction.extraction_class} -> {extraction.extraction_text}\n")