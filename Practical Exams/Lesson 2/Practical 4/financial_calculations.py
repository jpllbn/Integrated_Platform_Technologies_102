def compound_interest(P, AnInt, CompYr, NumOfYrsInvsted):
    amount = P * NumOfYrsInvsted * (1 + AnInt / CompYr)
    return amount