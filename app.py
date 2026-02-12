"""
Churn Intelligence System - Premium Dashboard
Enhanced UI with professional design
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# =============================================================================
# CONFIGURATION & THEME
# =============================================================================

# Custom theme
st.set_page_config(
    page_title="Churn Intelligence System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium look
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    /* Main container */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }

    /* Header styling */
    .header-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }

    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        font-size: 1.2rem;
        color: #64748b;
        font-weight: 400;
    }

    /* Card styling */
    .metric-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
        height: 100%;
    }

    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .metric-label {
        font-size: 0.875rem;
        color: #64748b;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }

    .metric-delta {
        font-size: 0.875rem;
        font-weight: 600;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        display: inline-block;
    }

    .delta-positive {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
    }

    .delta-negative {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
    }

    /* Risk badges */
    .risk-badge {
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        display: inline-block;
    }

    .risk-green {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
    }

    .risk-amber {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
    }

    .risk-red {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        animation: pulse-red 2s infinite;
    }

    @keyframes pulse-red {
        0%, 100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.4); }
        50% { box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); }
    }

    /* Section headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Table styling */
    .dataframe {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.4);
    }

    /* Info box */
    .info-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 4px solid #f59e0b;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
    }

    /* Success box */
    .success-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 4px solid #10b981;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
    }

    /* Warning box */
    .warning-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-left: 4px solid #ef4444;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# DATA LOADING
# =============================================================================

@st.cache_data
def load_data():
    """Load and process the churn dataset"""
    try:
        df = pd.read_csv('data/churn_intelligence_dataset.csv')
        df['signup_date'] = pd.to_datetime(df['signup_date'])
        if 'churn_date' in df.columns:
            df['churn_date'] = pd.to_datetime(df['churn_date'], errors='coerce')
        df['last_login_date'] = pd.to_datetime(df['last_login_date'])
        return df
    except FileNotFoundError:
        st.error("📁 Dataset not found. Please ensure data/churn_intelligence_dataset.csv exists.")
        return None

@st.cache_data
def calculate_risk_scores(df):
    """Calculate churn risk scores for all users"""
    if df is None:
        return None

    scores = []
    for _, user in df.iterrows():
        if user.get('churned', 'no') == 'yes':
            continue

        login_score = 25 if user.get('total_logins_30d', 0) < 2 else 0
        onboarding_score = 20 if user.get('onboarding_step_reached', 1) <= 3 else 0
        feature_score = 20 if user.get('features_used_count', 0) <= 2 else 0
        collab_score = 20 if user.get('used_collaboration', 'no') == 'no' else 0
        inactive_score = 15 if user.get('days_since_last_login', 0) >= 7 else 0

        total_score = login_score + onboarding_score + feature_score + collab_score + inactive_score

        if total_score <= 30:
            tier = 'GREEN'
        elif total_score <= 60:
            tier = 'AMBER'
        else:
            tier = 'RED'

        scores_list = [
            ('Low Login Frequency', login_score),
            ('Onboarding Stalled', onboarding_score),
            ('Low Feature Adoption', feature_score),
            ('No Collaboration', collab_score),
            ('Inactive 7+ Days', inactive_score)
        ]
        primary_factor = max(scores_list, key=lambda x: x[1])[0] if total_score > 0 else 'Healthy'

        scores.append({
            'user_id': user['user_id'],
            'email': user['email'],
            'plan_type': user['plan_type'],
            'monthly_revenue': user['monthly_revenue'],
            'risk_score': total_score,
            'risk_tier': tier,
            'primary_risk_factor': primary_factor,
            'recommended_action': 'Human Outreach (24hr)' if tier == 'RED' else (
                'Send Nudge (48hr)' if tier == 'AMBER' else 'Monitor Monthly'
            ),
            'total_logins_30d': user.get('total_logins_30d', 0),
            'onboarding_step_reached': user.get('onboarding_step_reached', 1),
            'features_used_count': user.get('features_used_count', 0),
            'used_collaboration': user.get('used_collaboration', 'no'),
            'days_since_last_login': user.get('days_since_last_login', 0)
        })

    return pd.DataFrame(scores)

# =============================================================================
# COMPONENTS
# =============================================================================

def render_header():
    """Render premium header"""
    st.markdown("""
    <div class="header-container">
        <div class="main-title">🎯 Churn Intelligence System</div>
        <div class="subtitle">Real-time Customer Retention Analytics & Early Warning Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

