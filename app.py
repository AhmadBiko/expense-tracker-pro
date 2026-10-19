#[1] Importing the needed functions
import streamlit as st
import plotly.express as px
import json
from expense_functions import (
    add_expense,
    calculate_total,
    calculate_category_total,
    find_most_expensive,
    delete_expense,
    save_expenses,
    load_expenses,
    save_budget,
    load_budget,
    calculate_monthly_total,
    calculate_spending_by_month
)

#[2] Improving the app with wide layout
st.set_page_config(
    layout="wide"
)

#[3] Designing the app with CSS
st.markdown("""
<style>
.st-key-add_expense_card h3,
.st-key-delete_expense_card h3,
.st-key-category_chart_card h3,
.st-key-monthly_budget_card h3,
.st-key-expenses_table_card h3 {
    color: #F8FAFC;
}
.st-key-header_card,
.st-key-add_expense_card,
.st-key-delete_expense_card,
.st-key-category_chart_card,
.st-key-expenses_table_card,
.st-key-monthly_budget_card,
.st-key-monthly_spending_history_card {
    background-color: #0B111B;
    border-radius: 20px;
    padding: 20px
}
.st-key-total_spending_card,
.st-key-expense_count_card,
.st-key-largest_expense_card {
    background-color: #101A2A;
    border: 2px solid #3B82F6;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px
}
.st-key-total_spending_card:hover {
    background-color: #123544;
    border-color: #22D3EE;
}
.st-key-expense_count_card:hover {
    background-color: #302047;
    border-color: #C084FC;
}
.st-key-largest_expense_card:hover {
    background-color: #3B2B15;
    border-color: #FBBF24;
}
.st-key-total_spending_card:hover,
.st-key-expense_count_card:hover,
.st-key-largest_expense_card:hover {
    transform: translateY(-4px);
    transition: all 0.3s ease
}
.st-key-total_spending_card {
    border-color: #06B6D4;
}

.st-key-expense_count_card {
    border-color: #A855F7;
}

.st-key-largest_expense_card {
    border-color: #F59E0B;
}
.st-key-header_card {
    border: 2px solid #A855F7;
    margin-bottom: 15px
}
.st-key-add_expense_card {
    border: 2px solid #10D99A
}
.st-key-delete_expense_card {
    border: 2px solid #EF4444
}
.st-key-category_chart_card {
    border: 2px solid #F59E0B;
    margin-top: 20px;
    padding: 25px;
    min-height: 500px
}
.st-key-expenses_table_card {
    border: 2px solid #A855F7;
    margin-top: 15px 
}
.st-key-add_expense_card [data-testid="stHeadingIcon"] {
    color: #10D99A !important;
}
.st-key-delete_expense_card [data-testid="stHeadingIcon"] {
    color: #EF4444 !important;
}
.st-key-category_chart_card [data-testid="stHeadingIcon"] {
    color: #F59E0B !important;
}
.st-key-expenses_table_card [data-testid="stHeadingIcon"] {
    color: #A855F7 !important;
}
.st-key-monthly_budget_card [data-testid="stHeadingIcon"] {
    color: #06B6D4 !important;
}
.st-key-monthly_budget_card {
    border: 2px solid #06B6D4;
    margin-top : 15px
}
.budget-balance {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    background-color: #102B29;
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 20px
}
.budget-balance .budget-label {
    color: #94A3B8;
    font-size: 14px;
}
.budget-balance .budget-money {
    color: #10D99A;
    font-size: 24px;
    font-weight: 700;
    white-space: nowrap;
}
.st-key-monthly_budget_card [data-testid="stWidgetLabel"] p,
.st-key-add_expense_card [data-testid="stWidgetLabel"] p,
.st-key-delete_expense_card [data-testid="stWidgetLabel"] p {
    color: #CBD5E1;
    font-weight: 500;
}
.st-key-category_chart_card [data-testid="stPlotlyChart"] {
    margin-top: 25px;
}
.st-key-save_budget {
    display: flex;
    justify-content: flex-end;
    width: 100%;
    margin-top: 10px;
}
.st-key-monthly_spending_history_card {
    border: 2px solid #06B6D4;
    margin-top: 20px;
    margin-bottom: 10px;
    background-color: #111827;
}
.st-key-monthly_spending_history_card [data-testid="stHeading"] {
    margin-left: 28px;
}
</style>
""", unsafe_allow_html = True)

