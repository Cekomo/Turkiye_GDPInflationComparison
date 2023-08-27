# WorldBankAnalysis
Analysis of data in World Bank databases.

## TableManipulator
This file is to shaping structure of the table such as omitting commas, making text numeric if they consist of numbers etc.
Make sure manipulated file is at the same directory with the manipulator. 
Due to file permission issues, it may be required to execute python file in cmd (open as administrator) to not encounter "file not found" error.

## Where did data come from
- All economics related data is taken from World Bank.
- HDI, life expectancy data taken from UNDP.
- Literacy data taken from World Bank and poverty rate taken from OECD (possible most recent year extracted).
- Countries spoken languages data is generated using Chat-GPT.
- Countries (ISO code, region, capital city, area, population, currency) table is generated using Chat-GPT.