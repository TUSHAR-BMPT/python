"""
Enter the amount of the study benefits: 335.32
If the index raise is 1.17 percent, the study benefit,
after a raise, would be 339.243244 euros
and if there was another index raise, the study
benefits would be as much as 343.2123899548 euros
"""
study_benefits=float(input("Enter the amount of the study benefits: "))
index_rise=study_benefits*(1.17/100)
new_study_benefit= study_benefits+index_rise
print(f"If the index raise is 1.17 percent, the study benefit,\nafter a raise, would be {new_study_benefit} euros")
another_index_rise=new_study_benefit*(1.17/100)
another_new_study_benefit= new_study_benefit+another_index_rise
print(f"and if there was another index raise, the study\nbenefits would be as much as {another_new_study_benefit} euros")
