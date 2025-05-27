---
title: Iaso
nav_order: 1
---

# Iaso

Iaso is an open source data collection, campaign monitoring and facility
registry solution used mainly in health, currently in use in
performance-based financing projects, polio campaigns tracking, facility
registries and support to World Food Programme beneficiaries tracking.
Iaso provides a number of core features in support of continuous
geospatial data management: a mobile application, a web dashboard, a
matching feature to merge various data sources, a data science and
scripting interface and a seamless bi-directional integration with
DHIS2. Here are some of the features:

- Structured data collection using the xlsform format as its core, but
  adding entities and org units (Ã  la DHIS2)
- Managing as many referential lists as you want
- Facilitating the continuous data management of the master lists
- Easy to use by multiple teams in parallel
- Data sciences in support of georegistry management
- Fine grained geography based accesses and traceability
- Planning pre-campaign micro-planification survey from team dispatch
  coverage to survey design

Iaso tries to fill a gap in the digital health ecosystem by providing at
the same time features as a georegistry (holding the GIS referential,
and improving it), large scale data collection (the brunt of the work)
and planification (allocate, using the GIS referential, data collection
tasks to do).

### Approach

Iaso's strong integration with DHIS2, with tools to setup data exports
with matching interface, and a very lightweight mobile application based
on ODK makes it an interesting candidate for data collections where data
is ultimately analyzed in DHIS2. Another focus of the tool is on
microplanning activities for campaigns (e.g. MDA or vaccination) where
the aim is to provide planification tools, with the corresponding
monitoring of activities. The tool includes out of the box user
management with clear access rights based on hierarchical geographies,
and this is leveraged to allow organization of country wide
planification effort, with each region being able to handle its own
planning and monitoring. The primary users of Iaso are ministries of
Health, NGOs, WHO, Institute of Statistics, all institutions involved in
doing data collection related to locations (typically, statistics that
need to be collected offline, then aggregated on a regional level).

### Implementations

Iaso was first created for a project in DRC to gather data about
community health worker where it is still used. It was then adopted to
perform data collection for performance-based financing in at least ten
countries, with thousands of users. In many of these countries (Uganda,
Burundi, Ivory Coast), Iaso is in the process of hosting the software
locally to ensure the sustainability of the projects. Iaso has also been
used as a georegistry tool for the Ministries of health of DRC and Niger
to update the master facility list of these two countries.

Now, it is being used as the platform to encode data about polio
vaccination campaigns at WHO Afro and to prepare maps allowing to follow
the scope of these campaigns:
[1](https://afro-rrt-who.hub.arcgis.com/pages/Campaigns%20(SIAs)).
Finally, it has been picked by the World Food Programme as the base on
which to build their new conditional on-demand assistance tool, with
support for beneficiaries and complex workflows involving mobile devices
and NFC cards.

### Resources

- Website: <https://www.bluesquarehub.com/iaso/>
- Source Code: <https://github.com/BLSQ/iaso>
- Articles:
  <https://www.cordaid.org/en/news/better-data-better-schools-better-education/>