def render_kpi_cards(df, scores_df):
    """Render enhanced KPI cards"""
    active_users = len(df[df['churned'] == 'no'])
    at_risk_count = len(scores_df[scores_df['risk_tier'].isin(['AMBER', 'RED'])])
    at_risk_pct = (at_risk_count / active_users * 100) if active_users > 0 else 0
    mrr_at_risk = scores_df[scores_df['risk_tier'].isin(['AMBER', 'RED'])]['monthly_revenue'].sum()
    churn_rate = (len(df[df['churned'] == 'yes']) / len(df) * 100)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Active Users</div>
            <div class="metric-value">{active_users:,}</div>
            <div class="metric-delta delta-positive">Total Base</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">At-Risk Users</div>
            <div class="metric-value">{at_risk_count}</div>
            <div class="metric-delta delta-negative">{at_risk_pct:.1f}% Need Attention</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">MRR at Risk</div>
            <div class="metric-value">${mrr_at_risk:,.0f}</div>
            <div class="metric-delta delta-negative">Monthly Revenue</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Churn Rate</div>
            <div class="metric-value">{churn_rate:.1f}%</div>
            <div class="metric-delta {'delta-positive' if churn_rate < 25 else 'delta-negative'}">Target: 20%</div>
        </div>
        """, unsafe_allow_html=True)

def render_risk_distribution(scores_df):
    """Render enhanced risk distribution chart"""
    tier_counts = scores_df['risk_tier'].value_counts().reset_index()
    tier_counts.columns = ['Risk Tier', 'Count']

    colors = {'GREEN': '#10B981', 'AMBER': '#F59E0B', 'RED': '#EF4444'}

    fig = go.Figure(data=[go.Pie(
        labels=tier_counts['Risk Tier'],
        values=tier_counts['Count'],
        marker=dict(colors=[colors[t] for t in tier_counts['Risk Tier']]),
        textinfo='percent+label',
        textfont_size=14,
        hole=0.7,
        hovertemplate='<b>%{label}</b><br>Users: %{value}<br>Percentage: %{percent}<extra></extra>'
    )])

    fig.update_layout(
        title=dict(
            text='<b>User Risk Distribution</b>',
            font=dict(size=18, color='#1e293b')
        ),
        height=400,
        margin=dict(t=80, b=20, l=20, r=20),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.1,
            xanchor="center",
            x=0.5,
            font=dict(size=12)
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig, use_container_width=True)

def render_onboarding_funnel(df):
    """Render enhanced onboarding funnel"""
    funnel_data = df.groupby('onboarding_step_reached').agg({
        'user_id': 'count',
        'churned': lambda x: (x == 'yes').sum()
    }).reset_index()
    funnel_data.columns = ['Step', 'Total Users', 'Churned']
    funnel_data['Churn Rate'] = (funnel_data['Churned'] / funnel_data['Total Users'] * 100).round(1)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(
            x=funnel_data['Step'],
            y=funnel_data['Total Users'],
            name='Total Users',
            marker=dict(
                color='#4F46E5',
                line=dict(color='#3730A3', width=2)
            ),
            text=funnel_data['Total Users'],
            textposition='outside',
            textfont=dict(size=12, color='#4F46E5')
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=funnel_data['Step'],
            y=funnel_data['Churn Rate'],
            name='Churn Rate',
            mode='lines+markers',
            marker=dict(size=12, color='#EF4444'),
            line=dict(color='#EF4444', width=4),
            text=funnel_data['Churn Rate'].astype(str) + '%',
            textposition='top center',
            textfont=dict(size=11, color='#EF4444')
        ),
        secondary_y=True,
    )

    fig.update_xaxes(
        title_text="<b>Onboarding Step</b>",
        title_font=dict(size=14, color='#64748b'),
        tickfont=dict(size=12),
        gridcolor='#e2e8f0'
    )

    fig.update_yaxes(
        title_text="<b>Number of Users</b>",
        title_font=dict(size=14, color='#64748b'),
        tickfont=dict(size=12),
        gridcolor='#e2e8f0',
        secondary_y=False
    )

    fig.update_yaxes(
        title_text="<b>Churn Rate (%)</b>",
        title_font=dict(size=14, color='#64748b'),
        tickfont=dict(size=12),
        gridcolor='#e2e8f0',
        secondary_y=True,
        range=[0, 100]
    )

    fig.update_layout(
        title=dict(
            text='<b>🎯 The 6.5x Insight: Users Who Reach Step 7+ Have 6.5x Better Retention</b>',
            font=dict(size=16, color='#1e293b')
        ),
        height=450,
        margin=dict(t=80, b=60, l=60, r=60),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=12)
        ),
        hovermode='x unified',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.5)'
    )

    st.plotly_chart(fig, use_container_width=True)

def render_at_risk_users_table(scores_df):
    """Render enhanced at-risk users table"""
    st.markdown('<div class="section-header">🚨 At-Risk Users Requiring Attention</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        tier_filter = st.multiselect(
            'Risk Tier',
            options=['AMBER', 'RED'],
            default=['AMBER', 'RED'],
            label_visibility='collapsed'
        )

    with col2:
        plan_filter = st.multiselect(
            'Plan Type',
            options=scores_df['plan_type'].unique().tolist(),
            default=scores_df['plan_type'].unique().tolist(),
            label_visibility='collapsed'
        )

    with col3:
        sort_by = st.selectbox(
            'Sort By',
            options=['Risk Score ↓', 'Revenue ↓', 'Inactivity ↓'],
            label_visibility='collapsed'
        )

    filtered_df = scores_df[
        (scores_df['risk_tier'].isin(tier_filter)) &
        (scores_df['plan_type'].isin(plan_filter))
    ].copy()

    if sort_by == 'Risk Score ↓':
        filtered_df = filtered_df.sort_values('risk_score', ascending=False)
    elif sort_by == 'Revenue ↓':
        filtered_df = filtered_df.sort_values('monthly_revenue', ascending=False)
    else:
        filtered_df = filtered_df.sort_values('days_since_last_login', ascending=False)

    display_df = filtered_df.head(20).copy()

    # Format for display with HTML styling
    def format_tier(tier):
        colors = {'GREEN': '#10b981', 'AMBER': '#f59e0b', 'RED': '#ef4444'}
        return f'<span style="background: {colors[tier]}; color: white; padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 11px;">{tier}</span>'

    def format_score(score):
        color = '#ef4444' if score >= 60 else '#f59e0b' if score >= 30 else '#10b981'
        return f'<span style="color: {color}; font-weight: 700;">{score}/100</span>'

    display_df['Tier'] = display_df['risk_tier'].apply(format_tier)
    display_df['Risk'] = display_df['risk_score'].apply(format_score)
    display_df['Revenue'] = display_df['monthly_revenue'].apply(lambda x: f'${x}')
    display_df['Primary Risk'] = display_df['primary_risk_factor']
    display_df['Action'] = display_df['recommended_action']

    display_cols = ['user_id', 'email', 'Tier', 'Risk', 'Revenue', 'Primary Risk', 'Action']

    st.markdown(
        display_df[display_cols].to_html(escape=False, index=False),
        unsafe_allow_html=True
    )

def render_user_lookup(scores_df):
    """Render enhanced user lookup"""
    st.markdown('<div class="section-header">🔍 User Intelligence Lookup</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        search_user = st.text_input(
            "",
            placeholder="Search by User ID or Email...",
            label_visibility='collapsed'
        )

    with col2:
        st.write("")
        st.write("")
        search_button = st.button("🔎 Search", type="primary", use_container_width=True)

    with col3:
        st.write("")
        st.write("")
        clear_button = st.button("✖️ Clear", use_container_width=True)

    if clear_button or not search_user:
        return

    if search_button and search_user:
        result = scores_df[
            (scores_df['user_id'].astype(str).str.contains(search_user, case=False)) |
            (scores_df['email'].str.contains(search_user, case=False))
        ]

        if not result.empty:
            user = result.iloc[0]

            # User profile header
            tier_colors = {'GREEN': '#10b981', 'AMBER': '#f59e0b', 'RED': '#ef4444'}
            tier_color = tier_colors.get(user['risk_tier'], '#64748b')

            st.markdown(f"""
            <div style="background: white; border-radius: 16px; padding: 2rem; margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.07);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                    <div>
                        <div style="font-size: 0.875rem; color: #64748b; margin-bottom: 0.25rem;">USER PROFILE</div>
                        <div style="font-size: 1.5rem; font-weight: 700; color: #1e293b;">{user['email']}</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 0.875rem; color: #64748b; margin-bottom: 0.25rem;">RISK ASSESSMENT</div>
                        <div style="background: {tier_color}; color: white; padding: 0.5rem 1.5rem; border-radius: 25px; font-weight: 700; display: inline-block;">
                            {user['risk_tier']} TIER
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # KPI row
            kpi1, kpi2, kpi3, kpi4 = st.columns(4)

            with kpi1:
                st.metric("User ID", user['user_id'])
            with kpi2:
                st.metric("Plan", user['plan_type'])
            with kpi3:
                st.metric("Monthly Revenue", f"${user['monthly_revenue']}")
            with kpi4:
                st.metric("Risk Score", f"{user['risk_score']}/100")

            st.markdown("---")

            # Risk breakdown section
            st.markdown('<div class="section-header">📊 Risk Signal Breakdown</div>', unsafe_allow_html=True)

            signal_data = {
                'Signal': ['Login Frequency', 'Onboarding Progress', 'Feature Usage',
                          'Collaboration', 'Inactivity'],
                'Score': [
                    25 if user['total_logins_30d'] < 2 else 0,
                    20 if user['onboarding_step_reached'] <= 3 else 0,
                    20 if user['features_used_count'] <= 2 else 0,
                    20 if user['used_collaboration'] == 'no' else 0,
                    15 if user['days_since_last_login'] >= 7 else 0
                ],
                'Status': [
                    '⚠️ Low (<2 logins)' if user['total_logins_30d'] < 2 else '✅ Healthy',
                    f"⚠️ Step {user['onboarding_step_reached']}" if user['onboarding_step_reached'] <= 3 else '✅ Step 4+',
                    f"⚠️ {user['features_used_count']} features" if user['features_used_count'] <= 2 else '✅ 3+ features',
                    '⚠️ Not used' if user['used_collaboration'] == 'no' else '✅ Used',
                    f"⚠️ {user['days_since_last_login']} days" if user['days_since_last_login'] >= 7 else '✅ Active'
                ],
                'Impact': [
                    'HIGH' if user['total_logins_30d'] < 2 else 'NONE',
                    'MEDIUM' if user['onboarding_step_reached'] <= 3 else 'NONE',
                    'MEDIUM' if user['features_used_count'] <= 2 else 'NONE',
                    'MEDIUM' if user['used_collaboration'] == 'no' else 'NONE',
                    'LOW' if user['days_since_last_login'] >= 7 else 'NONE'
                ]
            }

            signal_df = pd.DataFrame(signal_data)

            def color_score_row(row):
                score = row['Score']
                if score == 0:
                    return ['background: #d1fae5'] * len(row)
                elif score <= 15:
                    return ['background: #fef3c7'] * len(row)
                else:
                    return ['background: #fee2e2'] * len(row)

            styled = signal_df.style.apply(color_score_row, axis=1)
            st.dataframe(styled, use_container_width=True, hide_index=True)

            # Action recommendation
            st.markdown("---")
            st.markdown('<div class="section-header">💡 Recommended Action</div>', unsafe_allow_html=True)

            if user['risk_tier'] == 'RED':
                st.markdown("""
                <div class="warning-box">
                    <div style="font-weight: 700; font-size: 1.1rem; margin-bottom: 0.5rem;">🔴 HIGH RISK — Immediate Action Required</div>
                    <div>Human outreach within 24 hours. Primary issue: <b>{}</b></div>
                </div>
                """.format(user['primary_risk_factor']), unsafe_allow_html=True)
            elif user['risk_tier'] == 'AMBER':
                st.markdown("""
                <div class="info-box">
                    <div style="font-weight: 700; font-size: 1.1rem; margin-bottom: 0.5rem;">🟡 MEDIUM RISK — Automated Intervention</div>
                    <div>Send contextual nudge within 48 hours. Primary issue: <b>{}</b></div>
                </div>
                """.format(user['primary_risk_factor']), unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="success-box">
                    <div style="font-weight: 700; font-size: 1.1rem; margin-bottom: 0.5rem;">🟢 LOW RISK — Healthy User</div>
                    <div>Continue monthly monitoring. No immediate action needed.</div>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.warning(f"❌ No user found matching '{search_user}'")

def render_churn_trend(df):
    """Render churn trend chart"""
    if 'churn_date' not in df.columns:
        return

    churned = df[df['churned'] == 'yes'].copy()
    churned = churned.dropna(subset=['churn_date'])
    churned['churn_month'] = pd.to_datetime(churned['churn_date']).dt.to_period('M')

    monthly_churn = churned.groupby('churn_month').agg({
        'user_id': 'count',
        'monthly_revenue': 'sum'
    }).reset_index()
    monthly_churn.columns = ['Month', 'Churned Users', 'MRR Lost']
    monthly_churn['Month'] = monthly_churn['Month'].astype(str)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=monthly_churn['Month'],
        y=monthly_churn['Churned Users'],
        mode='lines+markers',
        name='Churned Users',
        line=dict(color='#EF4444', width=4),
        marker=dict(size=12, color='#EF4444'),
        fill='tozeroy',
        fillcolor='rgba(239, 68, 68, 0.1)',
        hovertemplate='<b>%{x}</b><br>Churned: %{y} users<extra></extra>'
    ))

    fig.update_layout(
        title=dict(
            text='<b>📈 Monthly Churn Trend</b>',
            font=dict(size=18, color='#1e293b')
        ),
        height=350,
        xaxis_title="<b>Month</b>",
        yaxis_title="<b>Churned Users</b>",
        margin=dict(t=80, b=60, l=60, r=60),
        hovermode='x unified',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,255,255,0.5)',
        xaxis=dict(gridcolor='#e2e8f0'),
        yaxis=dict(gridcolor='#e2e8f0')
    )

    st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# SIDEBAR
