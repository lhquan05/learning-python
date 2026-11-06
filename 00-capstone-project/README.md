# 🏆 Capstone Project: Matchday Store & Financial Analytics System
> **A Hybrid Retail POS, Smart Inventory, Accounting Engine, and Premier League Card Collector App**

---

## 📌 Project Overview
Welcome to the **Matchday Store & Financial Analytics System** capstone project! 

This project is designed as an immersive, project-based learning experience. It combines real-world retail workflows inspired by UK convenience stores (e.g., Tesco, Co-op) with accounting automation, financial analytics, and a gamified **Premier League Player Card Collection** feature.

By completing this application, you will gain hands-on expertise in Python fundamentals, Object-Oriented Programming (OOP), desktop GUI design, data manipulation with **Pandas**, probability simulation with **NumPy**, and real-world accounting mechanics.

---

## 🛠️ Tech Stack & Prerequisites
* **Language:** Python 3.8+
* **Data & Analytics:** `pandas` (Excel file parsing, financial aggregation), `numpy` (probability calculations & gacha mechanics)
* **GUI Framework:** `tkinter` (or `streamlit` for a web-based alternative)
* **Storage Layer:** Excel Files (`inventory.xlsx`, `sales_history.xlsx`, `customers.xlsx`)

### Required Python Libraries
To install the required dependencies, run:
```bash
pip install pandas numpy openpyxl
```

---

## 🎯 Core Requirements

### 1. Store Inventory Management (`inventory.xlsx`)
* All product catalogs, cost prices, selling prices, and stock levels must be managed dynamically via an Excel file (`inventory.xlsx`).
* **Accounting Assets:** Automatically compute **Total Inventory Asset Value** (`Stock * Cost Price`) using `pandas`.
* **Low Stock Warning:** Flag products falling below a defined stock threshold (e.g., $\le 3$ units).
* **Excel Reload Capability:** Allow external edits by accountants in Excel and sync updates in real-time inside the application via a "Reload from Excel" button.

### 2. POS Checkout & Smart "Meal Deal" Algorithm
* **Item Scanning:** Tabular GUI allowing users to browse items by category (Main, Snack, Drink) and scan them into an active cart.
* **UK Meal Deal Optimization Algorithm:**
  * Automatically detect combinations of **1 Main + 1 Snack + 1 Drink** tagged for the deal.
  * Apply a fixed promotional price (e.g., £3.95).
  * **Customer Savings Maximization:** Prioritize grouping the items with the highest standalone retail prices into the Meal Deal to deliver maximum savings to the customer.
* **Transaction Logging:** Append completed sales into `sales_history.xlsx` with timestamps, line items, VAT (20%), and final totals.

### 3. Payment, Bill Splitting & Clubcard Loyalty
* **Split Bill Tool:** Calculate individual shares when a group splits the total bill evenly ($\text{Share} = \frac{\text{Total}}{N \text{ People}}$).
* **Loyalty Clubcard:** Track customer IDs to accumulate loyalty points and bind unlocked digital rewards to user profiles.

### 4. Fan Zone & Gacha Player Card Collector
* **Transaction Reward Trigger:** Upon checkout completion, trigger a **NumPy** probability simulation to drop a random Premier League digital trading card (e.g., Erling Haaland, Bukayo Saka, Cole Palmer).
* **Card Album:** Save earned cards to the customer's profile inventory (`Dream Team Collection`).

---

## 🖥️ Graphical User Interface (UI) Architecture

The application must feature an intuitive multi-tab window with at least **3 core tabs**:

```
+-----------------------------------------------------------------------+
|  [🛒 Self-Checkout POS]   [📊 Excel Inventory]   [⚽ Matchday Fan Zone]  |
+-----------------------------------------------------------------------+
|                                                                       |
|  Tab 1: Product Catalog Table | Active Cart | Total & Split Bill      |
|  Tab 2: Excel Live Table     | Restock Form| Pandas Inventory Stats  |
|  Tab 3: Card Collection Album| Gacha Drop  | NumPy Odds Display      |
|                                                                       |
+-----------------------------------------------------------------------+
```

