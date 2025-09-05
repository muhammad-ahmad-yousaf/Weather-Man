# Weather‑Man

**Weather‑Man** is a Python-based command-line application that loads historical daily weather data (such as temperature and humidity) and provides both summary insights and visualization charts. It currently supports weather data for three locations: **Lahore**, **Murree**, and **Dubai**.

---

##  Features

- **Yearly Summary**  
  Identify the hottest day, coldest day, and the most humid day of a given year.

- **Monthly Averages**  
  Compute monthly averages for maximum temperature, minimum temperature, and humidity.

- **Monthly Charts**  
  Visualize daily temperature trends with clear bar charts—either with separate bars for high/low or combined for easy comparison.

---

##  Project Structure

```
Weather‑Man/
│
├── data/
│   ├── lahore_weather/
│   │   └── *.txt
│   ├── Murree_weather/
│   │   └── *.txt
│   └── Dubai_weather/
│       └── *.txt
│
├── monthly_avg.py        # MonthlyAverage class implementation
├── monthly_graph.py      # MonthlyGraph class implementation
├── yearly_max.py         # YearlyMax class implementation
├── main.py               # Main program with interactive CLI
└── README.md             # Project overview and setup guide
```

---

##  Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/muhammad-ahmad-yousaf/Weather-Man.git
   cd Weather-Man
   ```

2. **Ensure your data files** are placed in the respective folders:
   ```
   data/lahore_weather/*.txt
   data/Murree_weather/*.txt
   data/Dubai_weather/*.txt
   ```
   Each `.txt` file should follow the CSV format with headers like:
   ```
   PKT,Max TemperatureC,Mean TemperatureC,Min TemperatureC,...,WindDirDegrees
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

   You’ll be prompted to select a city (Lahore, Murree, Dubai) and interact via menu options:
   - 1: View yearly summary (hottest, coldest, most humid day)
   - 2: Get monthly averages (requires year and month)
   - 3 & 4: Display monthly bar charts (with or without combined visualization)
   - 5: Exit the program

---

##  Example Snapshot

```
1- Lahore
2- Murree
3- Dubai
Select the City: 1

----------------------------------------
1 - Yearly Summary
2 - Monthly Averages
3 - Monthly Chart (separate)
4 - Monthly Chart (combined)
5 - Exit
Enter your option: 1
Enter year (like 2002): 1997

 Highest: 24°C on January 08
 Lowest: 12°C on January 20
 Humid: 100% on January 01
```

---

##  Notes & Recommendations

- Ensure your `.txt` files are properly formatted and encoded in UTF-8.
- Date parsing depends on the `PKT` field in the format `YYYY‑M‑D`. Incorrect entries will be skipped.
- Consider extending the tool:
  - Accept additional cities or datasets.
  - Add new summary features (e.g. wind speed, precipitation).
  - Output to files (CSV or JSON) instead of console print.
  - Implement unit tests to validate data processing and functionality.

---

##  Contributing

Contributions are welcome! Please follow this process:
1. Fork the repo.
2. Create a feature branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m "Add some feature"`.
4. Push to your fork: `git push origin feature-name`.
5. Open a Pull Request here, describing your changes.

---

##  License

This project is licensed under the **MIT License**—feel free to modify and use it freely.

---

**Thank you for exploring Weather‑Man!**  
Feel free to reach out if you’d like help extending the tool, optimizing performance, or improving data handling.
