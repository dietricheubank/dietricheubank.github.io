# Clinical Endpoint Modernization Simulator

A fictional planning exercise for healthcare endpoint modernization. All device volumes, architecture choices, workload assumptions, and numerical inputs are synthetic.

## What it does
- Choose a fictional shared versus assigned station mix
- Change migration volume, pilot size, weekly team capacity and number of teams
- Validate six conceptual readiness gates
- Model indicative post-pilot deployment waves and capacity constraints
- Stop treating readiness as approved when mandatory checks are not met

## Important exclusions
No real employer information, deployment schedule, configuration settings, vendor pricing, performance benchmark, clinical workflows or patient data is included. This is not a medical device validation tool or clinical change authorization system.

## Simulation math
- Shared stations = rounded total times chosen fictional mix
- Weekly capacity = devices per team per week times teams
- Deployment weeks = ceiling((scope - pilot) / weekly capacity)
- Gates are instructional checkboxes; checking them does not demonstrate real validation

## Additional development
Future releases could include independent validation evidence, site-specific work windows, dependency scheduling, optional contingency capacity and more detailed issue-triage examples using synthetic data.
