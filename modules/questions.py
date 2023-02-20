 
def get_applicant_info():
    """Prompt dialog to get the applicant's MD insurance information.

    Returns:
        Returns the applicant's MD insurance information.
    """

    md_charges = questionary.text("What are your annual medical insurance costs?").ask()
    age = questionary.text("What's your current age?").ask()
    initial_investment = questionary.text("How much will your initial investment in our financial product (the portfolio) be?").ask()
    risk_tolerance = questionary.select("In general, what is your risk-tolerance ? (your answer will affect the portfolio selection, so please answer carefully. Also note that with greater risk, comes greater potential returns)", 
        choices=["Low Risk", "Medium Risk", "High Risk", "Ultra-High Risk"],
).ask()

    md_charges = float(md_charges)
    age = int(age)
    initial_investment = float(initial_investment)
    risk_tolerance = str(risk_tolerance)

    return md_charges, age, initial_investment, risk_tolerance

def create_portfolio(bank_data, md_charges, age, initial_investment, risk_tolerance, top_std, top_sharpe_ratio, top_annual_return):
    """Determine which loans the user qualifies for.

    Portfolio Creation criteria is based on:
        - Medical Insurance Costs
        - Age
        - Initial Investment
        - Risk tolerance
        - The API data (imported)

    Args:
        md_charges (float): The users current annual medical insurance costs.
        age (int): The users current age
        initial_investment (float): The users initial investment in our portfolio offering.
        risk_tolerance (str): The applicant's self-assesed risk tolerance. 
        top_std (list): The top ten least volatile stocks out of the pool of 50.
        top_sharpe_ratio (list): : The top ten stocks of the pool of 50, based on their balance between potential risk and return.
        top_annual_return (list): The stocks with the best annual return

    Returns:
        Creates a portfolio based on the users risk assesment, and logs the user MD insurance info aswell.

#     """
#     {float(md_cost_age_df_mean.tail(1)* 100)}
    
    
