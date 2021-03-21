from partner import Partner
from create_partner import CreatePartner


p = CreatePartner()
partner = Partner.from_dict({
        'owner_name': 'MnR',
        'tranding_name': 'MnR',
        'document': 0,
        'address': [16, 16]
        })

print(' '.join([str(point) for point in partner.address]))
result = p.set_data(partner)
print(result)

