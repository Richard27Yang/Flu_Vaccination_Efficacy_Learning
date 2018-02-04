# Data sources
To accurately predict the effictivenss of the flu vaccine, data sources is required to be robust and reliable. In this proposal, the core data originates from the United States Center for Disease Control (CDC) FluView utility, which contains robust and standardized information gathered across each state across United States. Data is gathered from 2000 and keeps updates by week. 
Three different resources of data  is listed:

* CDC - A Weekly Influenza Surveillance Report Prepared by the Influenza Division, Influenza-Like Illness (ILI) Activity Level Indicator Determined by Data Reported to ILINet(https://gis.cdc.gov/grasp/fluview/main.html)
  The dataset is extracted from CDC's influenza surveillance systems, the WHO/NREVSS Collaborating Labs and the US Outpatient Influenza-like Illness Surveillance Network (ILINet). It presents the Year, Week, State, ILI Activity Level since 2008.

* CDC BRFSS - Behavioral Risk Factor Surveillance System (BRFSS) data (https://www.cdc.gov/brfss/index.html).
This whole dataset contains information for health-related risk behaviors, chronic health conditions, and use of preventive services. 
Regarding the present study, the useful information for the present study is the Year,	Locationabbr,	Locationdesc,	flu vaccine, GeoLocation.

* CDC - Pneumonia and Influenza Mortality Surveillance from the National Center for Health Statistics Mortality Surveillance System. (https://gis.cdc.gov/grasp/fluview/mortality.html)
The information in this dataset contains States,	Age group,	Year,	Week,	PERCENT P&I,	NUM INFLUENZA AND PNEUMONIA DEATHS.

The final combined dataset contains data covers:
* States Records 
* Year From 2008 to 2017
* Week from 1-52 typically each year
* Activity Level from 0-10, which is used to measure of the number of cases of Influenza.
* Flu vaccined taken percentage for adults older than 65 by BRFSS survey
* Pneumonia and Influenza Mortality number from 2008-2016


