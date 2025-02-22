import streamlit as st
import pandas as pd
import numpy as np

def calculate_tax_2024(yearly_income, tax_class, is_single=False):
    """
    Calculate German income tax for 2024
    This is a simplified calculation and may not include all factors
    """
    # Basic tax-free amount for 2024
    basic_tax_free = 11604
    
    # Tax class factors (simplified)
    class_factors = {
        1: 1.0,  # Single
        3: 1.2,  # More favorable for higher earner
        4: 1.0,  # Standard
        5: 0.8,  # Less favorable for lower earner
    }
    
    # Use tax class 1 if single, otherwise use specified class
    factor = class_factors[1] if is_single else class_factors.get(tax_class, 1.0)
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
    st.title("German Marriage ❤️ Tax Calculator 2024")
    st.write("""
    Compare tax calculations for married couples using different tax class combinations,
    and see how it compares to being single. This is a simplified calculation and
    should not be used as official tax advice.
    """)
    
    # Input for first person
    st.subheader("Person 1 Income Details")
    income_1 = st.number_input("Yearly Income (€) - Person 1", min_value=0.0, value=50000.0, step=1000.0)
    
    # Input for second person
    st.subheader("Person 2 Income Details")
    income_2 = st.number_input("Yearly Income (€) - Person 2", min_value=0.0, value=40000.0, step=1000.0)
    
    # Calculate taxes for all scenarios
    if st.button("Calculate Taxes"):
        # Option A: Tax Class 3/5
        tax_3 = calculate_tax_2024(income_1, 3)
        tax_5 = calculate_tax_2024(income_2, 5)
        total_tax_option_a = tax_3 + tax_5
        
        # Option B: Both Tax Class 4
        tax_4_1 = calculate_tax_2024(income_1, 4)
        tax_4_2 = calculate_tax_2024(income_2, 4)
        total_tax_option_b = tax_4_1 + tax_4_2
        
        # Option C: Both Single (Tax Class 1)
        tax_single_1 = calculate_tax_2024(income_1, 1, is_single=True)
        tax_single_2 = calculate_tax_2024(income_2, 1, is_single=True)
        total_tax_option_c = tax_single_1 + tax_single_2
        
        # Display results
        st.header("Tax Comparison")
        
        col1, col2, col3 = st.columns(3)
        
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
            
        with col3:
            st.subheader("Option C: Both Single")
            st.write(f"Person 1 (Single) Tax: €{tax_single_1:,.2f}")
            st.write(f"Person 2 (Single) Tax: €{tax_single_2:,.2f}")
            st.write(f"Total Tax: €{total_tax_option_c:,.2f}")
        
        # Calculate savings compared to single status
        savings_a = total_tax_option_c - total_tax_option_a
        savings_b = total_tax_option_c - total_tax_option_b
        
        # Find best option
        tax_options = {
            "A (3/5)": total_tax_option_a,
            "B (4/4)": total_tax_option_b,
            "C (Single)": total_tax_option_c
        }
        best_option = min(tax_options.items(), key=lambda x: x[1])
        
        st.header("Summary")
        st.write(f"Option {best_option[0]} results in the lowest total tax (€{best_option[1]:,.2f})")
        
        # Marriage savings analysis
        st.subheader("Marriage Tax Benefit Analysis")
        st.write(f"Tax savings with Option A (3/5) vs Single: €{savings_a:,.2f}")
        st.write(f"Tax savings with Option B (4/4) vs Single: €{savings_b:,.2f}")
        
        # Display warning
        st.warning("""
        Please note: This is a simplified calculation and does not include all factors that might affect your tax liability. 
        Consult with a tax professional for accurate calculations and advice.
        """)

if __name__ == "__main__":
    main()
