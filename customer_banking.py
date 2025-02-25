# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account 
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the balance of the savings account: "))
    savings_interest = float(input("Enter the annual interest rate (in %): "))
    savings_maturity = int(input("Enter the number of months you wish to save: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned_savings = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Interest earned on the savings account: ${interest_earned_savings:,.2f}")
    print(f"Updated savings account balance: ${updated_savings_balance:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    CD_balance = float(input("Enter the balance for the CD: "))
    CD_interest = float(input("Enter the annual interest rate for the CD account (in %): " ))
    CD_term = int(input("Enter the number of months for the CD: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned_cd = create_cd_account(CD_balance, CD_interest, CD_term)
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Interest earned on the CD account: ${interest_earned_cd:,.2f}")
    print(f"Updated CD account balance: ${updated_cd_balance:,.2f}")

if __name__ == "__main__":
    main()