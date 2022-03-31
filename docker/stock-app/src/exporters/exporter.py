from exporters.sqlite_base import SqliteBase
from model.models import IncomeStatementHistory, BalanceSheetHistory, CashflowStatementHistory
from model.models import IncomeStatementHistoryQuarterly, BalanceSheetHistoryQuarterly, CashflowStatementHistoryQuarterly
from model.models import FinData

def model_factory(schema, type):

    schema_map = {
        ('incomeStatementHistory', 'anual'): IncomeStatementHistory,
        ('cashflowStatementHistory', 'anual'): CashflowStatementHistory,
        ('balanceSheetHistory', 'anual'): BalanceSheetHistory,
        ('incomeStatementHistoryQuarterly', 'quarterly'): IncomeStatementHistoryQuarterly,
        ('balanceSheetHistoryQuarterly', 'quarterly'): BalanceSheetHistoryQuarterly,
        ('cashflowStatementHistoryQuarterly', 'quarterly'): CashflowStatementHistoryQuarterly,
        ('fin_data', 'fin_data'): FinData
    }

    if (schema, type) in schema_map:
        return schema_map[(schema, type)]
    else:
        return False


class SqliteExporter:

    def __init__(self, db, stock, schema, mode, date, data) -> None:
        self.db = db
        self.ticker = stock
        self.date = date
        self.data = data
        self.schema = schema
        self.mode = mode

    def export(self):

        with SqliteBase(self.db) as session:

            cls_ = model_factory(self.schema, self.mode)

            if cls_:
                report = cls_(self.date, self.ticker, self.data)
                session.merge(report)
