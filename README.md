# Abia State Agricultural Decision Support System (ADSS)

The **Abia State Agricultural Decision Support System (ADSS)** is a specialized software solution designed to empower farmers and agricultural stakeholders in Abia State with real-time, data-driven insights. It integrates automated weather monitoring, historical climate analysis, and agronomic modeling to aid in critical farm management decisions.

## 🎯 Project Goals

- **Automate Data Collection**: Continuously retrieve and archive hyper-local weather data.
- **Mitigate Climate Risk**: Provide real-time alerts for drought and waterlogging.
- **Optimize Planting Schedules**: Recommend optimal planting sizes based on historical data.
- **Enhance Crop Planning**: Assess crop suitability dynamically.

## 🚀 Key Features

The application is structured into **7 interactive modules**:

1.  **Overview & Trends**: Real-time metrics (Temp, Humidity, Wind), statistical summaries, and temperature trends.
2.  **Weather Forecast**: 48-hour hourly forecast and 5-day daily outlook for planning farm operations.
3.  **Historical Trends**: Long-term climate analysis including annual rainfall, drought frequency, and planting onset estimation.
4.  **Risk Analysis**: Early warning system for drought ( < 5mm/week) and waterlogging ( > 150mm/week).
5.  **GDD Tracking (Growing Degree Days)**: Phenological tracking to estimate crop maturity for crops like Maize, Rice, Cassava, and Yam.
6.  **Crop Planning**: Strategic decision support comparing current seasons against historical averages and assessing crop suitability.
7.  **Data Archive**: Tabular view of raw weather data with export capabilities.

## 🛠️ Technology Stack

-   **Frontend**: [Streamlit](https://streamlit.io/) (Python)
-   **Backend Data Collection**: Python scripts (`data_collector.py`)
-   **Database**: [Supabase](https://supabase.com/) (PostgreSQL)
-   **Visualization**: [Plotly](https://plotly.com/)
-   **Automation**: GitHub Actions (Virtual Weather Station)
-   ** libraries**: `requests`, `pandas`, `schedule`, `numpy`

## 📦 Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/jemeka-php/weather-sync.git
    cd Weather_data_project
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Configuration**:
    Create a `.env` file in the root directory based on `.env.example`. You will need:
    -   `SUPABASE_URL`
    -   `SUPABASE_KEY`
    -   `OPENWEATHER_API_KEY`

4.  **Run the Dashboard**:
    ```bash
    streamlit run dashboard.py
    ```

## 📖 Usage

### Running the Data Collector
To start collecting weather data manually:
```bash
python data_collector.py
```
*Note: In production, this is handled by GitHub Actions.*

### accessing the Dashboard
Once the Streamlit app is running, navigate to the local URL provided (usually `http://localhost:8501`). Use the sidebar to switch between the 7 different modules.

## 📂 Project Structure

-   `dashboard.py`: Main Streamlit application.
-   `data_collector.py`: Backend script for fetching and syncing data.
-   `config.py`: Configuration for crop profiles and API keys.
-   `market_prices.py` / `seasonal_crops.py`: Helper modules for specific logic.
-   `.github/workflows`: Automation workflows.

## 👥 Contributors
-   **Developer**: [John Chukwuemeka/Techrise 2.0 Data Enginering Class B, Group 3]

---
*For detailed documentation, refer to `ADSS_Project_Documentation.md` and `Dashboard_User_Guide.md` included in the project.*
