# Deploy Your Churn Intelligence Dashboard to Streamlit Cloud

## Quick Deploy (5 Minutes)

### Step 1: Push Code to GitHub

Your code is already on GitHub. Verify at:
https://github.com/shru2704/churn-intelligence-system

### Step 2: Create Streamlit Cloud Account

1. Go to: https://streamlit.io/cloud
2. Click "Sign up"
3. Sign in with your GitHub account
4. Authorize Streamlit Cloud

### Step 3: Deploy Your App

1. Click "New app" button
2. Select your repository: `shru2704/churn-intelligence-system`
3. Branch: `main`
4. Main file path: `app.py`
5. Click "Deploy"

**That's it!** Your app will be live at: `https://churn-intelligence-system.streamlit.app`

---

## Test Your Dashboard Locally

Before deploying, test locally:

```bash
# Open terminal in your project folder
cd "c:/Users/Shruti/OneDrive/Documents/Desktop/the silent exit"

# Run the app
python -m streamlit run app.py

# Dashboard opens at: http://localhost:8501
```

---

## Dashboard Features

| Feature | Description |
|---------|-------------|
| **Risk Score Calculator** | Auto-calculates churn risk for all users |
| **User Lookup** | Search any user by ID or email |
| **At-Risk List** | Filtered list of Amber + Red users |
| **KPI Cards** | Active users, at-risk count, MRR at risk |
| **Distribution Chart** | Donut chart of risk tiers |
| **Funnel Analysis** | Onboarding drop-off visualization |
| **Churn Trends** | Monthly churn rate over time |

---

## Customization (Optional)

### Change App Title

Edit `app.py`, line 18:
```python
st.set_page_config(
    page_title="Churn Intelligence System",  # Change this
    ...
)
```

### Add Your Logo

1. Create `assets/` folder
2. Add your logo as `logo.png`
3. Update `app.py` to display it

### Change Colors

Edit the CSS in `app.py` (lines 20-60)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Module not found" | Run: `pip install streamlit pandas plotly` |
| "Dataset not found" | Ensure `data/churn_intelligence_dataset.csv` exists |
| App is slow | Reduce dataset size or filter data in queries |
| Charts not showing | Check internet connection (Plotly needs CDN) |

---

## Share Your Dashboard

Once deployed, share the link:
- On LinkedIn: "Just built an interactive churn analytics dashboard!"
- On resume: `streamlit.io/churn-intelligence-system`
- In interviews: "Let me show you the live demo..."

---

**Live Demo URL**: `https://churn-intelligence-system.streamlit.app` (after you deploy)

*For support: https://docs.streamlit.io*
