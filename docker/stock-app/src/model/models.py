
from datetime import datetime

import sqlalchemy

from exporters.sqlite_base import SqliteBase


def formate_date(date):

    return datetime.strptime(date, '%Y-%m-%d')


class CashflowStatementHistory(SqliteBase.Base):

    __tablename__ = "cashflowStatementHistory"

    date = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    ticker = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    sql_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)

    investments = sqlalchemy.Column(sqlalchemy.BIGINT)
    changeToLiabilities = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCashflowsFromInvestingActivities = sqlalchemy.Column(
        sqlalchemy.BIGINT)
    netBorrowings = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCashFromFinancingActivities = sqlalchemy.Column(sqlalchemy.BIGINT)
    changeToOperatingActivities = sqlalchemy.Column(sqlalchemy.BIGINT)
    issuanceOfStock = sqlalchemy.Column(sqlalchemy.BIGINT)
    netIncome = sqlalchemy.Column(sqlalchemy.BIGINT)
    changeInCash = sqlalchemy.Column(sqlalchemy.BIGINT)
    repurchaseOfStock = sqlalchemy.Column(sqlalchemy.BIGINT)
    effectOfExchangeRate = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCashFromOperatingActivities = sqlalchemy.Column(sqlalchemy.BIGINT)
    depreciation = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherCashflowsFromInvestingActivities = sqlalchemy.Column(
        sqlalchemy.BIGINT)
    dividendsPaid = sqlalchemy.Column(sqlalchemy.BIGINT)
    changeToInventory = sqlalchemy.Column(sqlalchemy.BIGINT)
    changeToAccountReceivables = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherCashflowsFromFinancingActivities = sqlalchemy.Column(
        sqlalchemy.BIGINT)
    changeToNetincome = sqlalchemy.Column(sqlalchemy.BIGINT)
    capitalExpenditures = sqlalchemy.Column(sqlalchemy.BIGINT)

    def __init__(self, date, ticker, report) -> None:
        self.date = date
        self.ticker = ticker
        self.sql_date = formate_date(date)
        self.investments = report.get('investments', None)
        self.changeToLiabilities = report.get('changeToLiabilities', None)
        self.totalCashflowsFromInvestingActivities = report.get(
            'totalCashflowsFromInvestingActivities', None)
        self.netBorrowings = report.get('netBorrowings', None)
        self.totalCashFromFinancingActivities = report.get(
            'totalCashFromFinancingActivities', None)
        self.changeToOperatingActivities = report.get(
            'changeToOperatingActivities', None)
        self.issuanceOfStock = report.get('issuanceOfStock', None)
        self.netIncome = report.get('netIncome', None)
        self.changeInCash = report.get('changeInCash', None)
        self.repurchaseOfStock = report.get('repurchaseOfStock', None)
        self.effectOfExchangeRate = report.get('effectOfExchangeRate', None)
        self.totalCashFromOperatingActivities = report.get(
            'totalCashFromOperatingActivities', None)
        self.depreciation = report.get('depreciation', None)
        self.otherCashflowsFromInvestingActivities = report.get(
            'otherCashflowsFromInvestingActivities', None)
        self.dividendsPaid = report.get('dividendsPaid', None)
        self.changeToInventory = report.get('changeToInventory', None)
        self.changeToAccountReceivables = report.get(
            'changeToAccountReceivables', None)
        self.otherCashflowsFromFinancingActivities = report.get(
            'otherCashflowsFromFinancingActivities', None)
        self.changeToNetincome = report.get('changeToNetincome', None)
        self.capitalExpenditures = report.get('capitalExpenditures', None)


