from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table import DataTypes
from pyflink.table.udf import udf
import pandas as pd

# 通过 batch table environment 来执行查询
env_settings = EnvironmentSettings.in_batch_mode()
table_env = TableEnvironment.create(env_settings)

orders = table_env.from_elements([('Jack', 'FRANCE', 10), ('Rose', 'ENGLAND', 30), ('Jack', 'FRANCE', 20)],
                                 ['name', 'country', 'revenue'])

map_function = udf(lambda x: pd.concat([x.name, x.revenue * 10], axis=1),
                    result_type=DataTypes.ROW(
                                [DataTypes.FIELD("name", DataTypes.STRING()),
                                 DataTypes.FIELD("revenue", DataTypes.BIGINT())]),
                    func_type="pandas")

orders.map(map_function).alias('name', 'revenue').to_pandas()