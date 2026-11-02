import pandas as pd


def main() -> None:
    data = [
        {
            "Insurer": "Star Health",
            "Annual_Premium_INR": 18500,
            "Claim_Settlement_Ratio_Pct": 96.8,
            "Room_Rent_Limit": "Single Private Room",
            "Room_Rent_Cap_Pct": 1,
            "Co_Pay_Pct": 10,
            "Policy_Clause_Text": "Room rent is capped at 1% of sum insured per day with 10% co-pay for non-network hospitals.",
        },
        {
            "Insurer": "HDFC ERGO",
            "Annual_Premium_INR": 22300,
            "Claim_Settlement_Ratio_Pct": 98.1,
            "Room_Rent_Limit": "Any Room",
            "Room_Rent_Cap_Pct": 0,
            "Co_Pay_Pct": 0,
            "Policy_Clause_Text": "No room rent cap; daycare procedures covered up to sum insured.",
        },
        {
            "Insurer": "Niva Bupa",
            "Annual_Premium_INR": 20100,
            "Claim_Settlement_Ratio_Pct": 95.4,
            "Room_Rent_Limit": "Twin Sharing",
            "Room_Rent_Cap_Pct": 1,
            "Co_Pay_Pct": 5,
            "Policy_Clause_Text": "Twin sharing room covered with proportionate deduction if upgraded.",
        },
        {
            "Insurer": "ICICI Lombard",
            "Annual_Premium_INR": 19400,
            "Claim_Settlement_Ratio_Pct": 97.3,
            "Room_Rent_Limit": "Single Private Room",
            "Room_Rent_Cap_Pct": 1,
            "Co_Pay_Pct": 0,
            "Policy_Clause_Text": "Modern treatments covered; room rent limited to single private room.",
        },
        {
            "Insurer": "Care Health",
            "Annual_Premium_INR": 17600,
            "Claim_Settlement_Ratio_Pct": 94.9,
            "Room_Rent_Limit": "Shared Room",
            "Room_Rent_Cap_Pct": 2,
            "Co_Pay_Pct": 15,
            "Policy_Clause_Text": "2% room rent cap per day and mandatory 15% co-pay for claims above age threshold.",
        },
    ]

    df = pd.DataFrame(data)
    df.to_csv("indian_insurance_policies.csv", index=False)


if __name__ == "__main__":
    main()