class BalanceSheetHistory(SqliteBase.Base):

    __tablename__ = "balanceSheetHistory"

    date = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    ticker = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    sql_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)

    intangibleAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalLiab = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalStockholderEquity = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherCurrentLiab = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    commonStock = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherCurrentAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    retainedEarnings = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherLiab = sqlalchemy.Column(sqlalchemy.BIGINT)
    goodWill = sqlalchemy.Column(sqlalchemy.BIGINT)
    treasuryStock = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    cash = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCurrentLiabilities = sqlalchemy.Column(sqlalchemy.BIGINT)
    deferredLongTermAssetCharges = sqlalchemy.Column(sqlalchemy.BIGINT)
    shortLongTermDebt = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherStockholderEquity = sqlalchemy.Column(sqlalchemy.BIGINT)
    propertyPlantEquipment = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCurrentAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    longTermInvestments = sqlalchemy.Column(sqlalchemy.BIGINT)
    netTangibleAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    shortTermInvestments = sqlalchemy.Column(sqlalchemy.BIGINT)
    netReceivables = sqlalchemy.Column(sqlalchemy.BIGINT)
    longTermDebt = sqlalchemy.Column(sqlalchemy.BIGINT)
    inventory = sqlalchemy.Column(sqlalchemy.BIGINT)
    accountsPayable = sqlalchemy.Column(sqlalchemy.BIGINT)

    def __init__(self, date, ticker, report) -> None:
        self.date = date
        self.ticker = ticker
        self.sql_date = formate_date(date)
        self.intangibleAssets = report.get('intangibleAssets', None)
        self.totalLiab = report.get('totalLiab', None)
        self.totalStockholderEquity = report.get(
            'totalStockholderEquity', None)
        self.otherCurrentLiab = report.get('otherCurrentLiab', None)
        self.totalAssets = report.get('totalAssets', None)
        self.commonStock = report.get('commonStock', None)
        self.otherCurrentAssets = report.get('otherCurrentAssets', None)
        self.retainedEarnings = report.get('retainedEarnings', None)
        self.otherLiab = report.get('otherLiab', None)
        self.goodWill = report.get('goodWill', None)
        self.treasuryStock = report.get('treasuryStock', None)
        self.otherAssets = report.get('otherAssets', None)
        self.cash = report.get('cash', None)
        self.totalCurrentLiabilities = report.get(
            'totalCurrentLiabilities', None)
        self.deferredLongTermAssetCharges = report.get(
            'deferredLongTermAssetCharges', None)
        self.shortLongTermDebt = report.get('shortLongTermDebt', None)
        self.otherStockholderEquity = report.get(
            'otherStockholderEquity', None)
        self.propertyPlantEquipment = report.get(
            'propertyPlantEquipment', None)
        self.totalCurrentAssets = report.get('totalCurrentAssets', None)
        self.longTermInvestments = report.get('longTermInvestments', None)
        self.netTangibleAssets = report.get('netTangibleAssets', None)
        self.shortTermInvestments = report.get('shortTermInvestments', None)
        self.netReceivables = report.get('netReceivables', None)
        self.longTermDebt = report.get('longTermDebt', None)
        self.inventory = report.get('inventory', None)
        self.accountsPayable = report.get('accountsPayable', None)


