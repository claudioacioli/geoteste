from databasemanager import DatabaseManager
from result import Result


class CreatePartner(DatabaseManager):


    def __init__(self, conn=None, closeFlag=True):
       super().__init__(conn, closeFlag)
       self._open()


    def _create(self, partner):
        cursor = self._conn.cursor()
        dml = """
        insert into partner 
        (tranding_name, owner_name, document, address, coverage_area)
        values
        (%s, %s, %s, ST_GeomFromGeoJSON(%s), ST_GeomFromGeoJSON(%s))
        returning id;
        """
#        print(dml % (partner.tradingName, 
#            partner.ownerName, 
#            partner.document,
#            partner.address))

#        return 0
        cursor.execute(dml, (
            partner.tradingName, 
            partner.ownerName, 
            partner.document,
            partner.address,
            partner.coverageArea))

        id = cursor.fetchone()[0]
        cursor.close()
        return id


    def set_data(self, args):
        id = 0
        id = self._create(args)
        if self._closeFlag:
            self._close()
        return Result(data=id)

