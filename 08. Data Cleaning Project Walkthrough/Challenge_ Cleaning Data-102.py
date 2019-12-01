## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

true_avengers = avengers.loc[avengers['Year'] > 1960]

true_avengers['Year'].hist()

## 5. Consolidating Deaths ##

true_avengers['Deaths'] = (true_avengers[['Death1', 'Death2', 'Death3', 'Death4', 'Death5']] == 'YES').sum(axis=1)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()

REFERENCE_YEAR = 2015
joined_accuracy_count = (true_avengers['Years since joining'] == (REFERENCE_YEAR - true_avengers['Year'])).sum(axis=0)