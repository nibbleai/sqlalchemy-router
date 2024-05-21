import random
import shutil

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

__all__ = ['RoutingSession', 'engines']

master_engine = create_engine(
    'sqlite:///master.db', echo=True, logging_name='master'
)
slave_engine_1 = create_engine(
    'sqlite:///replica_1.db', echo=True, logging_name='replica_1'
)
slave_engine_2 = create_engine(
    'sqlite:///replica_2.db', echo=True, logging_name='replica_2'
)

engines = {
    'master': master_engine,
    'slave_1': slave_engine_1,
    'slave_2': slave_engine_2,
}


class RoutingSession(Session):

    master = 'master'
    replicas = ('slave_1', 'slave_2')

    def get_bind(self, mapper=None, **kwargs):
        if self._flushing:
            # attempting to write: route to the master db
            return engines[self.master]
        # route to any of the read-replicas
        fake_auto_replication()
        return engines[random.choice(self.replicas)]


def fake_auto_replication():  # In the real-world, RDS would do that for us!
    for replica in ('replica_1', 'replica_2'):
        shutil.copy('master.db', f'{replica}.db')
