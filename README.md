# QACafe
Case Study For DTS Level 6 Software/DevOps

## Problem Statement
* QA Café is looking for a Workforce Management application to handle the HR details of staff across 16 locations plus 7 franchised locations. 
* This application will have to be centrally accessible by both the mainline sites as well as the franchised sites, meaning web access is required.
* The learners will have to orchestrate a pipeline that will allow for development of this application as well as deploying the application for use by all sites.
* The learners will have to decide whether to use a single centralised application in a live environment or multiple instances of the application across multiple environments.
* Learners should consider the benefits of hosting this pipeline and the subsequent environments in the cloud, as well as which cloud solution would be most appropriate.
* Learners will have to consider containerisation as an option for rolling out updates and bug fixes.
* The pipeline should rigorously test the application on building, the learners should consider what frameworks to use to ensure consistent, long term testing.
* The learners will have to consider what personal details a Workforce Management application will require and therefore what measures should be in place to ensure the security of said data.

## Functional Requirements
* Should store the details of all QA Café employees. 
* Should be amendable at all times, whilst not losing any important data, such as employment start dates, holiday requests etc.
* Each site should have their own group of employees and should only be accessible to management at that site. Site A shouldn’t be able to adjust stored details for site B’s staff etc. It’s up to the learners how this could be achieved.

## Operational Requirements
* The application should be accessible to each site from a single location (URL) so reverse proxy’s/load balancers should be considered.
* The application should be containerised to allow for rolling updates while not removing access to the application at any time.
