# search-api

#MOTIVATION

Due to the large volume of data generated by the TERRA-REF project, it can be challenging for a user to locate 
specific data about a given experiment, or to find data or view images associated with a particular day or scan of 
the plot. The goal of this search api is to provide a tool that would make locating data easier. 

#DESIGN

#RESULTS PROVIDED

Depending on the query, results will be returned as a json, or as a json containing links to download datasets from 
the terra clowder instance, links to csvs, or other files. For all queries a 'count' method will be provided which shows 
the user how much data will be returned. If a particular query will return a very large result, the user can then
further refine the query to return fewer results.

# MAPPING, CLOWDER, BETYDB, BRAPI, SEARCH-API

cultivar, cultivar, germplasm, germplasm

experiment.id, experiment.id, studydbid, studydbid

site.id, site.id, observationunitdbid, observationunitdbid
sitename, sitename, observationunitname, observationunitname




#SWAGGER DOCUMENTATION

https://search-api-dev.workbench.terraref.org/search-api/v1/ui/

#DEPLOYMENT INSTRUCTIONS

