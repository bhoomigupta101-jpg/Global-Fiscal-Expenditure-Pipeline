USE PublicSpendingDB;
GO
CREATE OR ALTER VIEW vw_Final_Executive_Report AS
SELECT
    REF_AREA_LABEL AS Country,
    SECTOR_LABEL AS Government_Level,
    UNIT_MEASURE_LABEL AS Currency_Type,
    TRY_CAST(Year AS INT) AS FiscalYear,
    TRY_CAST(Amount AS FLOAT) AS RawAmount,
    CASE
        WHEN SECTOR_LABEL = 'General government' THEN 'Total'
        ELSE 'DEPARTMENTAL'
    END AS Data_Hierarchy
FROM dbo.Fact_Spending
WHERE UNIT_MEASURE_LABEL = 'Domestic currency'
  AND Amount > 0;
GO