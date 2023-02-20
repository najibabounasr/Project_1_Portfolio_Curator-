# -*- coding: utf-8 -*-
"""Portfolio Currator.

This is a command line application to create an optimal portfolio, based on their current medical insurance and personal information, aswell as the stock data pulled in and analyzed via. the API.

Example:
    $ python app.py
"""
import sys
import fire
import questionary
from pathlib import Path
# from modules.questions import get_applicant_info
import pandas as pd
     
    # 1. Create a function to recieve the applicant information :
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

# NOTE : The below variable 'md_average_roc' is the annual mean pct_change in medical insurance charges, based on the dataset we analyzed in the notebook. 
md_average_roc = 7.05805500745121


# 2. Create a function to create a portfolio, based on the risk assesment (unweighted) :
# def create_unweighted_portfolio(md_charges, age, initial_investment, risk_tolerance):
def create_unweighted_portfolio(risk_tolerance):
    """Determine which loans the user qualifies for.

    Portfolio Creation criteria is based on:
        - Medical Insurance Costs
        - Age
        - Initial Investment
        - Risk tolerance
        - The API data (imported)
        """ 
    # 1. Pull in variables
    # 2. Import the 'top performing' .csv
    
    top_std_df = pd.read_csv(
        Path('./Resources/top_std.csv')
    )
    top_std_df.columns =['stocks', 'prices']
    top_std = top_std_df
    
    
    top_annual_return_df = pd.read_csv(
        Path('./Resources/top_annual_returns.csv')
    )
    top_annual_return_df.columns =['stocks', 'prices']
    top_annual_return = top_annual_return_df
    
    top_sharpe_ratio_df = pd.read_csv(
       Path('./Resources/top_sharpe_ratios.csv')
    )
    top_sharpe_ratio_df.columns =['stocks', 'prices']
    top_sharpe_ratio = top_sharpe_ratio_df
    
    # 3. create empty dataframe:
    portfolio = pd.DataFrame()
    # 4. Create Portfolio
     portfolio = pd.DataFrame()
    
    if risk_assesment == str("Low Risk"):
        portfolio = list(top_std[0:5].keys()) + list(top_sharpe_ratio[5:10].keys())
        print(portfolio)
    elif risk_assesment == str("Medium Risk"):
        portfolio = list(top_sharpe_ratio.keys())
        print(portfolio)
    elif risk_assesment == str("High Risk"):
        portfolio = list(top_sharpe_ratio[5:10].keys()) + list(top_annual_return[5:10].keys())
        print(portfolio)
    elif risk_assesment == str("Ultra-High Risk"):
        portfolio = list(top_annual_return.keys())
        print(portfolio)

        
      
    print(portfolio['stocks'])
    
    "Low Risk", "Medium Risk", "High Risk", "Ultra-High Risk"
"""
    Args:
        md_charges (float): The users current annual medical insurance costs.
        age (int): The users current age
        initial_investment (float): The users initial investment in our portfolio offering.
        risk_tolerance (str): The applicant's self-assesed risk tolerance. 
        top_std (list): The top ten least volatile stocks out of the pool of 50.
        top_sharpe_ratio (list): : The top ten stocks of the pool of 50, based on their balance between potential risk and return.
        top_annual_return (list): The stocks with the best annual return

    Returns:
        Creates a portfolio based on the users risk assesment, and logs the user MD insurance info aswell."""

    
    
def run():
    """The main function for running the script."""


    # Get the applicant's information
    md_charges, age, initial_investment, risk_tolerance = get_applicant_info()

    # Find qualifying loans
    portfolio = create_unweighted_portfolio(
        md_charges, age, initial_investment, risk_tolerance
    )
    
    

if __name__ == "__main__":
    fire.Fire(run)


   