# =============================================================================

def render_sidebar(df):
    """Render enhanced sidebar"""
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: white; margin-bottom: 0.25rem;">
                Churn Intelligence
            </div>
            <div style="font-size: 0.875rem; color: #94a3b8;">
                Early Warning System
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown("""
        <div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;">
            Navigation
        </div>
        """, unsafe_allow_html=True)

        page = st.radio(
            "",
            ["📊 Dashboard", "🔍 User Lookup", "📋 Intervention Tracker", "📈 Analytics"],
            label_visibility='collapsed'
        )

        st.markdown("---")

        # Quick stats in sidebar
        st.markdown("""
        <div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem;">
            Quick Stats
        </div>
        """, unsafe_allow_html=True)

        metric1, metric2 = st.columns(2)
        with metric1:
            st.metric("Total", f"{len(df):,}", help_text="Total users")
        with metric2:
            active = len(df[df['churned'] == 'no'])
            st.metric("Active", f"{active:,}", help_text="Active users")

        st.markdown("---")

        st.markdown("""
        <div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;">
            About
        </div>
        <div style="font-size: 0.875rem; color: #cbd5e1; line-height: 1.5;">
            Real-time analytics for predicting and preventing customer churn using behavioral signals.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align: center; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #334155;">
            <div style="font-size: 0.75rem; color: #64748b;">
                Built with Streamlit + Python
            </div>
            <div style="font-size: 0.75rem; color: #64748b;">
                <a href="https://github.com/shru2704/churn-intelligence-system" style="color: #667eea; text-decoration: none;">
                    View on GitHub →
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    return page

# =============================================================================
# MAIN APP
# =============================================================================

def main():
    # Load data
    df = load_data()
    if df is None:
        st.stop()

    scores_df = calculate_risk_scores(df)
    if scores_df is None:
        st.stop()

    # Render sidebar
    page = render_sidebar(df)

    # Main content area
    render_header()

    if page == "📊 Dashboard":
        render_kpi_cards(df, scores_df)
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            render_risk_distribution(scores_df)
        with col2:
            render_onboarding_funnel(df)
        st.markdown("---")
        render_at_risk_users_table(scores_df)

    elif page == "🔍 User Lookup":
        render_user_lookup(scores_df)

    elif page == "📋 Intervention Tracker":
        st.markdown('<div class="section-header">📋 Intervention Tracker</div>', unsafe_allow_html=True)
        st.info("📌 Intervention tracking feature coming soon! This will log all nudge deliveries and responses.")
        st.markdown("""
        <div class="info-box">
            <div style="font-weight: 600; margin-bottom: 0.5rem;">🚀 Coming Soon</div>
            <div>Full intervention tracking with:</div>
            <ul style="margin-top: 0.5rem; margin-left: 1rem;">
                <li>Nudge delivery logs</li>
                <li>Open and response tracking</li>
                <li>Conversion metrics</li>
                <li>CS team activity history</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif page == "📈 Analytics":
        render_churn_trend(df)

        st.markdown("---")

        st.markdown('<div class="section-header">📊 Feature Usage vs Churn Correlation</div>', unsafe_allow_html=True)

        feature_churn = df.groupby(pd.cut(
            df['features_used_count'],
            bins=[0, 2, 5, 10],
            labels=['Low (1-2)', 'Medium (3-5)', 'High (6+)']
        ))['churned'].apply(lambda x: (x == 'yes').mean() * 100).reset_index()
        feature_churn.columns = ['Feature Usage', 'Churn Rate %']

        fig = px.bar(
            feature_churn,
            x='Feature Usage',
            y='Churn Rate %',
            color='Churn Rate %',
            color_continuous_scale=['#10B981', '#F59E0B', '#EF4444'],
            title='<b>Churn Rate by Feature Usage Depth</b>'
        )

        fig.update_layout(
            height=400,
            margin=dict(t=80, b=60, l=60, r=60),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(255,255,255,0.5)',
            xaxis=dict(gridcolor='#e2e8f0'),
            yaxis=dict(gridcolor='#e2e8f0')
        )

        st.plotly_chart(fig, use_container_width=True)

    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; background: rgba(255,255,255,0.5); border-radius: 12px;">
        <div style="font-size: 0.875rem; color: #64748b;">
            Built with ❤️ using <b>Streamlit</b> • <b>Python</b> • <b>Plotly</b>
        </div>
        <div style="font-size: 0.875rem; color: #64748b; margin-top: 0.5rem;">
            <a href="https://github.com/shru2704/churn-intelligence-system" style="color: #667eea;">
                View Source Code →
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
