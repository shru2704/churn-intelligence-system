"""
Churn Intelligence System - Interactive Dashboard
Built with Streamlit
A fully functional web application for analyzing and predicting customer churn
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Churn Intelligence System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1F2937;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #6B7280;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1F2937;
    }
    .kpi-label {
        font-size: 0.875rem;
        color: #6B7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .kpi-delta {
        font-size: 0.875rem;
        font-weight: 500;
    }
    .delta-positive {
        color: #10B981;
    }
    .delta-negative {
        color: #EF4444;
    }
    .risk-green {
        background-color: #D1FAE5;
        color: #065F46;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.75rem;
    }
    .risk-amber {
        background-color: #FEF3C7;
        color: #92400E;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.75rem;
    }
    .risk-red {
        background-color: #FEE2E2;
        color: #991B1B;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.75rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA LOADING & PROCESSING
# ============================================================================

@st.cache_data
def load_data():
    """Load and process the churn dataset"""
    try:
        df = pd.read_csv('data/churn_intelligence_dataset.csv')
        # Convert date columns
        df['signup_date'] = pd.to_datetime(df['signup_date'])
        if 'churn_date' in df.columns:
            df['churn_date'] = pd.to_datetime(df['churn_date'], errors='coerce')
        df['last_login_date'] = pd.to_datetime(df['last_login_date'])
        return df
    except FileNotFoundError:
        st.error("Dataset not found. Please ensure data/churn_intelligence_dataset.csv exists.")
        return None

@st.cache_data
def calculate_risk_scores(df):
    """Calculate churn risk scores for all users"""
    if df is None:
        return None

    scores = []

    for _, user in df.iterrows():
        # Skip churned users
        if user.get('churned', 'no') == 'yes':
            continue

        # Calculate individual signal scores
        login_score = 25 if user.get('total_logins_30d', 0) < 2 else 0
        onboarding_score = 20 if user.get('onboarding_step_reached', 1) <= 3 else 0
        feature_score = 20 if user.get('features_used_count', 0) <= 2 else 0
        collab_score = 20 if user.get('used_collaboration', 'no') == 'no' else 0
        inactive_score = 15 if user.get('days_since_last_login', 0) >= 7 else 0

        total_score = login_score + onboarding_score + feature_score + collab_score + inactive_score

        # Determine risk tier
        if total_score <= 30:
            tier = 'GREEN'
        elif total_score <= 60:
            tier = 'AMBER'
        else:
            tier = 'RED'

        # Determine primary risk factor
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

# ============================================================================
# DASHBOARD COMPONENTS
# ============================================================================

def render_kpi_cards(df, scores_df):
    """Render KPI cards at the top of dashboard"""
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        active_users = len(df[df['churned'] == 'no'])
        st.metric(
            label="Active Users",
            value=f"{active_users:,}",
            delta=None
        )

    with col2:
        at_risk_count = len(scores_df[scores_df['risk_tier'].isin(['AMBER', 'RED'])])
        at_risk_pct = (at_risk_count / active_users * 100) if active_users > 0 else 0
        st.metric(
            label="At-Risk Users",
            value=f"{at_risk_count}",
            delta=f"{at_risk_pct:.1f}% of active"
        )

    with col3:
        mrr_at_risk = scores_df[scores_df['risk_tier'].isin(['AMBER', 'RED'])]['monthly_revenue'].sum()
        st.metric(
            label="MRR at Risk",
            value=f"${mrr_at_risk:,.0f}",
            delta=None
        )

    with col4:
        churn_rate = (len(df[df['churned'] == 'yes']) / len(df) * 100)
        st.metric(
            label="Churn Rate",
            value=f"{churn_rate:.1f}%",
            delta="Target: 20%"
        )

def render_risk_distribution(scores_df):
    """Render risk tier distribution chart"""
    tier_counts = scores_df['risk_tier'].value_counts().reset_index()
    tier_counts.columns = ['Risk Tier', 'Count']

    colors = {'GREEN': '#10B981', 'AMBER': '#F59E0B', 'RED': '#EF4444'}
    tier_counts['Color'] = tier_counts['Risk Tier'].map(colors)

    fig = px.pie(
        tier_counts,
        values='Count',
        names='Risk Tier',
        color='Risk Tier',
        color_discrete_map=colors,
        title='User Risk Distribution',
        hole=0.6
    )

    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        marker=dict(line=dict(color='#FFFFFF', width=2))
    )

    fig.update_layout(
        height=350,
        margin=dict(t=50, b=0, l=0, r=0),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0,
            xanchor="center",
            x=0.5
        )
    )

    st.plotly_chart(fig, use_container_width=True)

def render_onboarding_funnel(df):
    """Render onboarding funnel analysis"""
    funnel_data = df.groupby('onboarding_step_reached').agg({
        'user_id': 'count',
        'churned': lambda x: (x == 'yes').sum()
    }).reset_index()
    funnel_data.columns = ['Step', 'Total Users', 'Churned']
    funnel_data['Churn Rate'] = (funnel_data['Churned'] / funnel_data['Total Users'] * 100).round(1)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=funnel_data['Step'],
        y=funnel_data['Total Users'],
        name='Total Users',
        marker_color='#4F46E5',
        text=funnel_data['Total Users'],
        textposition='outside'
    ))

    fig.add_trace(go.Scatter(
        x=funnel_data['Step'],
        y=funnel_data['Churn Rate'],
        name='Churn Rate %',
        mode='lines+markers',
        marker=dict(size=10, color='#EF4444'),
        line=dict(color='#EF4444', width=2),
        yaxis='y2',
        text=funnel_data['Churn Rate'].astype(str) + '%',
        textposition='top center'
    ))

    fig.update_layout(
        title='Onboarding Funnel Drop-off & Churn Rate',
        height=350,
        xaxis_title='Onboarding Step Reached',
        yaxis_title='Number of Users',
        yaxis2=dict(
            title='Churn Rate (%)',
            overlaying='y',
            side='right',
            range=[0, 100]
        ),
        margin=dict(t=50, b=0, l=0, r=0),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        barmode='group'
    )

    st.plotly_chart(fig, use_container_width=True)

def render_at_risk_users_table(scores_df):
    """Render at-risk users table with filters"""
    st.subheader("🚨 At-Risk Users (Requiring Attention)")

    # Filters
    col1, col2, col3 = st.columns(3)

    with col1:
        tier_filter = st.multiselect(
            'Filter by Risk Tier',
            options=['AMBER', 'RED'],
            default=['AMBER', 'RED']
        )

    with col2:
        plan_filter = st.multiselect(
            'Filter by Plan',
            options=scores_df['plan_type'].unique().tolist(),
            default=scores_df['plan_type'].unique().tolist()
        )

    with col3:
        sort_by = st.selectbox(
            'Sort by',
            options=['Risk Score (High to Low)', 'Revenue (High to Low)', 'Inactivity (High to Low)'],
            index=0
        )

    # Apply filters
    filtered_df = scores_df[
        (scores_df['risk_tier'].isin(tier_filter)) &
        (scores_df['plan_type'].isin(plan_filter))
    ].copy()

    # Apply sorting
    if sort_by == 'Risk Score (High to Low)':
        filtered_df = filtered_df.sort_values('risk_score', ascending=False)
    elif sort_by == 'Revenue (High to Low)':
        filtered_df = filtered_df.sort_values('monthly_revenue', ascending=False)
    else:
        filtered_df = filtered_df.sort_values('days_since_last_login', ascending=False)

    # Display top 20
    display_df = filtered_df.head(20).copy()

    # Format for display
    display_df['Risk Tier'] = display_df['risk_tier'].apply(
        lambda x: f"<span class='risk-{x.lower()}'>{x}</span>"
    )
    display_df['Monthly Revenue'] = display_df['monthly_revenue'].apply(lambda x: f"${x}")
    display_df['Risk Score'] = display_df['risk_score'].apply(lambda x: f"{x}/100")

    # Select columns to display
    display_cols = ['user_id', 'email', 'Risk Tier', 'Risk Score', 'Monthly Revenue',
                    'primary_risk_factor', 'recommended_action']

    st.markdown(
        display_df[display_cols].to_html(escape=False, index=False),
        unsafe_allow_html=True
    )

def render_user_lookup(scores_df):
    """Render user lookup functionality"""
    st.subheader("🔍 User Lookup")

    col1, col2 = st.columns([2, 1])

    with col1:
        search_user = st.text_input(
            "Search by User ID or Email",
            placeholder="Enter user ID or email address...",
            key="user_search"
        )

    with col2:
        st.write("")
        st.write("")
        search_button = st.button("Look Up User", type="primary")

    if search_button and search_user:
        # Search by user_id or email
        result = scores_df[
            (scores_df['user_id'].astype(str).str.contains(search_user, case=False)) |
            (scores_df['email'].str.contains(search_user, case=False))
        ]

        if not result.empty:
            user = result.iloc[0]

            # User profile card
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("User ID", user['user_id'])
            with col2:
                st.metric("Plan", user['plan_type'])
            with col3:
                st.metric("Monthly Revenue", f"${user['monthly_revenue']}")

            st.markdown("---")

            # Risk assessment
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Risk Score", f"{user['risk_score']}/100")

            with col2:
                tier_emoji = {'GREEN': '🟢', 'AMBER': '🟡', 'RED': '🔴'}
                st.metric("Risk Tier", f"{tier_emoji.get(user['risk_tier'], '')} {user['risk_tier']}")

            with col3:
                st.metric("Primary Risk", user['primary_risk_factor'])

            with col4:
                st.metric("Recommended Action", user['recommended_action'])

            st.markdown("---")

            # Detailed breakdown
            st.subheader("Risk Breakdown")

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
                ]
            }

            signal_df = pd.DataFrame(signal_data)

            # Color code the scores
            def color_score(val):
                if val == 0:
                    return 'color: #10B981'
                elif val <= 15:
                    return 'color: #F59E0B'
                else:
                    return 'color: #EF4444'

            styled_df = signal_df.style.applymap(
                lambda x: color_score(x) if isinstance(x, (int, float)) else '',
                subset=['Score']
            )

            st.dataframe(styled_df, use_container_width=True, hide_index=True)

        else:
            st.warning(f"No user found matching '{search_user}'")

def render_intervention_tracker():
    """Render intervention tracking section"""
    st.subheader("📋 Intervention Tracker")

    # Sample intervention data
    interventions = pd.DataFrame({
        'Date': ['2026-02-10', '2026-02-11', '2026-02-12', '2026-02-13'],
        'User': ['user_47', 'user_132', 'user_89', 'user_156'],
        'Type': ['Onboarding Nudge', 'Feature Discovery', 'Human Outreach', 'Re-engagement'],
        'Status': ['✅ Converted', '⏳ Pending', '✅ Responded', '❌ Churned'],
        'Result': ['Upgraded to Pro', 'Awaiting response', 'Scheduled call', 'Lost']
    })

    st.dataframe(interventions, use_container_width=True, hide_index=True)

def render_churn_trend(df):
    """Render churn trend over time"""
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
        line=dict(color='#EF4444', width=3),
        marker=dict(size=8),
        fill='tozeroy',
        fillcolor='rgba(239, 68, 68, 0.1)'
    ))

    fig.update_layout(
        title='Monthly Churn Trend',
        height=300,
        xaxis_title='Month',
        yaxis_title='Churned Users',
        margin=dict(t=50, b=0, l=0, r=0),
        hovermode='x unified'
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    # Header
    st.markdown('<h1 class="main-header">🎯 Churn Intelligence System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Real-time customer retention analytics and early warning dashboard</p>', unsafe_allow_html=True)

    # Load data
    df = load_data()
    if df is None:
        st.stop()

    scores_df = calculate_risk_scores(df)
    if scores_df is None:
        st.stop()

    # Sidebar
    st.sidebar.title("⚙️ Controls")

    page = st.sidebar.radio(
        "Select View",
        ["📊 Dashboard", "🔍 User Lookup", "📋 Intervention Tracker", "📈 Analytics"],
        label_visibility="collapsed"
    )

    st.sidebar.markdown("---")

    # Quick stats in sidebar
    st.sidebar.subheader("Quick Stats")
    st.sidebar.metric("Total Users", f"{len(df):,}")
    st.sidebar.metric("Active Users", f"{len(df[df['churned'] == 'no']):,}")
    st.sidebar.metric("Churned Users", f"{len(df[df['churned'] == 'yes']):,}")

    # Main content
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
        render_intervention_tracker()

    elif page == "📈 Analytics":
        render_churn_trend(df)

        st.markdown("---")

        st.subheader("Feature Usage vs Churn Rate")

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
            title='Churn Rate by Feature Usage Depth'
        )

        fig.update_layout(height=350, margin=dict(t=50, b=0, l=0, r=0))

        st.plotly_chart(fig, use_container_width=True)

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #6B7280; font-size: 0.875rem;'>
        Built with Streamlit • Python • Plotly • <a href='https://github.com/shru2704/churn-intelligence-system'>GitHub</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