class IncomeStatementHistory(SqliteBase.Base):

    __tablename__ = "incomeStatementHistory"

    date = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    ticker = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    sql_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    researchDevelopment = sqlalchemy.Column(sqlalchemy.BIGINT)
    effectOfAccountingCharges = sqlalchemy.Column(sqlalchemy.BIGINT)
    incomeBeforeTax = sqlalchemy.Column(sqlalchemy.BIGINT)
    minorityInterest = sqlalchemy.Column(sqlalchemy.BIGINT)
    netIncome = sqlalchemy.Column(sqlalchemy.BIGINT)
    sellingGeneralAdministrative = sqlalchemy.Column(sqlalchemy.BIGINT)
    grossProfit = sqlalchemy.Column(sqlalchemy.BIGINT)
    ebit = sqlalchemy.Column(sqlalchemy.BIGINT)
    operatingIncome = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherOperatingExpenses = sqlalchemy.Column(sqlalchemy.BIGINT)
    interestExpense = sqlalchemy.Column(sqlalchemy.BIGINT)
    extraordinaryItems = sqlalchemy.Column(sqlalchemy.BIGINT)
    nonRecurring = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherItems = sqlalchemy.Column(sqlalchemy.BIGINT)
    incomeTaxExpense = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalRevenue = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalOperatingExpenses = sqlalchemy.Column(sqlalchemy.BIGINT)
    costOfRevenue = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalOtherIncomeExpenseNet = sqlalchemy.Column(sqlalchemy.BIGINT)
    discontinuedOperations = sqlalchemy.Column(sqlalchemy.BIGINT)
    netIncomeFromContinuingOps = sqlalchemy.Column(sqlalchemy.BIGINT)
    netIncomeApplicableToCommonShares = sqlalchemy.Column(sqlalchemy.BIGINT)

    def __init__(self, date, ticker, report) -> None:
        self.date = date
        self.ticker = ticker
        self.sql_date = formate_date(date)
        self.researchDevelopment = report.get('researchDevelopment', None)
        self.effectOfAccountingCharges = report.get(
            'effectOfAccountingCharges', None)
        self.incomeBeforeTax = report.get('incomeBeforeTax', None)
        self.minorityInterest = report.get('minorityInterest', None)
        self.netIncome = report.get('netIncome', None)
        self.sellingGeneralAdministrative = report.get(
            'sellingGeneralAdministrative', None)
        self.grossProfit = report.get('grossProfit', None)
        self.ebit = report.get('ebit', None)
        self.operatingIncome = report.get('operatingIncome', None)
        self.otherOperatingExpenses = report.get(
            'otherOperatingExpenses', None)
        self.interestExpense = report.get('interestExpense', None)
        self.extraordinaryItems = report.get('extraordinaryItems', None)
        self.nonRecurring = report.get('nonRecurring', None)
        self.otherItems = report.get('otherItems', None)
        self.incomeTaxExpense = report.get('incomeTaxExpense', None)
        self.totalRevenue = report.get('totalRevenue', None)
        self.totalOperatingExpenses = report.get(
            'totalOperatingExpenses', None)
        self.costOfRevenue = report.get('costOfRevenue', None)
        self.totalOtherIncomeExpenseNet = report.get(
            'totalOtherIncomeExpenseNet', None)
        self.discontinuedOperations = report.get(
            'discontinuedOperations', None)
        self.netIncomeFromContinuingOps = report.get(
            'netIncomeFromContinuingOps', None)
        self.netIncomeApplicableToCommonShares = report.get(
            'netIncomeApplicableToCommonShares', None)


class CashflowStatementHistoryQuarterly(SqliteBase.Base):

    __tablename__ = "cashflowStatementHistoryQuarterly"

    date = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    ticker = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    sql_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)

    investments = sqlalchemy.Column(sqlalchemy.BIGINT)
    changeToLiabilities = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCashflowsFromInvestingActivities = sqlalchemy.Column(
        sqlalchemy.BIGINT)
    netBorrowings = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCashFromFinancingActivities = sqlalchemy.Column(sqlalchemy.BIGINT)
    changeToOperatingActivities = sqlalchemy.Column(sqlalchemy.BIGINT)
    issuanceOfStock = sqlalchemy.Column(sqlalchemy.BIGINT)
    netIncome = sqlalchemy.Column(sqlalchemy.BIGINT)
    changeInCash = sqlalchemy.Column(sqlalchemy.BIGINT)
    repurchaseOfStock = sqlalchemy.Column(sqlalchemy.BIGINT)
    effectOfExchangeRate = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCashFromOperatingActivities = sqlalchemy.Column(sqlalchemy.BIGINT)
    depreciation = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherCashflowsFromInvestingActivities = sqlalchemy.Column(
        sqlalchemy.BIGINT)
    dividendsPaid = sqlalchemy.Column(sqlalchemy.BIGINT)
    changeToInventory = sqlalchemy.Column(sqlalchemy.BIGINT)
    changeToAccountReceivables = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherCashflowsFromFinancingActivities = sqlalchemy.Column(
        sqlalchemy.BIGINT)
    changeToNetincome = sqlalchemy.Column(sqlalchemy.BIGINT)
    capitalExpenditures = sqlalchemy.Column(sqlalchemy.BIGINT)

    def __init__(self, date, ticker, report) -> None:
        self.date = date
        self.ticker = ticker
        self.sql_date = formate_date(date)
        self.investments = report.get('investments', None)
        self.changeToLiabilities = report.get('changeToLiabilities', None)
        self.totalCashflowsFromInvestingActivities = report.get(
            'totalCashflowsFromInvestingActivities', None)
        self.netBorrowings = report.get('netBorrowings', None)
        self.totalCashFromFinancingActivities = report.get(
            'totalCashFromFinancingActivities', None)
        self.changeToOperatingActivities = report.get(
            'changeToOperatingActivities', None)
        self.issuanceOfStock = report.get('issuanceOfStock', None)
        self.netIncome = report.get('netIncome', None)
        self.changeInCash = report.get('changeInCash', None)
        self.repurchaseOfStock = report.get('repurchaseOfStock', None)
        self.effectOfExchangeRate = report.get('effectOfExchangeRate', None)
        self.totalCashFromOperatingActivities = report.get(
            'totalCashFromOperatingActivities', None)
        self.depreciation = report.get('depreciation', None)
        self.otherCashflowsFromInvestingActivities = report.get(
            'otherCashflowsFromInvestingActivities', None)
        self.dividendsPaid = report.get('dividendsPaid', None)
        self.changeToInventory = report.get('changeToInventory', None)
        self.changeToAccountReceivables = report.get(
            'changeToAccountReceivables', None)
        self.otherCashflowsFromFinancingActivities = report.get(
            'otherCashflowsFromFinancingActivities', None)
        self.changeToNetincome = report.get('changeToNetincome', None)
        self.capitalExpenditures = report.get('capitalExpenditures', None)