#[4] Header
with st.container(key = 'header_card'):
    st.markdown(
    """<h1>💎 Expense Tracker <span style="color: #10D99A;">Pro</span></h1>
    <p><span style="color: #94A3B8; margin-left: 70px">Track your expenses, analyze your spending, and stay in control!</span></p>
    """,unsafe_allow_html = True)

#[5] Loading the data
try:
    expenses = load_expenses()
except json.JSONDecodeError:
    st.error("The expense file is corrupted.")
    st.stop()

#[6] Summary data
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(key = 'total_spending_card'):
        st.markdown('<p><span style="color: #94A3B8;">Total Spending</span></p>',
            unsafe_allow_html = True)
        st.subheader(f'€{calculate_total(expenses):.2f}')

with col2:
    with st.container(key = 'expense_count_card'):
        st.markdown('<p><span style="color: #94A3B8;">Expenses</span></p>',
            unsafe_allow_html = True)
        st.subheader(len(expenses))

with col3:
    with st.container(key = 'largest_expense_card'):
        st.markdown('<p><span style="color: #94A3B8;">Largest Expense</span></p>',
            unsafe_allow_html = True)
        if expenses:
            data = find_most_expensive(expenses)
            st.subheader(f'€{data["amount"]:.2f}', help = f'Category : {data["category"]}')
        else:
            st.subheader('€0.00')
    
#[7] Add,  Delete and chart data
col4, col5 = st.columns(2)

with col4:
    with st.container(key = 'add_expense_card'):
        st.subheader('Add New Expense', icon=":material/add_circle:")
        category = st.selectbox(
            "Choose a category:",
            ["Food", "Transport", "Shopping", "Entertainment", "Other"]
        )
        amount = st.number_input('Enter expense amount (€):', min_value = 0.0, step = 0.01)
        description = st.text_input('Enter expense description:')
        if st.button('Add Expense'):
            try:
                add_expense(expenses, category, amount, description)
                save_expenses(expenses)
            except ValueError as error:
                st.error(f'Invalid expense : {error}')
            else:
                st.success('Expense added successfully!')
                st.rerun()
    with st.container(key = 'monthly_budget_card'):
        col6, col7 = st.columns([3, 1])
        with col6:
            st.subheader("Monthly Budget", icon=":material/target:")
        with col7:
            save_clicked = st.button("Save", key="save_budget")
        budget = st.number_input('Monthly budget (€)', min_value = 1.0, value = load_budget(),  step = 10.0)
        spent = calculate_monthly_total(expenses)
        if save_clicked:
            save_budget(budget)
        remaining = budget - spent
        progress = spent / budget
        left, right = st.columns(2)
        st.progress(min(progress, 1.0))
        with left:
            st.markdown(f'<p style="color: #94A3B8;">€{spent:.2f} spent</p>', unsafe_allow_html=True)
        with right:
            st.markdown(f'<p style="text-align: right; color: #94A3B8;">{progress * 100:.1f}% used</p>',
            unsafe_allow_html=True)
        if remaining >= 0:
            st.markdown(f"""<div class="budget-balance">
            <span class="budget-label">Remaining</span>
            <span class="budget-money">€{remaining:.2f}</span>
            </div>""", unsafe_allow_html=True)
        else:
            st.error(f"€{-remaining:.2f} over budget")