1. **Tab 1: 🛒 Self-Checkout POS**
   * Left side: `Treeview` catalog displaying Product ID, Name, Category, Price, Stock. Double-click to scan.
   * Right side: Real-time cart listbox showing items, applied Meal Deal discounts, subtotal, and tax.
   * Action bar: Bill splitting entry box, "Calculate Split" button, and "Complete Checkout" button.
2. **Tab 2: 📊 Excel Inventory & Financial Reports**
   * Live data grid showing `inventory.xlsx`.
   * Restock control panel (Quantity input + "Add Stock" button).
   * "Reload from Excel" button to refresh external spreadsheet modifications.
3. **Tab 3: ⚽ Matchday Fan Zone & Dream Team**
   * Digital album grid displaying collected player cards, positions, clubs, and overall ratings.
   * Popup/banner announcing new cards earned after checkout.

---

## 🚀 Advanced Features (Killer Portfolio Enhancements)

*Take your application to the next level with these industry-grade accounting and analytics modules!*

### 1. Automated P&L (Profit and Loss) Financial Statement 📈
* **Cost of Goods Sold (COGS):** Extend the Excel dataset to include `Cost_Price`.
* **Automated Financial Reporting:** Use `pandas` to generate an automated income statement:
  $$\text{Gross Revenue} - \text{COGS} = \text{Gross Profit}$$
  $$\text{Gross Profit} - \text{VAT (20\%)} = \text{Net Profit}$$
* Export this report automatically to a `PnL_Report.xlsx` file upon closing a shift.

### 2. Market Basket Analysis & Cross-Selling Recommendations 🛒
* Analyze historical sales from `sales_history.xlsx` using `pandas`.
* Identify products frequently bought together (e.g., Chicken Sandwich & Coca-Cola) and display "Frequently Bought Together" recommendations at checkout.

### 3. Inventory Turnover & Aging Analysis ⏳
* Categorize inventory into **Fast-Moving** and **Slow-Moving** assets based on sales velocity to help accountants identify dead stock needing clearance.

### 4. Smart Automated Purchase Orders (PO) 📦
* Calculate average daily consumption rates using **NumPy**.
* When stock drops below safety stock levels, auto-generate a vendor-ready `Purchase_Order.xlsx`.

### 5. Matchday Dynamic Surge Pricing ⚡
* Simulate dynamic pricing adjustments during big matchdays (e.g., increase snack and drink prices by 5-10% during high-demand games) to model revenue optimization principles.

### 6. Football Minigame: Matchday Score Predictor & Card Fusion ⚽
* **Match Score Predictor:** Allow customers to predict Premier League match scores at POS checkout for a chance to win *Legend Class* player cards (90+ rating).
* **Card Fusion System:** Implement an algorithm allowing users to combine 3 duplicate player cards to forge 1 higher-tier card.

---

## 📁 Suggested Project Structure

```text
matchday-store-app/
├── assets/                  # Icons and images (optional)
├── data/
│   ├── inventory.xlsx       # Product catalog, prices, and stock
│   ├── sales_history.xlsx   # Transaction logs
│   └── customers.xlsx       # Customer Clubcard and card collection data
├── src/
│   ├── __init__.py
│   ├── pos_logic.py         # Cart and Meal Deal grouping algorithms
│   ├── accounting.py        # Pandas P&L report generation & analytics
│   ├── gacha.py             # NumPy probability & player card logic
│   └── gui.py               # Tkinter / Streamlit interface
├── README.md                # Project assignment guide
└── main.py                  # App entry point
```

---

## 📜 License & Acknowledgments
Created as an educational capstone project for hands-on Python programming, accounting automation, and financial analysis. Inspired by UK retail systems and Premier League matchdays.
