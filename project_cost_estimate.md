# 💰 Project Financial Requirements & Cost Estimate

This document outlines the estimated financial requirements for hosting, maintaining, and scaling the **Abia State Agricultural Decision Support System (ADSS)**. 

Estimates are provided in **USD ($)** and **Nigerian Naira (₦)**, assuming an exchange rate of **$1 USD = ₦1,650**.

---

## 🏗️ 1. Infrastructure & Hosting

| Component | Service Provider | Description | Est. Cost (Monthly) | Est. Cost (Naira) |
| :--- | :--- | :--- | :--- | :--- |
| **Web Hosting** | **Render / DigitalOcean** | Production-grade Cloud Server (VPS) or PaaS to host the Streamlit dashboard 24/7 with auto-scaling. | **$25.00** | **₦41,250** |
| **Database** | **Supabase (Pro)** | PostgreSQL Cloud Database. The Pro tier provides daily backups, larger storage (8GB+), and higher bandwidth for concurrent users. | **$25.00** | **₦41,250** |
| **Domain Name** | **Namecheap / GoDaddy** | Annual renewal for a professional domain (e.g., `abia-adss.ng` or `.com`). *(Calculated monthly)* | **$1.50** | **₦2,475** |
| **Subtotal** | | | **$51.50** | **₦84,975** |

---

## 📡 2. APIs & Data Services

| Component | Service Provider | Description | Est. Cost (Monthly) | Est. Cost (Naira) |
| :--- | :--- | :--- | :--- | :--- |
| **Weather API** | **OpenWeatherMap** | **One Call API 3.0**. <br> - *Free Tier:* 1,000 calls/day (Sufficient for current 3 zones). <br> - *Growth:* Budgeting for expansion to 20+ zones and frequent updates. | **$40.00** | **₦66,000** |
| **SMS Gateway** | **Termii** | **Local Nigerian SMS Gateway**. <br> - *Cost:* ~₦4.00 per SMS unit. <br> - *Est. Volume:* 2,000 farmers × 2 alerts/month = 4,000 SMS. | **$20.00** | **₦33,000** |
| **Email Service** | **SendGrid / Postmark** | Transactional emails for reports and alerts. <br> - *Essentials Plan:* Up to 50k emails/month. | **$15.00** | **₦24,750** |
| **Subtotal** | | | **$75.00** | **₦123,750** |

---

## 🔮 3. Total Project Funding Requirement (Monthly)

| Item | USD ($) | Naira (₦) |
| :--- | :--- | :--- |
| **Infrastructure (Hosting & DB)** | $51.50 | ₦84,975 |
| **Data Services (API & SMS)** | $75.00 | ₦123,750 |
| **Contingency / Misc (10%)** | $12.65 | ₦20,872 |
| **TOTAL MONTHLY RUNNING COST** | **$139.15** | **₦229,597** |

---

## 🚀 4. Scale-Up Considerations (Yearly Projection)

For a 12-month runway to ensure stability during the pilot phase:

*   **Annual Operating budget:** ~$1,670 (approx **₦2,755,000**)
*   **Hardware (Optional):** If deploying physical IoT sensors in zones (optional):
    *   *Cost per Station:* ~$250 (₦412,500)
    *   *Pilot (3 Zones):* $750 (₦1,237,500)

### 💡 Recommendation for Funding Ask
We recommend asking for a seed grant of **$5,000 (approx ₦8.25 Million)** to cover:
1.  **24 Months of Operational Costs** (Hosting, APIs, SMS).
2.  **Deployment of 3 Physical Verification Sensors** to validate API data.
3.  **Farmer Field Training** and Onboarding workshops.
