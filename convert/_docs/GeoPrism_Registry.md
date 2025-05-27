---
title: GeoPrism Registry
nav_order: 1
---

# GeoPrism Registry {#geoprism_registry}

GeoPrism Registry is an open-source Common Geo-Registry (CGR)
implementation that utilizes spatial knowledge graphs to provide a
single source of truth for managing geographic data over time across
multiple organizations and information systems. It is used to host,
manage, regularly update and share lists, associated hierarchies, and
geospatial data through time for geographic objects core to spatial data
infrastructure, sustainable development, and public health (e.g.,
administrative divisions, settlements, health facilities, schools, and
other relevant physical and non-physical geographic features).

Information systems used to make decisions often have different pictures
of the geographies (i.e., people, places, and infrastructures) they
respectively cover. Within a single area, different programs collect and
store different geographic data in siloed systems at different times,
leading to discrepancies and duplication of effort. This also results in
decisions based on incomplete and out-of-date geographic data (e.g.,
spatial distribution of population and resources), ineffective resource
allocation, and in the worst cases, affected populations being missed
completely during times of crisis. For example, DHIS2 is limited to a
single hierarchy that is configured primarily for reporting purposes. It
is not necessarily the same hierarchy that is best suited for a health
worker, client, or facility registry. Additionally, the same identifiers
are not being used for the common locations referenced across these
systems. In order to perform trend analysis, data from multiple health
information systems need to be properly contextualized across space and
time.

### Approach

Just as a terminology service can standardize vocabularies for
interoperability across a health information ecosystem, GeoPrism
Registry standardizes location identity, classification, geometries, and
how locations are used in multiple and interrelated hierarchies. Health
information systems do not need to conform to the hierarchy structure of
a single system, such as an instance of DHIS2. Rather, GeoPrism can
track different hierarchies used by multiple systems and how they relate
to each other. For example, a facility registry can have different
levels in its hierarchy than an instance of DHIS2, and yet GeoPrism can
facilitate synchronization of health facilities between the two systems
for the correct operational and administrative boundaries. This
compliments the capabilities of the Global Open Facility Registry (GOFR)
Facility Match tool developed by IntraHealth, which focuses on
reconciling facility lists maintained by multiple sources but does not
model the time component. GeoPrism is interoperable with FHIR/mCSD and
DHIS2.

### Implementations

GeoPrism's ontology, GIS, hierarchy management, metadata-driven data
management, cross-platform, and fully localizable technology stack has
been deployed to support disease intervention and elimination efforts
for over ten years. These capabilities were originally developed for the
Innovative Vector Control Consortium (IVCC) to build the Disease Data
Management System (DDMS). GeoPrism is the technical foundation for the
DDMS and provides hierarchy and ontology management for normalizing
disparate datasets by common geographies and ontological terms,
integration with DHIS2, and spatial dashboarding capabilities. The DDMS
has been implemented in several countries in Africa and Asia, including
Zambia, Bioko, Ethiopia, the Philippines, and currently in three
provinces in India.

TerraFrame was selected by the Digital Solutions for Malaria Elimination
(DSME) initiative to implement the requirements of a Common Geo-Registry
(CGR) by leveraging and expanding upon the multi-hierarchy management
and ontology capabilities of GeoPrism, which is now called GeoPrism
Registry. A workshop in April of 2018 was conducted at the University of
Oslo (UiO) to evaluate the DHIS2, GeoPrism, and other platforms as
potential candidates for implementing the CGR requirement. The workshop
concluded with UiO endorsing TerraFrame's GeoPrism technology as being
several steps ahead of anything in the industry for multi-hierarchy
management.

GeoPrism Registry is the latest iteration of the technology that started
with the DDMS and has been deployed in Laos, Mozambique, and for the US
Federal Government. The core GeoPrism spatial knowledge graphing
technology has been deployed for the US Department of Interior and is
being used by the Office of Surface Mining Reclamation and Enforcement,
US Fish and Wildlife, and the US Forest Service. Importantly,
TerraFrame's work with the US Federal Government has resulted in
significant enhancements to the technology that are being used in health
sector implementations and continues to be a revenue stream for
improvements and maintenance. By exclusively using an open-source
business model, TerraFrame has been able to sustain GeoPrism throughout
the years by implementing cross-sectoral enhancements into the core
technology so that enhancements and maintenance are not funded by a
single industry vertical.

