---
title: SanteMPI
nav_order: 1
---

# SanteMPI

SanteMPI is a proven, next-generation, fully featured Master Patient
Index/Client Registry (MPI/CR) platform designed to overcome barriers to
leveraging person-centered data as a catalyst for transforming health
systems. It is an essential national digital health infrastructure
component that leverages unique identity to facilitate data
consolidation, harmonization, sharing, and building health information
exchanges (e.g., OpenHIE) to establish interoperability across multiple
software solutions. It is a flexible architecture and online/offline
capability also supports large scale registration programs such as
COVID-19 vaccination registration, and birth and death updates to a
CRVS. SanteMPI fulfills these essential roles by implementing all
relevant interoperability specifications and requirements related to
Client Registry in the OpenHIE specification, including Client Registry
as a service, HL7 FHIR, and widely deployed legacy standards like HL7v2.

### Approach

SanteMPI is one of the SanteSuite products, which allows the SanteDB
iCDR to operate as a Master Person/Patient Index. SanteMPI provides a
series of plugins, API interfaces, and user interfaces to manage the
registration of patients, de-duplication and integration of their
records from multiple source systems within a jurisdiction.
Functionality includes searching, matching, de-duplication, generation
of patient population statistics Examples where a Master Patient Index
are leveraged are:

- Hospitals whereby multiple departmental systems require integration of
  a consistent patient identity.
- Jurisdictions (states, provinces, countries, etc.) which wish to
  deploy consistent patient identity.
- Research projects which require merging/harmonization of multiple data
  sets, etc.

The primary users of SanteMPI are digital health architects, data base
managers, software integrators, those responsible for identity
management, health information exchange implementers, users of any
digital health application that depends on uniquely identifying a
person/patient.

### Implementations

SanteMPI and its predecessor MEDIC CR are used internationally. It has
been integrated with immunization information systems (Tanzania\'s TImR)
to implement patient registration and ensure that patients are assigned
unique ID\'s. It was implemented in Myanmar to support harmonization of
patient data across the OpenMRS installed base supporting the HIV/TB
programs. It is currently under evaluation for use in a couple of large
initiatives in Africa and in the assessment and planning phase of a
multi-country deployment in East Asia/Pacific.

### Resources

- Website:
  <https://help.santesuite.org/product-overview/santesuite-products/master-patient-index-santempi>
- Source Code: <https://github.com/santedb/santempi>
- Articles:[Working towards a master patient index and unique
  identifiers to improve health systems: the example of
  Myanmar](https://www.who-seajph.org/article.asp?issn=2224-3151;year=2019;volume=8;issue=2;spage=83;epage=86;aulast=Thorell)