class BalanceSheetHistoryQuarterly(SqliteBase.Base):

    __tablename__ = "balanceSheetHistoryQuarterly"

    date = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    ticker = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    sql_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)

    intangibleAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalLiab = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalStockholderEquity = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherCurrentLiab = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    commonStock = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherCurrentAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    retainedEarnings = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherLiab = sqlalchemy.Column(sqlalchemy.BIGINT)
    goodWill = sqlalchemy.Column(sqlalchemy.BIGINT)
    treasuryStock = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    cash = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCurrentLiabilities = sqlalchemy.Column(sqlalchemy.BIGINT)
    deferredLongTermAssetCharges = sqlalchemy.Column(sqlalchemy.BIGINT)
    shortLongTermDebt = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherStockholderEquity = sqlalchemy.Column(sqlalchemy.BIGINT)
    propertyPlantEquipment = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCurrentAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    longTermInvestments = sqlalchemy.Column(sqlalchemy.BIGINT)
    netTangibleAssets = sqlalchemy.Column(sqlalchemy.BIGINT)
    shortTermInvestments = sqlalchemy.Column(sqlalchemy.BIGINT)
    netReceivables = sqlalchemy.Column(sqlalchemy.BIGINT)
    longTermDebt = sqlalchemy.Column(sqlalchemy.BIGINT)
    inventory = sqlalchemy.Column(sqlalchemy.BIGINT)
    accountsPayable = sqlalchemy.Column(sqlalchemy.BIGINT)

    def __init__(self, date, ticker, report) -> None:
        self.date = date
        self.ticker = ticker
        self.sql_date = formate_date(date)
        self.intangibleAssets = report.get('intangibleAssets', None)
        self.totalLiab = report.get('totalLiab', None)
        self.totalStockholderEquity = report.get(
            'totalStockholderEquity', None)
        self.otherCurrentLiab = report.get('otherCurrentLiab', None)
        self.totalAssets = report.get('totalAssets', None)
        self.commonStock = report.get('commonStock', None)
        self.otherCurrentAssets = report.get('otherCurrentAssets', None)
        self.retainedEarnings = report.get('retainedEarnings', None)
        self.otherLiab = report.get('otherLiab', None)
        self.goodWill = report.get('goodWill', None)
        self.treasuryStock = report.get('treasuryStock', None)
        self.otherAssets = report.get('otherAssets', None)
        self.cash = report.get('cash', None)
        self.totalCurrentLiabilities = report.get(
            'totalCurrentLiabilities', None)
        self.deferredLongTermAssetCharges = report.get(
            'deferredLongTermAssetCharges', None)
        self.shortLongTermDebt = report.get('shortLongTermDebt', None)
        self.otherStockholderEquity = report.get(
            'otherStockholderEquity', None)
        self.propertyPlantEquipment = report.get(
            'propertyPlantEquipment', None)
        self.totalCurrentAssets = report.get('totalCurrentAssets', None)
        self.longTermInvestments = report.get('longTermInvestments', None)
        self.netTangibleAssets = report.get('netTangibleAssets', None)
        self.shortTermInvestments = report.get('shortTermInvestments', None)
        self.netReceivables = report.get('netReceivables', None)
        self.longTermDebt = report.get('longTermDebt', None)
        self.inventory = report.get('inventory', None)
        self.accountsPayable = report.get('accountsPayable', None)


