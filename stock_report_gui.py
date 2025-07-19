import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import datetime
import os
import tkinter as tk
from tkinter import messagebox

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    hist = stock.history(period="6mo")
    return info, hist

def generate_chart(ticker, hist):
    plt.figure(figsize=(10, 5))
    plt.plot(hist['Close'], label='Close Price', color='blue')
    plt.title(f"{ticker} - Price Trend (6 Months)")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    chart_path = f"{ticker}_chart.png"
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def create_pdf_report(ticker, info, chart_path, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt=f"Stock Report: {ticker}", ln=True, align='C')
    pdf.set_font("Arial", size=12)

    fields = ['longName', 'sector', 'industry', 'marketCap', 'trailingPE', 'forwardPE', 'profitMargins', 'beta', 'dividendYield']
    for field in fields:
        value = info.get(field, 'N/A')
        pdf.cell(200, 10, txt=f"{field}: {value}", ln=True)

    pdf.image(chart_path, x=10, y=None, w=180)
    pdf.output(output_path)
    os.remove(chart_path)

def run_analysis(tickers):
    today = datetime.date.today()
    os.makedirs("reports", exist_ok=True)
    success_count = 0
    for ticker in tickers:
        try:
            info, hist = fetch_stock_data(ticker)
            chart_path = generate_chart(ticker, hist)
            output_path = f"reports/{ticker}_report_{today}.pdf"
            create_pdf_report(ticker, info, chart_path, output_path)
            print(f"[✓] Generated report for {ticker}: {output_path}")
            success_count += 1
        except Exception as e:
            print(f"[X] Failed to process {ticker}: {e}")
    return success_count

# GUI 部分
if __name__ == "__main__":
    def submit():
        raw = entry.get()
        tickers = [t.strip().upper() for t in raw.split(",") if t.strip()]
        if not tickers:
            messagebox.showerror("Error", "Please enter at least one valid stock ticker.")
            return
        count = run_analysis(tickers)
        if count > 0:
            messagebox.showinfo("Success", f"Reports generated for {count} stock(s).")
        else:
            messagebox.showerror("Error", "No reports were generated.")

    root = tk.Tk()
    root.title("Stock Report Generator")
    root.geometry("400x180")
    root.resizable(False, False)

    tk.Label(root, text="Enter stock symbols (comma-separated):", font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(root, width=40, font=("Arial", 12))
    entry.pack(pady=5)
    tk.Button(root, text="Generate PDF Report", command=submit, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=15)

    root.mainloop()
