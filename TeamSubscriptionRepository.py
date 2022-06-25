from numbers import Number
from typing import Sequence

from Repository import Repository
from TeamSubscription import TeamSubscription

class TeamSubscriptionRepository(Repository):
    _tablename = "TeamSubscriptions"

    def __init__(self, dbname):
        super().__init__(dbname)
    
    def setup(self):
        stmt = super()._create_table_statement.format(table_name = self._tablename, params = "userId bigint, teamName text")
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, items : Sequence[TeamSubscription]):
        stmt = super()._add_item_statement.format(table_name = self._tablename, values = "?, ?")
        self.conn.executemany(stmt, items)
        self.conn.commit()
        return items

    def delete_item(self, user_id: Number):
        stmt = super()._delete_item_statement.format(table_name = self._tablename, condition = "userId = (?)")
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self, user_id: Number):
        stmt = super()._get_all_items_statement.format(values = "userId, teamName", table_name = self._tablename, condition = "userId = (?)")
        args = (user_id, )
        return [x for x in self.conn.execute(stmt, args)]