with col5:
    with st.container(key = 'delete_expense_card'):
        st.subheader('Delete Expense', icon=":material/delete:")
        if expenses:
            selected_index = st.selectbox(
            "Select Expense",
            range(len(expenses)),
            format_func=lambda i: f'{expenses[i]["category"]} — €{expenses[i]["amount"]:.2f}'
            )
            if st.button('Delete Expense'):
                try:
                    delete_expense(expenses, selected_index + 1)
                    save_expenses(expenses)
                except ValueError as error:
                    st.error(f'Invalid expense : {error}')
                except TypeError as error:
                    st.error(f'Invalid expense : {error}')
                else:
                    st.success('Expense deleted successfully!')
                    st.rerun()
    if expenses:
        with st.container(key = 'category_chart_card'):
            category_totals = {}
            categories = {expense["category"] for expense in expenses}
            for category in categories:
                category_totals[category] = calculate_category_total(expenses, category)
            chart_data = [
                {"Category": category, "Total": total} for category, total in category_totals.items()
            ]
            if chart_data:
                st.subheader("Spending by Category", icon=":material/bar_chart:")

                data = px.pie(
                chart_data,
                color_discrete_sequence=[
                    "#10D99A",  
                    "#A855F7",  
                    "#F59E0B",  
                    "#06B6D4",  
                    "#3B82F6",  
                    "#FB7185"    
                ],
                names="Category",
                values="Total",
                hole=0.55)

                data.update_layout(
                hoverlabel=dict(
                bgcolor="#1E293B",
                bordercolor="#475569",
                font=dict(color="white", size=14)),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                height=320,
                margin=dict(l=10, r=10, t=10, b=10),
                legend=dict(
                orientation="v",
                x=1.02,
                y=0.5,
                xanchor="left",
                yanchor="middle",
                font=dict(size=12, color="white"),
                itemsizing="constant",
                entrywidthmode="pixels",
                entrywidth=100))

                data.update_traces(
                    hovertemplate=(
                    "<b>%{label}</b><br>"
                    "€%{value:.2f}<br>"
                    "%{percent:.1%} of total spending"
                    "<extra></extra>"),
                legendgrouptitle=None,
                textposition="inside",
                textinfo="none",
                marker=dict(line=dict(color="#0B111B", width=3)))

                data.add_annotation(
                text=f'<span style="color:#94A3B8;font-size:13px;">Total spent</span><br><b>€{calculate_total(expenses):.2f}</b>',
                x=0.5,
                y=0.5,
                xref="paper",
                yref="paper",
                showarrow=False,
                align="center",
                font=dict(size=22, color="white"))

                st.plotly_chart(data, use_container_width=True)

with st.container(key = 'monthly_spending_history_card'):
    st.subheader("Monthly Spending History", icon=":material/bar_chart:")
    chart_data = calculate_spending_by_month(expenses)
    chart_data = dict(sorted(chart_data.items()))
    if chart_data:

        data = px.bar(
            x=list(chart_data.keys()),
            y=list(chart_data.values()),
            color_discrete_sequence=[  
                "#3B82F6" ],
            labels={
                "x": "Month",
                "y": "Spending (€)"},
            text_auto=".2f")

        data.update_xaxes(type="category")
        data.update_yaxes(range=[0, max(chart_data.values()) * 1.2])

        data.update_traces(width=0.65,
            textposition="outside",
            texttemplate="€%{y:.2f}",
            hovertemplate=(
                "<b>Month: %{label}</b><br>"
                "€%{value:.2f}<br>"
                "<extra></extra>"),
            marker=dict(
                color="#3B82F6",
                cornerradius = 8))

        data.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

        st.plotly_chart(data, use_container_width=True)
    else:
        st.info('No dated expenses available yet.')

with st.container(key = 'expenses_table_card'):
    st.subheader("All Expenses", icon=":material/receipt_long:")
    st.markdown('<p><span style="color: #94A3B8; margin-left: 5px">Here are all your recorded expenses</span></p>',
    unsafe_allow_html = True)
    if expenses:
        data = sorted(expenses, key=lambda expense: expense.get("date", ""), reverse = True)
        st.dataframe(
            data,
            column_config = {"date": st.column_config.TextColumn("Date"),
            "amount": st.column_config.NumberColumn("Amount (€)", format="€%.2f"),
            'category': st.column_config.TextColumn('Category'),
            'description': st.column_config.TextColumn('Description')}, 
            hide_index = True
        )
    else:
        st.info("No expenses recorded yet.")