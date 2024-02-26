import pandas as pd

# df = pd.DataFrame(columns=[
#     'orgName',
#     'shortOrgName',
#     'userType',
#     'bossPost',
#     'bossName',
#     'responsiblePost',
#     'responsibleName',
#     'tel',
#     'mail',
#     'date-time'])
#
# df.to_csv('offer.csv', index=False, header=True)
print(pd.read_csv('offer.csv'))