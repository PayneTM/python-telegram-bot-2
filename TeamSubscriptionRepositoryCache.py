from numbers import Number
from TeamSubscription import TeamSubscription
from TeamSubscriptionRepository import TeamSubscriptionRepository


class TeamSubscriptionRepositoryCache(TeamSubscriptionRepository):
    _tablename = "TeamSubscriptionCache"

    def __init__(self, dbname):
        super().__init__(dbname)
    
    def setup(self):
        stmt = super()._create_table_statement.format(table_name = self._tablename, params = "userId bigint, teamName text")
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item : TeamSubscription):
        stmt = super()._add_item_statement.format(table_name = self._tablename, values = "?, ?")
        args = (item.user_id, item.team_name, )
        self.conn.execute(stmt, args)
        self.conn.commit()
        return item

    def delete_item(self, user_id : Number):
        stmt = super()._delete_item_statement.format(table_name = self._tablename, condition = "userId = (?)")
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self, user_id: Number):
        stmt = super()._get_all_items_statement.format(values = "userId, teamName", table_name = self._tablename, condition = "userId = (?)")
        args = (user_id, )
        return [x for x in self.conn.execute(stmt, args)]