Laos PDR: In 2019, the Laos Malaria Program aimed to stratify villages
according to malaria endemicity to help improve resource efficiency.
However, access to geographic data was limited, with notable data
quality issues and inconsistencies (e.g., missing geo-coordinates,
unvalidated village names, inconsistent hierarchies). CHAI worked with
the Department of Healthcare and Rehabilitation, the Department of
Planning and Cooperation (DPC), and the World Health Organization to
define a custodian of a health facility master list and a Ministry of
Health (MOH)-wide village master list, improve their quality and
management processes, and then deployed the datasets in the GPR platform
from 2020-2022. The GPR helped to make standardized and up-to-date
lists, hierarchies, and geospatial data accessible to programs across
the MOH and its functionalities simplified maintenance and regular
update. Since installation, the health facility master list and village
list in the GPR have been used to develop an access to care map in Bokeo
Province to support the MOH in their planning for distribution of
specialty health services and establishment of clinics. In addition, the
GPR is being fully integrated with the national DHIS2-based Health
Management Information System, to ensure accessibility of content to all
MOH programs at any level of the health system. Finally, DPC has engaged
with the Ministry of Planning and Investment and the Ministry of Home
Affairs to deploy additional master lists and associated data to the
GPR, such as a medical warehouse and public pharmacy master list which
will be available on the GPR platform in 2023.

Mozambique: In Mozambique, the GPR is governed by the Spatial
Development Agency (ADE), taking a cross-sectoral management approach.
The ADE team was trained on management and use of the GPR platform in
2022. Successive training with MOH agencies will occur to familiarize
Registry Administrators and Maintainers with the functionalities of the
GPR platform and their roles and responsibilities in reviewing and
maintaining datasets. These teams will work together to manage masters
lists and geo-coordinates for health facilities, vaccination
concentration points, and mobile health brigades in two districts to
support vaccine microplanning for routine childhood vaccine
distribution. In addition to these datasets, national administrative
boundaries and partial health facility lists are available on the
platform. The ADE team is actively engaging other MOH departments to
expand these master lists to include nationally representative data for
health facilities. Ongoing advocacy efforts are underway to bring
additional ministry teams (even outside of the ministry of health) to
host their data in the platform for central management.

GeoPrism Registry is a multi-tenant platform that is designed to give
organizations, such as government ministries, the ability to curate and
publish data over which they have the curation mandate, such as master
lists, associated hierarchies, and geospatial data for the geographic
objects.

### Resources

- Website: <https://terraframe.atlassian.net/wiki/spaces/GGR/overview>
- Source Code: <https://github.com/terraframe/geoprism-registry>
- GeoPrism Registry uses GeoPrism for visualizations:
  <https://github.com/terraframe/geoprism>
- GeoPrism Registry is built on RunwaySDK and uses its metadata-driven
  spatial knowledge graph framework:
  <https://github.com/terraframe/Runway-SDK>
- The Disease Data Management System (DDMS) has been deployed in
  multiple countries over the past 12 years and is still being used
  today in three provinces in India. DDMS is built on GeoPrism and
  RunwaySDK:<https://github.com/terraframe/DDMS>
- References for DDMS:
  - <https://etch.lstmed.ac.uk/projects/associated-projects/disease-data-management-system>
  - <https://www.lstmed.ac.uk/research/departments/vector-biology/monitoring-and-evaluation/the-disease-data-management-system>
- Articles:
  - [Version 2.0 of the Common Geo-Registry guidance, which incorporates
    lessons learned from the initial GeoPrism Registry
    implementation](https://healthgeolab.net/DOCUMENTS/Guidance_Common_Geo-registry_Ve2.pdf)
  - <https://dsme.community/common-geo-registry/>
  - [MSF paper when GPR was referred to
    CGR](https://drive.google.com/file/d/1m0vk3Oz5UZ-ji8jYrYaRuGP9ji8bNPHm/view?usp=sharing)
