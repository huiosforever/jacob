import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="VC Crypto Deal Analyzer", layout="wide")
st.title("🪙 VC Crypto Deal Analyzer (Bay Street Framework)")

# -------------------------------
# Sidebar Controls
# -------------------------------

st.sidebar.header("🔧 Chart Controls")

category_map = {
    "Market Dynamics": [
        "Token Price Simulation", "User Growth Curve", "FDV vs TVL", "DEX vs CEX Volume"
    ],
    "Token Health": [
        "Treasury Balance Over Time", "Token Supply Inflation", "Top Holder Concentration", "Staking Participation Rate"
    ],
    "Protocol Performance": [
        "Protocol Revenue YoY", "Bridge Usage", "Chain Gas Fees (last 30d)", "Public Comps Performance"
    ],
    "Governance & Security": [
        "Dev Activity Heatmap", "Validator Count Over Time", "Security Incidents Timeline"
    ]
}

selected_category = st.sidebar.selectbox("📊 Chart Category", list(category_map.keys()))
chart_type = st.sidebar.radio("📈 Chart Type", ["line", "bar", "area"])
animate = st.sidebar.checkbox("🔁 Animate (Simulated Data)", value=False)
sleep_time = st.sidebar.slider("⏱️ Update Delay (sec)", min_value=0, max_value=5, value=0)

# -------------------------------
# Chart Generator
# -------------------------------

def generate_chart(chart_title, chart_type="line"):
    df = pd.DataFrame({
        "x": np.linspace(1, 100, 100),
        "value": np.random.normal(loc=100, scale=10, size=100).cumsum()
    }).set_index("x")

    st.markdown(f"**{chart_title}**")

    if chart_type == "line":
        st.line_chart(df)
    elif chart_type == "bar":
        st.bar_chart(df)
    elif chart_type == "area":
        st.area_chart(df)

# -------------------------------
# Main Content Sections
# -------------------------------

st.header("1. Executive Summary")
st.markdown("""
- **Sector**: DeFi  
- **Thesis**: A decentralized derivatives platform with strong token utility and emissions control.  
- **Key Risks**: Token unlocks begin in 3 months; smart contracts unaudited.  
- **Exit Pathways**: CEX listing (Binance), DEX liquidity mining, potential acquisition by Layer 2 protocol.  
""")

st.header("2. Document Checklist")
checklist_data = {
    "Section": [
        "Pitch Deck", "Tokenomics Sheet", "Smart Contract Audit",
        "Team & Bios", "Market & Strategy", "Legal Structure (SAFT)", "Custom Requests"
    ],
    "Status": ["✅", "✅", "❌", "✅", "✅", "❌", "⏳"]
}
st.dataframe(pd.DataFrame(checklist_data))

st.header("3. Quantamental Metrics")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Private Token Deal")
    st.metric("Token IRR", "27.5%")
    st.metric("FDV", "$150M")
    st.metric("Bay Score", "82")
    st.markdown("- AHA (Holder Alignment): 30\n- LSD (Liquidity/Security Design): 32\n- FX Drag: +20")

with col2:
    st.subheader("Public Comps")
    st.markdown("""
    - **Comps**: $GMX, $DYDX, $INJ  
    - **Median EV/Revenue**: 9.8x  
    - **30D Volatility**: 44%
    """)

st.header("4. Diligence Timeline")
timeline = [
    ("Week 1", "Whitepaper + Token Model Review"),
    ("Week 2", "Dev Activity + Ecosystem Fit"),
    ("Week 3", "Legal/SAFT Review"),
    ("Week 4", "IC Memo + Token Listing Readiness")
]
st.table(pd.DataFrame(timeline, columns=["Week", "Milestone"]))

st.header("5. Summary")
st.success("This protocol demonstrates strong emissions control and ecosystem fit but requires further review of its audit and unlock schedule.")

# -------------------------------
# Chart Grid (4 Columns)
# -------------------------------

st.header("6. Charts & Visualizations")

charts_to_show = category_map[selected_category]
for row in range(0, len(charts_to_show), 4):
    cols = st.columns(4)
    for i in range(4):
        if row + i < len(charts_to_show):
            with cols[i]:
                generate_chart(charts_to_show[row + i], chart_type)
                if animate and sleep_time > 0:
                    time.sleep(sleep_time)
