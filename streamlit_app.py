import streamlit as st
import pandas as pd
import numpy as np

def calculate_tax_2024(yearly_income, tax_class):
    """
    Calculate German income tax for 2024
    This is a simplified calculation and may not include all factors
    """
    # Basic tax-free amount for 2024
    basic_tax_free = 11604
    
    # Tax class factors (simplified)
    class_factors = {
        3: 1.2,  # More favorable for higher earner
        4: 1.0,  # Standard
        5: 0.8,  # Less favorable for lower earner
    }
    
    # Apply tax class factor
    factor = class_factors.get(tax_class, 1.0)
    taxable_income = max(0, yearly_income - basic_tax_free)
    
    # Progressive tax calculation (2024 rates)
    if taxable_income <= 0:
        return 0
    elif taxable_income <= 15999:
        tax_rate = 0.14
    elif taxable_income <= 62809:
        tax_rate = 0.24
    elif taxable_income <= 277825:
        tax_rate = 0.42
    else:
        tax_rate = 0.45
    
    # Apply tax class factor to final tax
    return taxable_income * tax_rate * factor

def main():
    st.title("German Marriage ♥️ Tax Calculator 2024")
    st.write("""
    Compare tax calculations for married couples using different tax class combinations.
    This is a simplified calculation and should not be used as official tax advice.
    """)
    
    # Input for first person
    st.subheader("Person 1 Income Details")
    income_1 = st.number_input("Yearly Income (€) - Person 1", min_value=0.0, value=50000.0, step=1000.0)
    
    # Input for second person
    st.subheader("Person 2 Income Details")
    income_2 = st.number_input("Yearly Income (€) - Person 2", min_value=0.0, value=40000.0, step=1000.0)
    
    # Calculate taxes for both scenarios
    if st.button("Calculate Taxes"):
        # Option A: Tax Class 3/5
        tax_3 = calculate_tax_2024(income_1, 3)
        tax_5 = calculate_tax_2024(income_2, 5)
        total_tax_option_a = tax_3 + tax_5
        
        # Option B: Both Tax Class 4
        tax_4_1 = calculate_tax_2024(income_1, 4)
        tax_4_2 = calculate_tax_2024(income_2, 4)
        total_tax_option_b = tax_4_1 + tax_4_2
        
        # Display results
        st.header("Tax Comparison")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Option A: Class 3/5")
            st.write(f"Person 1 (Class 3) Tax: €{tax_3:,.2f}")
            st.write(f"Person 2 (Class 5) Tax: €{tax_5:,.2f}")
            st.write(f"Total Tax: €{total_tax_option_a:,.2f}")
        
        with col2:
            st.subheader("Option B: Both Class 4")
            st.write(f"Person 1 (Class 4) Tax: €{tax_4_1:,.2f}")
            st.write(f"Person 2 (Class 4) Tax: €{tax_4_2:,.2f}")
            st.write(f"Total Tax: €{total_tax_option_b:,.2f}")
        
        # Show difference
        difference = abs(total_tax_option_a - total_tax_option_b)
        better_option = "A (3/5)" if total_tax_option_a < total_tax_option_b else "B (4/4)"
        
        st.header("Summary")
        st.write(f"The difference between options is €{difference:,.2f}")
        st.write(f"Option {better_option} results in lower total tax")
        
        # Display warning
        st.warning("""
        Please note: This is a simplified calculation and does not include all factors that might affect your tax liability. 
        Consult with a tax professional for accurate calculations and advice.
        """)

if __name__ == "__main__":
    main()