class IncomeStatementHistoryQuarterly(SqliteBase.Base):

    __tablename__ = "incomeStatementHistoryQuarterly"

    date = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    ticker = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    sql_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    researchDevelopment = sqlalchemy.Column(sqlalchemy.BIGINT)
    effectOfAccountingCharges = sqlalchemy.Column(sqlalchemy.BIGINT)
    incomeBeforeTax = sqlalchemy.Column(sqlalchemy.BIGINT)
    minorityInterest = sqlalchemy.Column(sqlalchemy.BIGINT)
    netIncome = sqlalchemy.Column(sqlalchemy.BIGINT)
    sellingGeneralAdministrative = sqlalchemy.Column(sqlalchemy.BIGINT)
    grossProfit = sqlalchemy.Column(sqlalchemy.BIGINT)
    ebit = sqlalchemy.Column(sqlalchemy.BIGINT)
    operatingIncome = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherOperatingExpenses = sqlalchemy.Column(sqlalchemy.BIGINT)
    interestExpense = sqlalchemy.Column(sqlalchemy.BIGINT)
    extraordinaryItems = sqlalchemy.Column(sqlalchemy.BIGINT)
    nonRecurring = sqlalchemy.Column(sqlalchemy.BIGINT)
    otherItems = sqlalchemy.Column(sqlalchemy.BIGINT)
    incomeTaxExpense = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalRevenue = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalOperatingExpenses = sqlalchemy.Column(sqlalchemy.BIGINT)
    costOfRevenue = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalOtherIncomeExpenseNet = sqlalchemy.Column(sqlalchemy.BIGINT)
    discontinuedOperations = sqlalchemy.Column(sqlalchemy.BIGINT)
    netIncomeFromContinuingOps = sqlalchemy.Column(sqlalchemy.BIGINT)
    netIncomeApplicableToCommonShares = sqlalchemy.Column(sqlalchemy.BIGINT)

    def __init__(self, date, ticker, report) -> None:
        self.date = date
        self.ticker = ticker
        self.sql_date = formate_date(date)
        self.researchDevelopment = report.get('researchDevelopment', None)
        self.effectOfAccountingCharges = report.get(
            'effectOfAccountingCharges', None)
        self.incomeBeforeTax = report.get('incomeBeforeTax', None)
        self.minorityInterest = report.get('minorityInterest', None)
        self.netIncome = report.get('netIncome', None)
        self.sellingGeneralAdministrative = report.get(
            'sellingGeneralAdministrative', None)
        self.grossProfit = report.get('grossProfit', None)
        self.ebit = report.get('ebit', None)
        self.operatingIncome = report.get('operatingIncome', None)
        self.otherOperatingExpenses = report.get(
            'otherOperatingExpenses', None)
        self.interestExpense = report.get('interestExpense', None)
        self.extraordinaryItems = report.get('extraordinaryItems', None)
        self.nonRecurring = report.get('nonRecurring', None)
        self.otherItems = report.get('otherItems', None)
        self.incomeTaxExpense = report.get('incomeTaxExpense', None)
        self.totalRevenue = report.get('totalRevenue', None)
        self.totalOperatingExpenses = report.get(
            'totalOperatingExpenses', None)
        self.costOfRevenue = report.get('costOfRevenue', None)
        self.totalOtherIncomeExpenseNet = report.get(
            'totalOtherIncomeExpenseNet', None)
        self.discontinuedOperations = report.get(
            'discontinuedOperations', None)
        self.netIncomeFromContinuingOps = report.get(
            'netIncomeFromContinuingOps', None)
        self.netIncomeApplicableToCommonShares = report.get(
            'netIncomeApplicableToCommonShares', None)

