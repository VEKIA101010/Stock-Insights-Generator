# 📈 Stock Insights Generator

A powerful tool for financial analysts to automatically generate PDF reports containing both **technical charts** and **fundamental metrics** of selected stocks.

>  One-click insights for smarter investment decisions.

---

##  Features

-  Fetch real-time stock data via [Yahoo Finance](https://finance.yahoo.com)
-  Generate 6-month price trend charts with `matplotlib`
-  Include financial metrics like:
  - PE ratio
  - Market Cap
  - Profit Margins
  - Beta
  - Dividend Yield
-  Export report as **PDF**
-  Analyze multiple stocks in batch
-  Modular structure, easy to extend

---

##  Preview

### Sample Chart Output

![Price Chart](example_chart.png)

### Sample PDF Report

>  `reports/AAPL_report_2025-07-19.pdf`

![PDF Preview](example_pdf_preview.png)

---

##  Installation

Make sure Python 3.7+ is installed.

```bash
git clone https://github.com/yourusername/stock-insights-generator.git
cd stock-insights-generator
pip install -r requirements.txt

stock_list = ["AAPL", "MSFT", "TSLA"]
python main.py
stock-insights-generator/
├── main.py               # Main script
├── requirements.txt      # Required packages
├── README.md             # This file
├── reports/              # Generated PDFs
└── example_chart.png     # Example price chart
pip install -r requirements.txt
