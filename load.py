from partner import Partner
from create_partner import CreatePartner
import json


def get_content(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    return None


def to_partner(partner):
    id = partner['id']
    tradingName = partner['tradingName']
    ownerName = partner['ownerName']
    document = partner['document']
    address = json.dumps(partner['address'])
    coverageArea = json.dumps(partner['coverageArea'])

    return Partner(
            id=id,
            tradingName=tradingName,
            ownerName=ownerName,
            document=document,
            address=address,
            coverageArea=coverageArea
            )


def load_partners(data):
    partners = []
    for partner in data:
        partners.append(to_partner(partner))
    return partners


def create(partners):
    dao = CreatePartner(closeFlag=False)
    for partner in partners:
        dao.set_data(partner)
    dao.commit()
    dao.close()


def main():
    filename = 'data.json'
    content = get_content(filename)
    if content is not None:
        partners = content['pdvs']
        partners = load_partners(partners)
        create(partners)


if __name__ == '__main__':
    main()