class FinData(SqliteBase.Base):

    __tablename__ = "fin_data"

    ticker = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    ebitdaMargins = sqlalchemy.Column(sqlalchemy.FLOAT)
    profitMargins = sqlalchemy.Column(sqlalchemy.FLOAT)
    grossMargins = sqlalchemy.Column(sqlalchemy.FLOAT)
    operatingCashflow = sqlalchemy.Column(sqlalchemy.BIGINT)
    revenueGrowth = sqlalchemy.Column(sqlalchemy.FLOAT)
    operatingMargins = sqlalchemy.Column(sqlalchemy.FLOAT)
    ebitda = sqlalchemy.Column(sqlalchemy.BIGINT)
    targetLowPrice = sqlalchemy.Column(sqlalchemy.FLOAT)
    recommendationKey = sqlalchemy.Column(sqlalchemy.String)
    grossProfits = sqlalchemy.Column(sqlalchemy.BIGINT)
    freeCashflow = sqlalchemy.Column(sqlalchemy.BIGINT)
    targetMedianPrice = sqlalchemy.Column(sqlalchemy.FLOAT)
    currentPrice = sqlalchemy.Column(sqlalchemy.FLOAT)
    earningsGrowth = sqlalchemy.Column(sqlalchemy.FLOAT)
    currentRatio = sqlalchemy.Column(sqlalchemy.FLOAT)
    quickRatio = sqlalchemy.Column(sqlalchemy.FLOAT)
    returnOnAssets = sqlalchemy.Column(sqlalchemy.FLOAT)
    numberOfAnalystOpinions = sqlalchemy.Column(sqlalchemy.INTEGER)
    targetMeanPrice = sqlalchemy.Column(sqlalchemy.FLOAT)
    debtToEquity = sqlalchemy.Column(sqlalchemy.FLOAT)
    returnOnEquity = sqlalchemy.Column(sqlalchemy.FLOAT)
    targetHighPrice = sqlalchemy.Column(sqlalchemy.FLOAT)
    totalCash = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalDebt = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalRevenue = sqlalchemy.Column(sqlalchemy.BIGINT)
    totalCashPerShare = sqlalchemy.Column(sqlalchemy.FLOAT)
    financialCurrency = sqlalchemy.Column(sqlalchemy.String)
    maxAge = sqlalchemy.Column(sqlalchemy.Integer)
    revenuePerShare = sqlalchemy.Column(sqlalchemy.FLOAT)
    recommendationMean = sqlalchemy.Column(sqlalchemy.FLOAT)

    def __init__(self, _, ticker, report) -> None:

        self.ticker = ticker
        self.ebitdaMargins = report.get('ebitdaMargins', None).get('raw', None)
        self.profitMargins = report.get('profitMargins', None).get('raw', None)
        self.grossMargins = report.get('grossMargins', None).get('raw', None)
        self.operatingCashflow = report.get('operatingCashflow', None).get('raw', None)
        self.revenueGrowth = report.get('revenueGrowth', None).get('raw', None)
        self.operatingMargins = report.get('operatingMargins', None).get('raw', None)
        self.ebitda = report.get('ebitda', None).get('raw', None)
        self.targetLowPrice = report.get('targetLowPrice', None).get('raw', None)
        self.recommendationKey = report.get('recommendationKey', None)
        self.grossProfits = report.get('grossProfits', None).get('raw', None)
        self.freeCashflow = report.get('freeCashflow', None).get('raw', None)
        self.targetMedianPrice = report.get('targetMedianPrice', None).get('raw', None)
        self.currentPrice = report.get('currentPrice', None).get('raw', None)
        self.earningsGrowth = report.get('earningsGrowth', None).get('raw', None)
        self.currentRatio = report.get('currentRatio', None).get('raw', None)
        self.quickRatio = report.get('quickRatio', None).get('raw', None)
        self.returnOnAssets = report.get('returnOnAssets', None).get('raw', None)
        self.numberOfAnalystOpinions = report.get('numberOfAnalystOpinions', None).get('raw', None)
        self.targetMeanPrice = report.get('targetMeanPrice', None).get('raw', None)
        self.debtToEquity = report.get('debtToEquity', None).get('raw', None)
        self.returnOnEquity = report.get('returnOnEquity', None).get('raw', None)
        self.targetHighPrice = report.get('targetHighPrice', None).get('raw', None)
        self.totalCash = report.get('totalCash', None).get('raw', None)
        self.totalDebt = report.get('totalDebt', None).get('raw', None)
        self.totalRevenue = report.get('totalRevenue', None).get('raw', None)
        self.totalCashPerShare = report.get('totalCashPerShare', None).get('raw', None)
        self.financialCurrency = report.get('financialCurrency', None)
        self.maxAge = report.get('maxAge', None)
        self.revenuePerShare = report.get('revenuePerShare', None).get('raw', None)
        self.recommendationMean = report.get('recommendationMean', None).get('raw', None)

